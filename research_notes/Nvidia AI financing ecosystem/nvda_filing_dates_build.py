#!/usr/bin/env python3
"""Build nvda_filing_dates.csv from SEC EDGAR submissions data (CIK 1045810, NVIDIA Corp).

Source endpoints (retrieved 2026-11-22):
  https://data.sec.gov/submissions/CIK0001045810.json
  https://data.sec.gov/submissions/CIK0001045810-submissions-001.json
Usage: python3 nvda_filing_dates_build.py [out.csv] [start_date=2016-05-01]
The earnings release for a quarter is taken as the LAST Form 8-K carrying Item 2.02 (or
pre-Aug-2004 Item 12) filed after the previous periodic report and on/before the 10-Q/10-K;
earlier Item 2.02 8-Ks in the same window (pre-announcements) are listed separately.
Deadlines: 40 days (10-Q) / 60 days (10-K) after period end for a large accelerated filer,
rolled forward over weekends only (federal holidays are NOT modelled).
The Q3 FY2027 period end (2026-10-25) is hard-coded from EX-99.1 of the 2026-11-17 8-K.
"""
import csv, datetime as dt, json, subprocess, sys, time
from zoneinfo import ZoneInfo

UA = "research-notes-script/1.0 (filing date research)"
BASE = "https://data.sec.gov/submissions/"
ET = ZoneInfo("America/New_York")
D = dt.date.fromisoformat

def fetch(name):
    out = subprocess.run(["curl", "-sS", "-m", "60", "-A", UA, BASE + name],
                         capture_output=True, text=True, check=True).stdout
    time.sleep(0.3)
    return json.loads(out)

def load():
    rows = []
    def add(r):
        for i in range(len(r["form"])):
            rows.append({k: r[k][i] for k in r})
    d = fetch("CIK0001045810.json")
    add(d["filings"]["recent"])
    for f in d["filings"].get("files", []):
        add(fetch(f["name"]))
    rows.sort(key=lambda x: (x["filingDate"], x["acceptanceDateTime"]))
    return rows

def et(s):
    if not s:
        return ""
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(ET).strftime("%Y-%m-%d %H:%M ET")

def url(r):
    a = r["accessionNumber"]
    return f"https://www.sec.gov/Archives/edgar/data/1045810/{a.replace('-', '')}/{r['primaryDocument']}"

def label(pe):
    m = pe.month
    if m in (4, 5): return f"Q1 FY{pe.year + 1}"
    if m in (7, 8): return f"Q2 FY{pe.year + 1}"
    if m in (10, 11): return f"Q3 FY{pe.year + 1}"
    return f"Q4 FY{pe.year}"

def roll(d):
    while d.weekday() >= 5:
        d += dt.timedelta(days=1)
    return d

def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "nvda_filing_dates.csv"
    start = sys.argv[2] if len(sys.argv) > 2 else "2016-05-01"
    today = dt.date(2026, 11, 22)
    rows = load()
    per = [r for r in rows if r["form"] in ("10-Q", "10-K") and r["filingDate"] >= start]
    e8 = [r for r in rows if r["form"] == "8-K" and any(i in r["items"].split(",") for i in ("2.02", "12"))]
    res, prev_f = [], None
    for p in per:
        pe = D(p["reportDate"])
        lo = prev_f if prev_f else pe
        c = [e for e in e8 if lo < D(e["filingDate"]) <= D(p["filingDate"]) and D(e["filingDate"]) > pe]
        er, pre = (c[-1], c[:-1]) if c else (None, [])
        n = 40 if p["form"] == "10-Q" else 60
        due = roll(pe + dt.timedelta(days=n))
        pa = et(p["acceptanceDateTime"])
        res.append(dict(
            fiscal_period=label(pe), period_end=p["reportDate"],
            earnings_8k_report_date=er["reportDate"] if er else "",
            earnings_8k_filing_date=er["filingDate"] if er else "",
            earnings_8k_acceptance_et=et(er["acceptanceDateTime"]) if er else "",
            earnings_8k_items=er["items"] if er else "",
            earnings_8k_accession=er["accessionNumber"] if er else "",
            earnings_8k_url=url(er) if er else "",
            periodic_form=p["form"], periodic_filing_date=p["filingDate"], periodic_acceptance_et=pa,
            periodic_accession=p["accessionNumber"], periodic_url=url(p),
            gap_days_official_filing_dates=(D(p["filingDate"]) - D(er["filingDate"])).days if er else "",
            gap_days_by_acceptance_date=(D(pa[:10]) - D(et(er["acceptanceDateTime"])[:10])).days if er else "",
            days_period_end_to_periodic=(D(p["filingDate"]) - pe).days,
            sec_deadline_days=n, sec_deadline_weekend_rolled=due.isoformat(),
            days_filed_before_deadline=(due - D(p["filingDate"])).days,
            other_item_2_02_8ks_same_quarter="; ".join(
                f"{e['filingDate']} ({e['accessionNumber']}, items {e['items']})" for e in pre),
            note="",
            source="SEC EDGAR data.sec.gov/submissions/CIK0001045810.json and CIK0001045810-submissions-001.json, retrieved 2026-11-22"))
        prev_f = D(p["filingDate"])
    pe = dt.date(2026, 10, 25)
    due = roll(pe + dt.timedelta(days=40))
    for e in [e for e in e8 if D(e["filingDate"]) > prev_f]:
        res.append(dict(
            fiscal_period="Q3 FY2027", period_end=pe.isoformat(),
            earnings_8k_report_date=e["reportDate"], earnings_8k_filing_date=e["filingDate"],
            earnings_8k_acceptance_et=et(e["acceptanceDateTime"]), earnings_8k_items=e["items"],
            earnings_8k_accession=e["accessionNumber"], earnings_8k_url=url(e),
            periodic_form="10-Q", periodic_filing_date=f"NOT FILED as of {today}", periodic_acceptance_et="",
            periodic_accession="", periodic_url="",
            gap_days_official_filing_dates=f"open: {(today - D(e['filingDate'])).days} days elapsed at {today}",
            gap_days_by_acceptance_date="open",
            days_period_end_to_periodic=f"open: {(today - pe).days} days elapsed at {today}",
            sec_deadline_days=40, sec_deadline_weekend_rolled=due.isoformat(),
            days_filed_before_deadline=f"n/a ({(due - today).days} days remain at {today})",
            other_item_2_02_8ks_same_quarter="",
            note="Period end 2026-10-25 taken from EX-99.1 of the 2026-11-17 8-K; no 10-Q or NT 10-Q for this period "
                 "appears in the EDGAR submissions feed as of retrieval",
            source="SEC EDGAR data.sec.gov/submissions/CIK0001045810.json, retrieved 2026-11-22"))
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(res[0].keys()))
        w.writeheader()
        w.writerows(res)
    print(f"wrote {len(res)} rows to {out}")

if __name__ == "__main__":
    main()
