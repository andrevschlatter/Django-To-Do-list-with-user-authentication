# Nvidia's Q3 FY2027 10-Q timing: EDGAR record, precedents, deadline and consequences

Research date: 2026-11-22. Companion data files in this folder:

- `nvda_filing_dates.csv`: 43 rows, Q1 FY2017 to Q3 FY2027, built from EDGAR.
- `nvda_filing_dates_build.py`: the script that rebuilds the CSV from `data.sec.gov`.
- `precedent_filing_timelines.csv`: 220 EDGAR filings for 20 comparison companies (accession numbers and URLs).

**How to read the sourcing in these notes**

- **Dates, form types, 8-K item codes, accession numbers:** pulled directly (raw JSON, via curl) from `https://data.sec.gov/submissions/CIK0001045810.json` and `CIK0001045810-submissions-001.json` on 2026-11-22. These are exact.
- **Text of filings on `www.sec.gov/Archives`:** direct curl was refused (HTTP 403, "undeclared automated tool") with a generic User-Agent, so filing text was read through the WebFetch tool. That tool returns model-extracted text with short quotes. Quotes below are as returned by the tool and should be checked against the original before publication.
- **Press and analyst coverage:** news sites (TechCrunch, Longbridge, InvestmentNews, Nasdaq.com, Nvidia's investor site, eCFR, Cornell LII) were unreachable from this session, and the shared web-search budget ran out after two successful searches. Everything attributed to press or analysts comes from **search-tool summaries of result pages, not from article text**, and is tagged accordingly.
- **Tags:** [FILING/ON-RECORD], [ANONYMOUSLY SOURCED], [ANALYST ESTIMATE], [UNVERIFIED]. "(pre-Nov 17)" marks a source dated before November 17, 2026.

---

## 1. Filing-date table, Q1 FY2017 to Q3 FY2027, and the pattern

### Takeaway
The lead is confirmed: Nvidia furnished Q3 FY2027 results on November 17, 2026 and, as of November 22, has filed no 10-Q and no NT 10-Q for the quarter ended October 25, 2026. "Same-day 10-Q" is a practice that dates only from August 2018, with eight exceptions of 2 to 7 days since then; the current open gap (5 days) has not yet exceeded the post-2018 maximum of 7 days, but will on November 25.

### Cited Findings

**Table.** Every row is from the EDGAR submissions feed (source above). "Gap" is periodic-report filing date minus earnings 8-K filing date; the second figure uses the EDGAR acceptance date, which differs when a filing was accepted after 5:30 p.m. ET. Deadlines are 40 days (10-Q) or 60 days (10-K) after period end, rolled over weekends only.

| Fiscal period | Period end | Earnings 8-K (Item 2.02): report date / filing date | Earnings 8-K accession | Periodic report | Filing date (acceptance, ET) | Periodic accession | Gap, days (official / by acceptance date) | Deadline (40/60 d) | Days before deadline |
|---|---|---|---|---|---|---|---|---|---|
| Q1 FY2017 | 2016-05-01 | 2016-05-12 / 2016-05-12 | [0001045810-16-000243](https://www.sec.gov/Archives/edgar/data/1045810/000104581016000243/form8-kq117.htm) | 10-Q | 2016-05-25 (05-25 16:55 ET) | [0001045810-16-000275](https://www.sec.gov/Archives/edgar/data/1045810/000104581016000275/nvda2017q110q.htm) | 13 / 13 | 2016-06-10 | 16 |
| Q2 FY2017 | 2016-07-31 | 2016-08-11 / 2016-08-11 | [0001045810-16-000292](https://www.sec.gov/Archives/edgar/data/1045810/000104581016000292/form8-kq2fy17.htm) | 10-Q | 2016-08-23 (08-23 17:20 ET) | [0001045810-16-000300](https://www.sec.gov/Archives/edgar/data/1045810/000104581016000300/nvda2017q210q.htm) | 12 / 12 | 2016-09-09 | 17 |
| Q3 FY2017 | 2016-10-30 | 2016-11-10 / 2016-11-10 | [0001045810-16-000343](https://www.sec.gov/Archives/edgar/data/1045810/000104581016000343/form8-kq3fy17.htm) | 10-Q | 2016-11-22 (11-22 16:29 ET) | [0001045810-16-000353](https://www.sec.gov/Archives/edgar/data/1045810/000104581016000353/nvda2017q310q.htm) | 12 / 12 | 2016-12-09 | 17 |
| Q4 FY2017 | 2017-01-29 | 2017-02-09 / 2017-02-09 | [0001045810-17-000016](https://www.sec.gov/Archives/edgar/data/1045810/000104581017000016/form8-kq4fy17.htm) | 10-K | 2017-03-01 (03-01 17:30 ET) | [0001045810-17-000027](https://www.sec.gov/Archives/edgar/data/1045810/000104581017000027/nvda-2017x10k.htm) | 20 / 20 | 2017-03-30 | 29 |
| Q1 FY2018 | 2017-04-30 | 2017-05-09 / 2017-05-09 | [0001045810-17-000068](https://www.sec.gov/Archives/edgar/data/1045810/000104581017000068/form8-kq1fy18.htm) | 10-Q | 2017-05-23 (05-23 16:34 ET) | [0001045810-17-000075](https://www.sec.gov/Archives/edgar/data/1045810/000104581017000075/nvda2018q110q.htm) | 14 / 14 | 2017-06-09 | 17 |
| Q2 FY2018 | 2017-07-30 | 2017-08-10 / 2017-08-10 | [0001045810-17-000117](https://www.sec.gov/Archives/edgar/data/1045810/000104581017000117/form8-kq2fy18.htm) | 10-Q | 2017-08-23 (08-23 16:24 ET) | [0001045810-17-000123](https://www.sec.gov/Archives/edgar/data/1045810/000104581017000123/nvda2018q210q.htm) | 13 / 13 | 2017-09-08 | 16 |
| Q3 FY2018 | 2017-10-29 | 2017-11-06 / 2017-11-09 | [0001045810-17-000164](https://www.sec.gov/Archives/edgar/data/1045810/000104581017000164/form8-kq3fy18.htm) | 10-Q | 2017-11-21 (11-21 16:25 ET) | [0001045810-17-000172](https://www.sec.gov/Archives/edgar/data/1045810/000104581017000172/nvda2018q310q.htm) | 12 / 12 | 2017-12-08 | 17 |
| Q4 FY2018 | 2018-01-28 | 2018-02-08 / 2018-02-08 | [0001045810-18-000004](https://www.sec.gov/Archives/edgar/data/1045810/000104581018000004/form8-kq4fy18.htm) | 10-K | 2018-02-28 (02-28 16:31 ET) | [0001045810-18-000010](https://www.sec.gov/Archives/edgar/data/1045810/000104581018000010/nvda-2018x10k.htm) | 20 / 20 | 2018-03-29 | 29 |
| Q1 FY2019 | 2018-04-29 | 2018-05-10 / 2018-05-10 | [0001045810-18-000052](https://www.sec.gov/Archives/edgar/data/1045810/000104581018000052/form8-kq1fy19.htm) | 10-Q | 2018-05-22 (05-22 16:35 ET) | [0001045810-18-000080](https://www.sec.gov/Archives/edgar/data/1045810/000104581018000080/nvda2019q110q.htm) | 12 / 12 | 2018-06-08 | 17 |
| Q2 FY2019 | 2018-07-29 | 2018-08-16 / 2018-08-16 | [0001045810-18-000113](https://www.sec.gov/Archives/edgar/data/1045810/000104581018000113/form8-kq2fy19.htm) | 10-Q | 2018-08-16 (08-16 16:31 ET) | [0001045810-18-000114](https://www.sec.gov/Archives/edgar/data/1045810/000104581018000114/nvda2019q210q.htm) | 0 / 0 | 2018-09-07 | 22 |
| Q3 FY2019 | 2018-10-28 | 2018-11-15 / 2018-11-15 | [0001045810-18-000148](https://www.sec.gov/Archives/edgar/data/1045810/000104581018000148/form8-kq3fy19.htm) | 10-Q | 2018-11-15 (11-15 16:32 ET) | [0001045810-18-000150](https://www.sec.gov/Archives/edgar/data/1045810/000104581018000150/nvda2019q310q.htm) | 0 / 0 | 2018-12-07 | 22 |
| Q4 FY2019 | 2019-01-27 | 2019-02-14 / 2019-02-14 | [0001045810-19-000007](https://www.sec.gov/Archives/edgar/data/1045810/000104581019000007/form8-kq4fy19.htm) | 10-K | 2019-02-21 (02-21 16:37 ET) | [0001045810-19-000023](https://www.sec.gov/Archives/edgar/data/1045810/000104581019000023/nvda-2019x10k.htm) | 7 / 7 | 2019-03-28 | 35 |
| Q1 FY2020 | 2019-04-28 | 2019-05-16 / 2019-05-16 | [0001045810-19-000077](https://www.sec.gov/Archives/edgar/data/1045810/000104581019000077/form8-kq1fy20.htm) | 10-Q | 2019-05-16 (05-16 16:36 ET) | [0001045810-19-000079](https://www.sec.gov/Archives/edgar/data/1045810/000104581019000079/nvda2020q110q.htm) | 0 / 0 | 2019-06-07 | 22 |
| Q2 FY2020 | 2019-07-28 | 2019-08-15 / 2019-08-15 | [0001045810-19-000140](https://www.sec.gov/Archives/edgar/data/1045810/000104581019000140/form8-kq2fy20.htm) | 10-Q | 2019-08-15 (08-15 17:20 ET) | [0001045810-19-000144](https://www.sec.gov/Archives/edgar/data/1045810/000104581019000144/nvda2020q210q.htm) | 0 / 0 | 2019-09-06 | 22 |
| Q3 FY2020 | 2019-10-27 | 2019-11-14 / 2019-11-14 | [0001045810-19-000168](https://www.sec.gov/Archives/edgar/data/1045810/000104581019000168/form8-kq3fy20.htm) | 10-Q | 2019-11-14 (11-14 16:36 ET) | [0001045810-19-000170](https://www.sec.gov/Archives/edgar/data/1045810/000104581019000170/nvda2020q310q.htm) | 0 / 0 | 2019-12-06 | 22 |
| Q4 FY2020 | 2020-01-26 | 2020-02-13 / 2020-02-13 | [0001045810-20-000007](https://www.sec.gov/Archives/edgar/data/1045810/000104581020000007/form8-kq4fy20.htm) | 10-K | 2020-02-20 (02-20 16:38 ET) | [0001045810-20-000010](https://www.sec.gov/Archives/edgar/data/1045810/000104581020000010/nvda-2020x10k.htm) | 7 / 7 | 2020-03-26 | 35 |
| Q1 FY2021 | 2020-04-26 | 2020-05-21 / 2020-05-21 | [0001045810-20-000063](https://www.sec.gov/Archives/edgar/data/1045810/000104581020000063/nvda-20200521.htm) | 10-Q | 2020-05-21 (05-21 16:32 ET) | [0001045810-20-000065](https://www.sec.gov/Archives/edgar/data/1045810/000104581020000065/nvda-20200426.htm) | 0 / 0 | 2020-06-05 | 15 |
| Q2 FY2021 | 2020-07-26 | 2020-08-19 / 2020-08-19 | [0001045810-20-000145](https://www.sec.gov/Archives/edgar/data/1045810/000104581020000145/nvda-20200819.htm) | 10-Q | 2020-08-19 (08-19 16:36 ET) | [0001045810-20-000147](https://www.sec.gov/Archives/edgar/data/1045810/000104581020000147/nvda-20200726.htm) | 0 / 0 | 2020-09-04 | 16 |
| Q3 FY2021 | 2020-10-25 | 2020-11-18 / 2020-11-18 | [0001045810-20-000187](https://www.sec.gov/Archives/edgar/data/1045810/000104581020000187/nvda-20201118.htm) | 10-Q | 2020-11-18 (11-18 16:35 ET) | [0001045810-20-000189](https://www.sec.gov/Archives/edgar/data/1045810/000104581020000189/nvda-20201025.htm) | 0 / 0 | 2020-12-04 | 16 |
| Q4 FY2021 | 2021-01-31 | 2021-02-24 / 2021-02-24 | [0001045810-21-000007](https://www.sec.gov/Archives/edgar/data/1045810/000104581021000007/nvda-20210224.htm) | 10-K | 2021-02-26 (02-26 17:03 ET) | [0001045810-21-000010](https://www.sec.gov/Archives/edgar/data/1045810/000104581021000010/nvda-20210131.htm) | 2 / 2 | 2021-04-01 | 34 |
| Q1 FY2022 | 2021-05-02 | 2021-05-26 / 2021-05-26 | [0001045810-21-000063](https://www.sec.gov/Archives/edgar/data/1045810/000104581021000063/nvda-20210526.htm) | 10-Q | 2021-05-26 (05-26 16:35 ET) | [0001045810-21-000064](https://www.sec.gov/Archives/edgar/data/1045810/000104581021000064/nvda-20210502.htm) | 0 / 0 | 2021-06-11 | 16 |
| Q2 FY2022 | 2021-08-01 | 2021-08-18 / 2021-08-18 | [0001045810-21-000128](https://www.sec.gov/Archives/edgar/data/1045810/000104581021000128/nvda-20210818.htm) | 10-Q | 2021-08-20 (08-20 16:32 ET) | [0001045810-21-000131](https://www.sec.gov/Archives/edgar/data/1045810/000104581021000131/nvda-20210801.htm) | 2 / 2 | 2021-09-10 | 21 |
| Q3 FY2022 | 2021-10-31 | 2021-11-17 / 2021-11-17 | [0001045810-21-000160](https://www.sec.gov/Archives/edgar/data/1045810/000104581021000160/nvda-20211117.htm) | 10-Q | 2021-11-22 (11-19 21:16 ET) | [0001045810-21-000163](https://www.sec.gov/Archives/edgar/data/1045810/000104581021000163/nvda-20211031.htm) | 5 / 2 | 2021-12-10 | 18 |
| Q4 FY2022 | 2022-01-30 | 2022-02-16 / 2022-02-16 | [0001045810-22-000008](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000008/nvda-20220216.htm) | 10-K | 2022-03-18 (03-17 20:33 ET) | [0001045810-22-000036](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000036/nvda-20220130.htm) | 30 / 29 | 2022-03-31 | 13 |
| Q1 FY2023 | 2022-05-01 | 2022-05-25 / 2022-05-25 | [0001045810-22-000073](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000073/nvda-20220525.htm) | 10-Q | 2022-05-27 (05-27 16:21 ET) | [0001045810-22-000079](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000079/nvda-20220501.htm) | 2 / 2 | 2022-06-10 | 14 |
| Q2 FY2023 | 2022-07-31 | 2022-08-24 / 2022-08-24 | [0001045810-22-000136](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000136/nvda-20220824.htm) | 10-Q | 2022-08-31 (08-31 17:01 ET) | [0001045810-22-000147](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000147/nvda-20220731.htm) | 7 / 7 | 2022-09-09 | 9 |
| Q3 FY2023 | 2022-10-30 | 2022-11-16 / 2022-11-16 | [0001045810-22-000163](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000163/nvda-20221116.htm) | 10-Q | 2022-11-18 (11-18 16:35 ET) | [0001045810-22-000166](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000166/nvda-20221030.htm) | 2 / 2 | 2022-12-09 | 21 |
| Q4 FY2023 | 2023-01-29 | 2023-02-22 / 2023-02-22 | [0001045810-23-000014](https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/nvda-20230222.htm) | 10-K | 2023-02-24 (02-24 17:23 ET) | [0001045810-23-000017](https://www.sec.gov/Archives/edgar/data/1045810/000104581023000017/nvda-20230129.htm) | 2 / 2 | 2023-03-30 | 34 |
| Q1 FY2024 | 2023-04-30 | 2023-05-24 / 2023-05-24 | [0001045810-23-000087](https://www.sec.gov/Archives/edgar/data/1045810/000104581023000087/nvda-20230524.htm) | 10-Q | 2023-05-26 (05-26 16:17 ET) | [0001045810-23-000093](https://www.sec.gov/Archives/edgar/data/1045810/000104581023000093/nvda-20230430.htm) | 2 / 2 | 2023-06-09 | 14 |
| Q2 FY2024 | 2023-07-30 | 2023-08-23 / 2023-08-23 | [0001045810-23-000171](https://www.sec.gov/Archives/edgar/data/1045810/000104581023000171/nvda-20230823.htm) | 10-Q | 2023-08-28 (08-25 19:36 ET) | [0001045810-23-000175](https://www.sec.gov/Archives/edgar/data/1045810/000104581023000175/nvda-20230730.htm) | 5 / 2 | 2023-09-08 | 11 |
| Q3 FY2024 | 2023-10-29 | 2023-11-21 / 2023-11-21 | [0001045810-23-000225](https://www.sec.gov/Archives/edgar/data/1045810/000104581023000225/nvda-20231121.htm) | 10-Q | 2023-11-21 (11-21 16:36 ET) | [0001045810-23-000227](https://www.sec.gov/Archives/edgar/data/1045810/000104581023000227/nvda-20231029.htm) | 0 / 0 | 2023-12-08 | 17 |
| Q4 FY2024 | 2024-01-28 | 2024-02-21 / 2024-02-21 | [0001045810-24-000028](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000028/nvda-20240221.htm) | 10-K | 2024-02-21 (02-21 16:36 ET) | [0001045810-24-000029](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm) | 0 / 0 | 2024-03-28 | 36 |
| Q1 FY2025 | 2024-04-28 | 2024-05-22 / 2024-05-22 | [0001045810-24-000113](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000113/nvda-20240522.htm) | 10-Q | 2024-05-29 (05-29 16:36 ET) | [0001045810-24-000124](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000124/nvda-20240428.htm) | 7 / 7 | 2024-06-07 | 9 |
| Q2 FY2025 | 2024-07-28 | 2024-08-28 / 2024-08-28 | [0001045810-24-000262](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000262/nvda-20240828.htm) | 10-Q | 2024-08-28 (08-28 17:05 ET) | [0001045810-24-000264](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000264/nvda-20240728.htm) | 0 / 0 | 2024-09-06 | 9 |
| Q3 FY2025 | 2024-10-27 | 2024-11-20 / 2024-11-20 | [0001045810-24-000315](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000315/nvda-20241120.htm) | 10-Q | 2024-11-20 (11-20 16:31 ET) | [0001045810-24-000316](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000316/nvda-20241027.htm) | 0 / 0 | 2024-12-06 | 16 |
| Q4 FY2025 | 2025-01-26 | 2025-02-26 / 2025-02-26 | [0001045810-25-000021](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000021/nvda-20250226.htm) | 10-K | 2025-02-26 (02-26 16:48 ET) | [0001045810-25-000023](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm) | 0 / 0 | 2025-03-27 | 29 |
| Q1 FY2026 | 2025-04-27 | 2025-05-28 / 2025-05-28 | [0001045810-25-000115](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000115/nvda-20250528.htm) | 10-Q | 2025-05-28 (05-28 16:32 ET) | [0001045810-25-000116](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000116/nvda-20250427.htm) | 0 / 0 | 2025-06-06 | 9 |
| Q2 FY2026 | 2025-07-27 | 2025-08-27 / 2025-08-27 | [0001045810-25-000207](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000207/nvda-20250827.htm) | 10-Q | 2025-08-27 (08-27 16:52 ET) | [0001045810-25-000209](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000209/nvda-20250727.htm) | 0 / 0 | 2025-09-05 | 9 |
| Q3 FY2026 | 2025-10-26 | 2025-11-19 / 2025-11-19 | [0001045810-25-000228](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000228/nvda-20251119.htm) | 10-Q | 2025-11-19 (11-19 16:36 ET) | [0001045810-25-000230](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm) | 0 / 0 | 2025-12-05 | 16 |
| Q4 FY2026 | 2026-01-25 | 2026-02-25 / 2026-02-25 | [0001045810-26-000019](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/nvda-20260225.htm) | 10-K | 2026-02-25 (02-25 16:42 ET) | [0001045810-26-000021](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm) | 0 / 0 | 2026-03-26 | 29 |
| Q1 FY2027 | 2026-04-26 | 2026-05-20 / 2026-05-20 | [0001045810-26-000051](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/nvda-20260520.htm) | 10-Q | 2026-05-20 (05-20 16:35 ET) | [0001045810-26-000052](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm) | 0 / 0 | 2026-06-05 | 16 |
| Q2 FY2027 | 2026-07-26 | 2026-08-26 / 2026-08-26 | [0001045810-26-000073](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/nvda-20260826.htm) | 10-Q | 2026-08-26 (08-26 16:36 ET) | [0001045810-26-000075](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) | 0 / 0 | 2026-09-04 | 9 |
| Q3 FY2027 | 2026-10-25 | 2026-11-17 / 2026-11-17 | [0001045810-26-000088](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/nvda-20261117.htm) | 10-Q | NOT FILED as of 2026-11-22 | — | open: 5 days elapsed at 2026-11-22 / open | 2026-12-04 | n/a (12 days remain at 2026-11-22) |

Notes on individual rows:

- Q3 FY2018: the 8-K report date (2017-11-06) precedes its filing date (2017-11-09) because the same 8-K also carried Item 1.02; the earnings release date is the filing date. [FILING/ON-RECORD]
- Q4 FY2019 and Q2 FY2023 each have an earlier Item 2.02 8-K in the same quarter (a pre-announcement): 2019-01-28 ([0001045810-19-000004](https://www.sec.gov/Archives/edgar/data/1045810/000104581019000004/form8-kq4fy19update.htm)) and 2022-08-08 (0001045810-22-000133). The table uses the full results release. [FILING/ON-RECORD]
- Q3 FY2027 period end (October 25, 2026) is from the press release filed as EX-99.1 to the November 17, 2026 8-K: "third quarter ended October 25, 2026". [FILING/ON-RECORD] — [Nvidia 8-K EX-99.1, SEC EDGAR, 2026-11-17](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/q3fy27pr.htm)

**Pattern, computed from the table:**

- Q1 FY2017 to Q1 FY2019 (7 quarterly reports): the 10-Q was filed 12 to 14 days after earnings, every time. The two 10-Ks in that span were filed 20 days after earnings. [FILING/ON-RECORD] — [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json)
- Same-day filing began with Q2 FY2019 (earnings and 10-Q both on 2018-08-16). Since then Nvidia has filed 25 10-Qs: 17 the same day as earnings and 8 later (see section 2). [FILING/ON-RECORD] — [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json)
- The largest 10-Q gap since August 2018 is 7 days (Q2 FY2023 and Q1 FY2025). [FILING/ON-RECORD] — [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json)
- 10-Ks since FY2019: gaps of 7, 7, 2, 30, 2, 0, 0, 0 days (FY2019 through FY2026). [FILING/ON-RECORD] — [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json)
- The nine periodic reports before this one (Q2 FY2025 through Q2 FY2027, i.e. August 2024 to August 2026, seven 10-Qs and two 10-Ks) were all filed the same day as earnings, roughly 10 to 45 minutes after the 8-K was accepted. This matches the "9 same-day filings" headline that appeared in one search result. [FILING/ON-RECORD] — [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json); headline only, article not retrieved: [FourWeekMBA, date not retrieved](https://fourweekmba.com/ai-nvidia-holds-its-10-q-after-9-same-day-filings-due-dec-4/) [UNVERIFIED]
- Longer history (FY2004 to FY2016, same feed, not in the CSV): 10-Qs were filed 8 to 26 days after earnings and 10-Ks 27 to 46 days after. The last 10-Q gap above 15 days was Q3 FY2011 (earnings 8-K 2010-11-12, 10-Q 2010-12-07, 25 days). [FILING/ON-RECORD] — [EDGAR older-filings feed](https://data.sec.gov/submissions/CIK0001045810-submissions-001.json)
- As of 2026-11-22 the EDGAR feed shows only three Nvidia-CIK filings after November 12: a 13F-HR (Nov 16), the earnings 8-K (Nov 17) and a Form 144 (Nov 19). No 10-Q, no NT 10-Q. [FILING/ON-RECORD] — [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json)

### Inferences
- "Nvidia always files its 10-Q with earnings" overstates the record. The accurate statement is: same-day for the last nine periodic reports and for 17 of 25 10-Qs since August 2018; before that, about two weeks later as a matter of routine.
- What is unprecedented in the EDGAR record is not the gap itself (5 days so far) but that Nvidia announced in advance, in an SEC-furnished exhibit, that the 10-Q would come "in the coming weeks", and furnished a new supplemental exhibit to bridge the gap (section 5).
- If the 10-Q arrives on the December 4 deadline, the gap would be 17 days: the longest since December 2010, but shorter than gaps that were routine for Nvidia before 2011.

### Gaps
- Period-end dates in the table are the EDGAR `reportDate` field, not re-read from each cover page. For 2007 to 2008 that field is unreliable (it equals the filing date), which is why the CSV starts at FY2017 where the field is clean.
- Federal holidays are not modelled in the deadline column; none of the FY2017 to FY2027 deadlines shown falls on one that I am aware of, but this was not checked against a holiday calendar.

---

## 2. Earlier instances where the periodic report came after earnings, and what was going on

### Takeaway
Since same-day filing began, the only multi-day 10-Q gaps with an identifiable cause in the filings are August 2022 (the 10-Q was accepted 73 seconds after an 8-K disclosing a new US export licence requirement) and, for the 10-K, March 2022 (after the Arm deal collapsed). Most other gaps are a plain two-day lag that was Nvidia's norm from August 2021 to August 2023. Nvidia's two genuine late filings, in 2002 and 2006, both involved an audit committee review, an SEC inquiry and a restatement.

### Cited Findings

**Non-same-day periodic reports since August 2018** (all dates [FILING/ON-RECORD] from the [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json)):

| Period | Earnings | Periodic report | Gap | Context found in filings |
|---|---|---|---|---|
| Q4 FY2019 (10-K) | 2019-02-14 | 2019-02-21 | 7 | A guidance-update 8-K (Item 2.02) was filed 2019-01-28; its exhibits were not retrieved. No stated reason for the 7 days. |
| Q4 FY2020 (10-K) | 2020-02-13 | 2020-02-20 | 7 | No stated reason. |
| Q4 FY2021 (10-K) | 2021-02-24 | 2021-02-26 | 2 | No stated reason. |
| Q2 FY2022 | 2021-08-18 | 2021-08-20 | 2 | No stated reason. Arm acquisition pending. |
| Q3 FY2022 | 2021-11-17 | 2021-11-22 | 5 (2 by acceptance) | Accepted Friday 2021-11-19 at 21:16 ET, so EDGAR dates it the next business day. |
| Q4 FY2022 (10-K) | 2022-02-16 | 2022-03-18 | 30 (29) | Longest gap in the table. Arm termination was announced 2022-02-08 (8-K Item 1.02). Still 13 days ahead of the March 31 deadline. |
| Q1 FY2023 | 2022-05-25 | 2022-05-27 | 2 | No stated reason. |
| Q2 FY2023 | 2022-08-24 | 2022-08-31 | 7 | Export licence 8-K accepted 17:00:22 ET; 10-Q accepted 17:01:35 ET the same day. |
| Q3 FY2023 | 2022-11-16 | 2022-11-18 | 2 | No stated reason. |
| Q4 FY2023 (10-K) | 2023-02-22 | 2023-02-24 | 2 | No stated reason. |
| Q1 FY2024 | 2023-05-24 | 2023-05-26 | 2 | No stated reason. |
| Q2 FY2024 | 2023-08-23 | 2023-08-28 | 5 (2) | Accepted Friday 2023-08-25 at 19:36 ET. |
| Q1 FY2025 | 2024-05-22 | 2024-05-29 | 7 | The earnings 8-K also carried Item 8.01. Content not retrieved; from memory this was the ten-for-one stock split [UNVERIFIED]. No stated reason for the gap. |

- August 2022: the 8-K says that on August 26, 2022 the US government informed Nvidia of "a new license requirement, effective immediately" covering "A100 and forthcoming H100 integrated circuits" for China (including Hong Kong) and Russia, and that the Q3 FY2023 outlook "included approximately $400 million in potential sales to China". [FILING/ON-RECORD] (pre-Nov 17) — [Nvidia 8-K, SEC EDGAR, filed 2022-08-31](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000146/nvda-20220826.htm)
- FY2022 10-K: says the parties terminated the Arm agreement "because of significant regulatory challenges preventing the completion of the transaction" and that Nvidia would record a $1.36 billion charge in Q1 FY2023, "reflecting the write-off of the prepayment provided at signing in September 2020". [FILING/ON-RECORD] (pre-Nov 17) — [Nvidia 10-K, SEC EDGAR, filed 2022-03-18](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000036/nvda-20220130.htm)

**Major events that did NOT delay the periodic report** (dates [FILING/ON-RECORD], same feed):

- Crypto-inventory quarter: Q3 FY2019 earnings and 10-Q both on 2018-11-15.
- Mellanox closing (8-K Item 2.01, 2020-04-27): Q1 FY2021 earnings and 10-Q both on 2020-05-21.
- Arm agreement (8-K Item 1.01, 2020-09-14): Q3 FY2021 earnings and 10-Q both on 2020-11-18.
- October 2023 export rules (8-Ks Item 8.01 on 2023-10-17 and 2023-10-24): Q3 FY2024 earnings and 10-Q both on 2023-11-21.
- April 2025 (8-K Item 8.01 filed 2025-04-15, report date 2025-04-09; content not retrieved, from memory the H20 licence requirement and charge [UNVERIFIED]): Q1 FY2026 earnings and 10-Q both on 2025-05-28.

**Amended periodic reports and non-reliance 8-Ks in Nvidia's full EDGAR history** (complete list from the feed, 1998 to 2026):

| Filed | Form | Period | What it was |
|---|---|---|---|
| 2001-05-25 | 10-K405/A | FY ended 2001-01-28 | Purpose not retrieved. |
| 2002-07-03 | 10-Q/A | Q ended 2002-04-28 | "filed solely to correct typographical errors"; "does not change any of the financial data presented". |
| 2004-05-20 | 10-K/A | FY ended 2004-01-25 | "filed solely to amend Part III, Item 10 through Item 14". No restatement. |
| 2006-11-06 | 8-K Item 4.02 | report date 2006-11-01 | Non-reliance on all financial statements "for periods commencing on or after January 31, 1999" (stock option measurement dates). The only Item 4.02 8-K Nvidia has ever filed. |
| 2006-11-29 | 10-K/A | FY ended 2006-01-29 | Restated for option grants. |
| 2006-11-29 | 10-Q/A | Q ended 2006-04-30 | Restated for option grants. |

Sources: [10-Q/A 2002](https://www.sec.gov/Archives/edgar/data/1045810/000101287002002921/d10qa.htm); [10-K/A 2004](https://www.sec.gov/Archives/edgar/data/1045810/000104581004000014/amendment10k.htm); [8-K Item 4.02, 2006](https://www.sec.gov/Archives/edgar/data/1045810/000119312506223958/d8k.htm). All [FILING/ON-RECORD] (pre-Nov 17), publisher SEC EDGAR.

- The 2002 restatement predates Item 4.02 (which took effect in August 2004), so it has no non-reliance 8-K; it was disclosed in the FY2002 10-K, which says earlier reports for the restated periods "should not be relied upon and are superceded". [FILING/ON-RECORD] (pre-Nov 17) — [Nvidia 10-K, SEC EDGAR, filed 2002-05-14](https://www.sec.gov/Archives/edgar/data/1045810/000101287002002262/d10k.htm)
- An 8-K filed 2004-04-26 carries old-format "Item 4". Under the pre-August-2004 numbering that is a change of certifying accountant, not non-reliance; the document itself was not opened. [UNVERIFIED as to content]
- No 10-Q/A or 10-K/A has been filed since November 2006. [FILING/ON-RECORD] — [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json)

### Inferences
- The August 2022 timestamps (8-K and 10-Q accepted 73 seconds apart) are the clearest evidence in the record that Nvidia has previously held a 10-Q for a few days to add disclosure about a late-breaking development, without missing the deadline and without any change to reported numbers. That is the closest in-house analogue to the explanation attributed to UBS for the current delay (section 5).
- The 30-day FY2022 10-K gap is plausibly related to the Arm termination, but the filing does not say so.

### Gaps
- No Nvidia filing states a reason for any of the 2-to-7-day gaps. The context column is coincidence in time, not a stated cause.
- Could not verify whether the February 2022 cybersecurity incident is discussed in the FY2022 10-K (the readable portion stopped before Risk Factors).
- The 2019-01-28 guidance-cut exhibits, the 2001 10-K405/A and the 2004-04-26 8-K were not opened.

---

## 3. NT 10-Q / NT 10-K check across Nvidia's full EDGAR history

### Takeaway
Nvidia has filed exactly two late-filing notifications in 28 years on EDGAR: an NT 10-K in April 2002 and an NT 10-Q in September 2006. Both were tied to audit committee reviews with SEC involvement and both ended in restatements. There is no NT 10-K/A, and nothing since 2006.

### Cited Findings
- Form-type count across all 2,494 Nvidia-CIK filings (1998-03-06 to 2026-11-19): NT 10-K = 1, NT 10-Q = 1, NT 10-K/A = 0, NT 10-Q/A = 0. [FILING/ON-RECORD] — [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json) and [older-filings feed](https://data.sec.gov/submissions/CIK0001045810-submissions-001.json)

**NT 10-K, filed 2002-04-29 (fiscal year ended January 27, 2002)** [FILING/ON-RECORD] (pre-Nov 17) — [Nvidia Form 12b-25, SEC EDGAR, 2002-04-29](https://www.sec.gov/Archives/edgar/data/1045810/000095016802001121/dnt10k.htm)

- Stated reason: "The Registrant is in the process of restating previously reported financial results for fiscal years 2000 and 2001, as well as the first, second and third quarters of fiscal year 2002."
- It committed to file "no later than the 15th calendar day following the prescribed due date". The 10-K was filed 2002-05-14, 15 days later, so it was within the extension.
- It answered yes to an anticipated significant change in results and attached a press release. Signed by Jen-Hsun Huang.
- Background from the 10-K: "The SEC staff informed us in January 2002 that it had concerns relating to certain accounting matters"; the Audit Committee review was assisted by "the law firm of Cooley Godward LLP" and "forensic auditors from the firm of KPMG LLP"; the SEC and the US Attorney's Office "had authorized a private investigation into such matters".
- Outcome: net income restated to $176.9 million from $177.1 million (FY2002), $98.5 million from $99.9 million (FY2001) and $41.0 million from $38.1 million (FY2000); a net increase of about $1.3 million over three years. Mary Dotz became interim CFO in April 2002. — [Nvidia 10-K, SEC EDGAR, 2002-05-14](https://www.sec.gov/Archives/edgar/data/1045810/000101287002002262/d10k.htm)

**NT 10-Q, filed 2006-09-11 (quarter ended July 30, 2006)** [FILING/ON-RECORD] (pre-Nov 17) — [Nvidia Form 12b-25, SEC EDGAR, 2006-09-11](https://www.sec.gov/Archives/edgar/data/1045810/000119312506188313/dnt10q.htm)

- Stated reason: the Audit Committee "is conducting a voluntary review of the Company's stock option practices covering the time from the Company's initial public offering in 1999 through the current fiscal year", had "reached a preliminary conclusion that incorrect measurement dates were used", and Nvidia "does not currently anticipate that it will be filed on or before the fifth calendar day following the prescribed due date".
- SEC involvement: "The Company has voluntarily contacted the Securities and Exchange Commission staff" and "the SEC recently requested that the Company provide them with certain information".
- Sequence, from the feed and the filings:
  - 2006-08-10: 8-K reports revenue only for the quarter and says Nvidia does not expect to file its 10-Q by the September 8 deadline or the September 13 extension. — [8-K, 2006-08-10](https://www.sec.gov/Archives/edgar/data/1045810/000104581006000027/q207pressrelease.htm)
  - 2006-09-11: NT 10-Q filed; Nasdaq Staff Determination letter received the same day under Marketplace Rule 4310(c)(14), "issued in accordance with NASDAQ procedures due to the delayed filing". Nvidia requested a hearing; shares stayed listed pending the panel. — [8-K Item 3.01, 2006-09-12](https://www.sec.gov/Archives/edgar/data/1045810/000119312506189092/d8k.htm)
  - 2006-11-06: Item 4.02 non-reliance 8-K; expected charge "less than $150 million for stock-based compensation expense, net of related tax effects"; "no concerns with respect to the integrity of current management". — [8-K Item 4.02, 2006-11-06](https://www.sec.gov/Archives/edgar/data/1045810/000119312506223958/d8k.htm)
  - 2006-11-29: delayed 10-Q filed with a 10-K/A and a 10-Q/A. That is 82 days after the September 8 deadline and 111 days after the revenue-only release.
- Outcome in the delayed 10-Q: charges of "$199.6 million on a pre-tax basis" ($127.4 million net of tax); the Committee found the errors "were not motivated by any intent to mislead investors"; "the SEC is continuing the inquiry of our historical stock option grant practices it began in late August 2006"; nine derivative suits were filed from September 29, 2006; the Nasdaq panel heard the appeal on October 19, 2006 and "The Panel's decision is still pending". — [Nvidia 10-Q, SEC EDGAR, 2006-11-29](https://www.sec.gov/Archives/edgar/data/1045810/000119312506243229/d10q.htm)

### Inferences
- On the key question in the brief (did the 2006 options review delay Nvidia's 10-Q?): yes, by 82 days, with an NT filing, a Nasdaq deficiency letter and a restatement. The next 10-Q (Q3 FY2007, filed 2006-12-07) was on time by one day.
- Both of Nvidia's own late-filing episodes share the current situation's ingredients (an independent board-level review plus regulator interest) but differ in one decisive way: in both, the accounting itself was under review. Nothing retrieved from EDGAR says that about November 2026.

### Gaps
- Final outcome of the 2006 SEC inquiry and the Nasdaq panel decision was not retrieved (the later 10-K was not opened).
- The NT 10-K's attached April 29, 2002 restatement press release was not read separately.

---

## 4. Deadline for the Q3 FY2027 10-Q, Form 12b-25, and consequences of missing it

### Takeaway
December 4, 2026 is correct: 40 days after October 25, 2026 is Friday, December 4, with no weekend or holiday roll. Missing it would require a Form 12b-25 by Monday, December 7 and would buy only until Wednesday, December 9; beyond that Nvidia would lose Form S-3 eligibility for roughly a year, draw a Nasdaq deficiency letter, and start a clock under its notes indenture. None of that applies yet.

### Cited Findings

**The deadline**

- Form 10-Q General Instruction A.1: a quarterly report "shall be filed within the following period after the end of each of the first three fiscal quarters": "40 days after the end of the fiscal quarter for large accelerated filers and accelerated filers". [FILING/ON-RECORD] (pre-Nov 17) — [SEC, Form 10-Q General Instructions, form dated 02-25](https://www.sec.gov/files/form10-q.pdf)
- Nvidia is a large accelerated filer: EDGAR's category field says "Large accelerated filer", and the Q2 FY2027 10-Q cover checks that box. [FILING/ON-RECORD] — [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json); [Nvidia 10-Q, 2026-08-26](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- Arithmetic (mine): October 25, 2026 + 40 days = December 4, 2026, a Friday. One year earlier the same calendar position gave December 5, 2025, and Nvidia filed 16 days ahead of it.
- Weekend/holiday rule: when a due date "falls on a Saturday, Sunday or holiday, the report will be considered timely filed" on the next business day (Rule 0-3). Not needed here. [FILING/ON-RECORD] (pre-Nov 17) — [SEC Division of Corporation Finance, Exchange Act Rules C&DI, Q135.03](https://www.sec.gov/rules-regulations/staff-guidance/compliance-disclosure-interpretations/exchange-act-rules)

**Form 12b-25 (NT 10-Q)**

- It must be "filed no later than one business day after the due date of the annual or quarterly report", and the report itself is then due "no later than fifteen or five calendar days, respectively, after the due date". For Nvidia: NT 10-Q by Monday, December 7; 10-Q by Wednesday, December 9 (my arithmetic). [FILING/ON-RECORD] (pre-Nov 17) — [Exchange Act Rules C&DI, Q135.03](https://www.sec.gov/rules-regulations/staff-guidance/compliance-disclosure-interpretations/exchange-act-rules)
- "a company must file a Form 12b-25 for a periodic report that is filed after the due date" (Q135.02), and "there are no additional extensions" (Q135.05). — same source
- The form's Part II(b) is the representation that the quarterly report "will be filed on or before the fifth calendar day following the prescribed due date". Part III requires the registrant to "State below in reasonable detail why" the report could not be filed on time. Part IV(3) asks whether "any significant change in results of operations from the corresponding period for the last fiscal year will be reflected" and, if so, for an explanation "both narratively and quantitatively". The form warns that "Intentional misstatements or omissions of fact constitute Federal Criminal Violations". [FILING/ON-RECORD] (pre-Nov 17) — [SEC, Form 12b-25, form dated 01-19](https://www.sec.gov/files/form12b-25.pdf)

**Form S-3 and WKSI**

- Form S-3 General Instruction I.A.3(b) requires that the registrant "has filed in a timely manner all reports required to be filed during the twelve calendar months and any portion of a month immediately preceding the filing of the registration statement". If Rule 12b-25(b) was used, the report must have "actually been filed within the time period prescribed by that rule". [FILING/ON-RECORD] (pre-Nov 17) — [SEC, Form S-3 General Instructions](https://www.sec.gov/files/forms-3.pdf)
- Staff example: a registrant late on a 10-Q due September 15, 2008 but timely afterwards "would first be eligible to use Form S-3 on October 1, 2009" (Q115.06). Eligibility is tested "each time it updates the registration statement under Section 10(a)(3)" (Q114.02), which in practice is the next 10-K (Q114.04). [FILING/ON-RECORD] (pre-Nov 17) — [SEC, Securities Act Forms C&DI](https://www.sec.gov/rules-regulations/staff-guidance/compliance-disclosure-interpretations/securities-act-forms)
- During a 12b-25 extension a company "would not be eligible to file a new registration statement on Form S-3 until the subject report is filed" (Q135.06). — [Exchange Act Rules C&DI](https://www.sec.gov/rules-regulations/staff-guidance/compliance-disclosure-interpretations/exchange-act-rules)
- Nvidia's current shelf is an automatic shelf (form type S-3ASR, File No. 333-287619, filed 2025-05-28). It was used in June 2026 for a $25.0 billion, seven-tranche notes offering. [FILING/ON-RECORD] (pre-Nov 17) — [EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json); [Nvidia 8-K, 2026-06-18](https://www.sec.gov/Archives/edgar/data/1045810/000119312526275783/d48176d8k.htm)
- WKSI status is evaluated "only upon specified events", such as filing a shelf or the next 10-K (Q161.01). [FILING/ON-RECORD] (pre-Nov 17) — [SEC, Securities Act Rules C&DI](https://www.sec.gov/rules-regulations/staff-guidance/compliance-disclosure-interpretations/securities-act-rules)

**Rule 144**

- The current-public-information condition must be met "at the time each sale is made" (Q131.01), and during a 12b-25 extension the issuer "may be deemed not current until it is filed" (Q131.02 / Q135.08). [FILING/ON-RECORD] (pre-Nov 17) — [Securities Act Rules C&DI](https://www.sec.gov/rules-regulations/staff-guidance/compliance-disclosure-interpretations/securities-act-rules)
- An Nvidia officer filed a Form 144 on November 19, 2026 (Timothy S. Teter, 30,000 shares, about $4.54 million, under a 10b5-1 plan adopted 2026-05-22). Insider sales under Rule 144 are continuing while the 10-Q is outstanding but not yet due. [FILING/ON-RECORD] — [Form 144, SEC EDGAR, 2026-11-19](https://www.sec.gov/Archives/edgar/data/1045810/000192109426001223/primary_doc.xml)

**Nasdaq** (Nasdaq's rulebook was unreachable; the process is taken from issuer 8-Ks that quote Nasdaq's letters)

- Super Micro, 2024: Nasdaq's letter cited Listing Rule 5250(c)(1); "the Company has 60 calendar days to regain compliance or to submit a plan to do so"; "NASDAQ could grant the Company an exception of up to 180 calendar days from the filing's due date"; the letter "has no immediate effect on the listing or trading". Super Micro's notice came 19 days after its due date. [FILING/ON-RECORD] (pre-Nov 17) — [Super Micro 8-K Item 3.01, SEC EDGAR, 2024-09-20](https://www.sec.gov/Archives/edgar/data/1375365/000137536524000033/smci-20240917.htm)
- Nvidia's own 2006 letter arrived on the day it filed its NT 10-Q, three days after the due date, under the predecessor rule. — [Nvidia 8-K, 2006-09-12](https://www.sec.gov/Archives/edgar/data/1045810/000119312506189092/d8k.htm)

**Debt**

- Nvidia's notes are issued under a Base Indenture dated September 16, 2016 (trustee now Computershare Trust Company, N.A., as successor to Wells Fargo). [FILING/ON-RECORD] (pre-Nov 17) — [Nvidia 8-K, 2026-06-18](https://www.sec.gov/Archives/edgar/data/1045810/000119312526275783/d48176d8k.htm)
- Reporting covenant, Section 4.2 ("Reports by the Issuer"): the issuer must file with the trustee, "within 15 days after the Issuer is required to file the same with the Commission", copies of its Exchange Act reports. "Delivery of such reports, information and documents to the Trustee is for informational purposes only."
- Events of Default, Section 5.1(c): a covenant breach becomes an Event of Default only if it continues "for a period of 90 days after the date on which written notice specifying such failure" is given by the trustee or "the holders of at least 25% in aggregate principal amount of the Outstanding Securities" of the series. No "additional interest as sole remedy" clause was found in the readable portion. [FILING/ON-RECORD] (pre-Nov 17) — [Base Indenture, EX-4.1 to Nvidia 8-K, SEC EDGAR, 2016-09-16](https://www.sec.gov/Archives/edgar/data/1045810/000119312516711700/d260668dex41.htm)
- Size of what sits under that indenture: debt carrying amount $33,366 million at July 26, 2026, including the June 2026 $25.0 billion issue. "As of July 26, 2026, we complied with the required covenants under the outstanding notes." Commercial paper: "our commercial paper program had a capacity of $25.0 billion, with no amounts outstanding." [FILING/ON-RECORD] (pre-Nov 17) — [Nvidia 10-Q, SEC EDGAR, 2026-08-26](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)

### Inferences
- The December 4 date carries real weight for Nvidia specifically because it is an active shelf issuer: it sold $25 billion of notes off an automatic shelf five months ago. A single untimely 10-Q would cost S-3 (and with it automatic-shelf) eligibility for about twelve months, tested at the latest when the FY2027 10-K is filed (around March 2027).
- Read literally, the indenture clock would be: missed SEC deadline, then 15 days to deliver to the trustee, then a notice from the trustee or 25% of a series, then 90 days to cure. That is at least three and a half months from December 4 before an Event of Default could exist, and it needs holders to act. This is my reading of extracted text, not a legal opinion; whether a 12b-25 extension moves the "required to file" date under the indenture was not determined.
- With no commercial paper outstanding at July 26, 2026, a short delay does not obviously create a funding problem. A delinquent filer typically cannot issue new registered debt and may find CP dealers unwilling to place paper, but I found no document saying this about Nvidia.

### Gaps
- The text of Rule 12b-25, Rule 0-3, Rule 144(c), Rule 405 ("ineligible issuer") and Nasdaq Rules 5250(c)(1) / 5810 was not retrieved directly (eCFR, Cornell LII and Nasdaq hosts were unreachable). The points above rest on SEC staff C&DIs, SEC form instructions and issuer 8-Ks. The statement in the brief that a report filed within the 12b-25 window is deemed timely is supported by the Form S-3 instruction quoted above but the rule sentence itself was not retrieved.
- Whether the June 2026 officers' certificate modified the reporting covenant for the new notes: not checked.
- Whether Nvidia has a revolving credit facility and what its reporting covenant says: not found. The only credit-agreement 8-K on EDGAR is from October 2016; the readable part of the latest 10-Q does not mention a revolver.
- Section 13(a) enforcement exposure (SEC actions against delinquent filers, Section 12(j) proceedings): no source retrieved. General knowledge only, so not stated as a finding.
- Whether guarantee or lease documents (for example the SB Energy residual value guaranties) contain their own reporting covenants: the forms were to be filed as exhibits to the Q2 FY2027 10-Q and were not opened.

---

## 5. What Nvidia said on November 17, 2026, and what UBS and others reportedly said

### Takeaway
Nvidia's on-record statement is one sentence in the CFO commentary: "We plan to file our 10-Q in the coming weeks." No reason is given anywhere in the 8-K or its exhibits. The same exhibits newly list, as a forward-looking-statement item, "the ongoing investigation by an independent committee of NVIDIA's board of directors", which is the only investigation Nvidia has confirmed in an SEC filing. The UBS explanation and the SEC probe are known to me only through search-result summaries.

### Cited Findings

**On the record (Nvidia's November 17, 2026 8-K, accession 0001045810-26-000088, accepted 16:20:51 ET)**

- The 8-K body (Items 2.02 and 9.01) says nothing about the 10-Q, an investigation, auditors or a review. It identifies the commentary as by "Colette M. Kress, Interim CEO and CFO". [FILING/ON-RECORD] — [Nvidia 8-K, SEC EDGAR, 2026-11-17](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/nvda-20261117.htm)
- CFO commentary (EX-99.2), in the introduction before the "Revenue" heading: "We plan to file our 10-Q in the coming weeks." The next sentence: "In the interim, we have provided a supplemental document with additional financial information on our investor website." No reason is stated. [FILING/ON-RECORD] — [EX-99.2, SEC EDGAR, 2026-11-17](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/q3fy27cfocommentary.htm)
- The forward-looking statements in EX-99.1 and EX-99.2 include, among the listed items:
  - "expectations with respect to NVIDIA's Form 10-Q for the third quarter of fiscal 2027"
  - "expectations with respect to the ongoing investigation by an independent committee of NVIDIA's board of directors" (EX-99.2 adds "and related matters")
  - "expectations with respect to litigation, government and regulatory inquiries and other actions or proceedings"
  - "expectations with respect to NVIDIA's leadership transition and the search for a new chief executive officer"
  - and, among risk factors, "the scope, timing and outcome of investigations, litigation and government and regulatory actions and proceedings".
  [FILING/ON-RECORD] — [EX-99.1, SEC EDGAR, 2026-11-17](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/q3fy27pr.htm)
- None of that language was in the prior quarter's CFO commentary, which had no 10-Q timing sentence and no clause about an independent committee, leadership transition, inquiries or investigations. [FILING/ON-RECORD] (pre-Nov 17) — [Q2 FY2027 CFO commentary, SEC EDGAR, 2026-08-26](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- A new exhibit, EX-99.3 "NVIDIA Corporation Supplemental Financial Information For the Quarter Ended October 25, 2026", was furnished. It states "All financial information and data contained herein is unaudited" and contains condensed income statement, balance sheet and cash flow statement, plus cash equivalents and marketable securities, a roll-forward of non-marketable securities, inventory detail, revenue by customer headquarters location, and customer concentration. It has no section on commitments, guarantees or legal proceedings, and does not say why it is being provided. [FILING/ON-RECORD] — [EX-99.3, SEC EDGAR, 2026-11-17](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/supplementalfinancialinfor.htm)
- The August 26, 2026 earnings 8-K listed only Exhibits 99.1, 99.2 and 104, so EX-99.3 is new this quarter. [FILING/ON-RECORD] (pre-Nov 17) — [Nvidia 8-K, SEC EDGAR, 2026-08-26](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/nvda-20260826.htm)
- Results were reported in full, not as preliminary or partial figures: revenue $115.8 billion (up 103% year on year), GAAP gross margin 74.8%, GAAP diluted EPS $2.70, Q4 revenue outlook $130.0 billion plus or minus 3%. The words "preliminary", "audit committee", "auditor", "review" and "subpoena" do not appear in EX-99.1 or EX-99.2. [FILING/ON-RECORD] — [EX-99.1](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/q3fy27pr.htm); [EX-99.2](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/q3fy27cfocommentary.htm)
- The CFO commentary discloses some items a 10-Q would normally carry: inventory $39.7 billion; supply commitments $390 billion (up from $279 billion); maximum gross guarantee exposure $118.0 billion including $105.0 billion of SB Energy credit support; a $1.0 billion net loss on non-marketable equity securities including a $1.8 billion impairment. [FILING/ON-RECORD] — [EX-99.2](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/q3fy27cfocommentary.htm)

**Reported, from search-tool summaries only (article text NOT retrieved; publication dates not retrieved; treat as leads)**

- UBS analyst Timothy Arcuri "wrote that management indicated this was related to the ongoing investigation and whether any additional risk factors would need to be added to the filing"; he kept a Buy rating and cut his price target to $220 from $240. [ANALYST ESTIMATE, second-hand] — search summary citing [TechCrunch](https://techcrunch.com/?p=3190087) and [AI Chat Daily, "Nvidia delays 10-Q filing, weighs new risk disclosures"](https://www.aichatdaily.com/ai-business/nvidia-delays-10-q-filing-weighs-new-risk-disclosures)
- Kress reportedly said on the earnings call that Nvidia would not immediately file the 10-Q; Nvidia "has not said on the record why" beyond that. [UNVERIFIED] — search summary citing [TechCrunch](https://techcrunch.com/?p=3190087); see also [Longbridge, "Why Nvidia broke with its usual practice in holding back its quarterly SEC report"](https://longbridge.com/news/305948432)
- The Wall Street Journal reportedly reported, citing people familiar with the matter, that the SEC opened a civil probe into whether Nvidia's disclosures misled investors, with questions centred on Asia. [ANONYMOUSLY SOURCED, third-hand] — search summary citing [InvestmentNews, "Embattled Nvidia faces SEC probe as California attorney general eyes action"](https://www.investmentnews.com/equities/embattled-nvidia-faces-sec-probe-as-california-attorney-general-eyes-action/269054); related headline [Crowdfund Insider, "SEC Opens Inquiry into Nvidia's Disclosures Following Jensen Huang's Exit"](https://www.crowdfundinsider.com/?p=323680)
- The search summaries describe the board investigation as concerning Jensen Huang's personal conduct, including a relationship with an executive of Nvidia partner Megaspeed, and mention a separate Justice and Commerce Department investigation into Megaspeed over export controls and a board "national security and export control oversight committee". The summaries themselves flagged that outlets disagree on how these threads connect. [UNVERIFIED] — search summaries citing [TechCrunch](https://techcrunch.com/?p=3190087) and [Longbridge](https://longbridge.com/news/305948432)
- Other headlines returned, not opened: [TheStreet Pro, "Nvidia delivers the numbers but the SEC adds a new question"](https://pro.thestreet.com/market-commentary/nvidia-delivers-the-numbers-but-the-sec-adds-a-new-question); [Digital Today, "Nvidia delays quarterly report filing, sparking Wall Street focus on risk disclosures"](https://www.digitaltoday.co.kr/en/view/127763/nvidia-delays-quarterly-report-filing-sparking-wall-street-focus-on-risk-disclosures). [UNVERIFIED]
- Transcripts of the November 17 call exist at [Nasdaq.com](https://www.nasdaq.com/articles/nvidia-nvda-q3-2027-earnings-call-transcript) but could not be opened. [UNVERIFIED]

### Inferences
- **The lead needs one correction.** The brief says UBS tied the delay to an SEC investigation. As summarised, Arcuri referred to "the ongoing investigation" and to whether "additional risk factors" are needed. The only "ongoing investigation" Nvidia names in its own filing is the one by an independent committee of its board. The SEC probe is a separate, anonymously sourced press report that no Nvidia filing confirms. Until the UBS note is read directly, the safer wording is "the ongoing investigation (which Nvidia's filing identifies as an independent board committee investigation)".
- The shape of the disclosure fits a "disclosure text, not numbers" explanation: full GAAP statements were released, extra balance-sheet detail was furnished as EX-99.3, and what is missing is exactly the 10-Q-only content (risk factors, legal proceedings, contingencies note, controls conclusion and officer certifications). That is consistent with the UBS-attributed reason and with Nvidia's own August 2022 behaviour, but it is an inference.
- Structural facts on EDGAR that could each slow a 10-Q, none of them cited by Nvidia:
  - Kress became interim CEO on November 11, six days before earnings, and must now sign the certifications as both principal executive and principal financial officer.
  - The independent committee's investigation was ongoing as of November 17.
  - The principal accounting officer changed on May 4, 2026 (section 6).
- The alternative explanations floated in the brief (routine caution during a CEO transition; PwC completing additional procedures; new disclosures being drafted) could not be tested. Nothing retrieved mentions the auditor at all.

### Gaps
- **The UBS note, the earnings-call transcript, and every news article were unreadable from this session.** The exact Arcuri wording, the date of his note, whether "management indicated" refers to a call-back or the public call, and any other analysts' explanations are unverified.
- The WSJ report on the SEC probe was not retrieved; I do not know its date, whether it describes a formal order or subpoenas, or whether Nvidia or the SEC commented.
- Share-price reaction on November 17 to 18: not retrieved.
- Nvidia has filed no 8-K describing the independent committee, its mandate, its counsel, or any government inquiry. The first and only EDGAR reference is the forward-looking-statement clause on November 17.
- Part II (Legal Proceedings, Risk Factors) of the Q2 FY2027 10-Q could not be read, so I cannot say whether any SEC, DOJ or Commerce inquiry was already disclosed in August 2026. The readable Note 10 covered only the securities class action and derivative suits.

---

## 6. Other Nvidia 8-Ks in November 2026 and related 2026 filings

### Takeaway
Nvidia filed two 8-Ks in November 2026: Item 5.02 on November 12 (Huang's resignation, effective immediately, no reason given) and Item 2.02 on November 17 (earnings). There is no Item 8.01, 7.01 or 4.02 filing in the month.

### Cited Findings
- All 8-Ks from June to November 22, 2026 ([EDGAR submissions feed](https://data.sec.gov/submissions/CIK0001045810.json), [FILING/ON-RECORD]):

| Filed | Report date | Items | Subject |
|---|---|---|---|
| 2026-06-18 | 2026-06-15 | 8.01, 9.01 | $25.0 billion notes offering in seven series |
| 2026-06-30 | 2026-06-24 | 5.07 | Annual meeting results (content not opened) |
| 2026-07-02 | 2026-06-28 | 5.02 | Ajay Puri to retire; Nicholas Parker appointed EVP, Worldwide Field Operations |
| 2026-08-17 | 2026-08-17 | 1.01, 2.03, 7.01 | SB Energy residual value guaranties, capped at $105 billion, for an OpenAI-affiliated tenant |
| 2026-08-26 | 2026-08-26 | 2.02, 9.01 | Q2 FY2027 results |
| 2026-09-03 | 2026-09-02 | 8.01 | Agreement to acquire Hugging Face (about $11.9 billion) |
| 2026-11-12 | 2026-11-11 | 5.02, 9.01 | CEO resignation; interim CEO; board chair |
| 2026-11-17 | 2026-11-17 | 2.02, 9.01 | Q3 FY2027 results |

- November 12 8-K (accepted 08:52:41 ET): the Board "accepted the resignation of Jen-Hsun Huang" as President, CEO and director, effective immediately. No reason is stated; no separation terms; no mention of an investigation, a committee, the SEC or the 10-Q. Colette M. Kress, 59, was appointed interim CEO "while the Board conducts a search for a new Chief Executive Officer" and remains CFO. Harvey C. Jones, 73, a director since 1993, was appointed Chair. [FILING/ON-RECORD] (pre-Nov 17) — [Nvidia 8-K, SEC EDGAR, 2026-11-12](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvda-20261111.htm)
- The attached press release, "NVIDIA Announces CEO Transition", says the Board "will consider internal and external candidates", that it expects "operations, customer commitments and product roadmap to continue without interruption", and that Nvidia would report Q3 results on November 17 "as previously scheduled". It gives no reason for the resignation. [FILING/ON-RECORD] (pre-Nov 17) — [EX-99.1, SEC EDGAR, 2026-11-12](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvidiaannouncesceotransiti.htm)
- Earlier 2026 Item 5.02 filings relevant to the finance function and board:
  - Chief Accounting Officer Donald Robertson retired from that role effective May 4, 2026; Scott Gawel (previously CAO at Intel) became principal accounting officer the same day. — [8-K, 2026-04-27](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000026/nvda-20260424.htm)
  - Suzanne Nora Johnson joined the Board and its Audit Committee effective July 13, 2026. — [8-K, 2026-05-08](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000028/nvda-20260507.htm)
  - Director Persis Drell resigned January 20, 2026, "not because of any disagreement with the Company". — [8-K, 2026-01-23](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000003/nvda-20260120.htm)
  All [FILING/ON-RECORD] (pre-Nov 17).
- The August 17 8-K says the form of the SB Energy guaranty agreements "will be filed as an exhibit" to the Q2 FY2027 10-Q. [FILING/ON-RECORD] (pre-Nov 17) — [Nvidia 8-K, SEC EDGAR, 2026-08-17](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm)

### Inferences
- The Item 5.02 filing is unusually bare for the departure of a founder-CEO: no reason, no transition role, no separation terms. If separation arrangements are later agreed, a further Item 5.02 filing would normally follow, and its content might need to be reflected in the 10-Q.

### Gaps
- The 8-K filed 2026-03-06 (Items 5.02, 9.01) and the June annual-meeting 8-K were not opened.
- No EDGAR filing establishes when the independent committee was formed.

---

## 7. Precedents at other large companies, and what delays turned out to mean

### Takeaway
There are two different kinds of precedent and they should not be mixed. In "late with an NT filing" cases involving an internal or regulatory investigation, the usual outcome in this sample was a restatement or at least a material-weakness finding, and delays ran from days to more than a year. Nvidia today is in the other category, "on time but later than usual", where the clean precedents are fewer: Mattel in 2019 (restated, CFO left), Macy's in 2024 (immaterial revision), and Nvidia itself in August 2022 (added disclosure, no change to numbers).

### Cited Findings

All dates, form types and item codes below are [FILING/ON-RECORD] from each company's EDGAR submissions feed (`https://data.sec.gov/submissions/CIK##########.json`, retrieved 2026-11-22; accession numbers and URLs are in `precedent_filing_timelines.csv`). Deadline arithmetic is mine (60 days for a 10-K, 40 for a 10-Q). All sources in this section predate November 17, 2026.

**A. Not late, but later than usual (the Nvidia-type situation)**

| Company | Normal gap | The episode | NT filed? | Outcome |
|---|---|---|---|---|
| Mattel, Q3 2019 | 0 to 1 day for the five prior 10-Qs | Earnings 2019-10-29 with Items 2.02, 4.02 and 5.02; 10-Q and 10-K/A filed 2019-11-12, 14 days later, on the last timely day (day 40 was a Saturday and Monday was Veterans Day) | No | Restated Q3 and Q4 2017; CFO departure; material weaknesses |
| Macy's, Q3 2024 | 3 to 14 days | Preliminary sales only on 2024-11-25; full results 2024-12-11; 10-Q 2024-12-12, exactly day 40 | No | Immaterial revision, not a restatement; material weakness |
| Nvidia, Q2 FY2023 | 0 to 2 days | 10-Q 7 days after earnings, accepted 73 seconds after an export-control 8-K | No | Added disclosure only |
| Under Armour, Q3 2019 | 2 to 9 days | 10-Q 4 days after earnings (2019-11-04, 2019-11-08) while SEC and DOJ investigations were public | No | No timing anomaly |
| Nikola, 2020 to 2021 | 0 days | Every 10-Q and 10-K filed the same day as earnings through the post-September 2020 government investigations | No | No timing anomaly |
| GE, 2017 to 2018 | 7 to 12 days (10-Q); 26 to 35 (10-K) | 10-K 30 days after the 2018-01-24 earnings release | No | No timing anomaly |
| Boeing, 2019 to 2020 | 0 days (10-Q) | Unchanged through the 737 MAX period; never filed an NT | No | No timing anomaly |

- Mattel: it was made aware of "an anonymous whistleblower letter" on August 6, 2019 and terminated a notes offering. — [Mattel 8-K, SEC EDGAR, 2019-08-08](https://www.sec.gov/Archives/edgar/data/63276/000119312519216983/d771489d8k.htm)
- Mattel's investigation, by the Audit Committee with independent counsel and forensic accountants, took about two months. It found "income tax expense was understated by $109 million in the third quarter of 2017" and overstated by the same amount in Q4 2017, and "did not find that management engaged in fraud". The auditor "has replaced its lead audit engagement partner". Mattel said it was "working diligently to prepare and file the amended report by November 12, 2019", and did. — [Mattel 8-K EX-99.2, SEC EDGAR, 2019-10-29](https://www.sec.gov/Archives/edgar/data/63276/000119312519277846/d788142dex992.htm); [Mattel 8-K](https://www.sec.gov/Archives/edgar/data/63276/000119312519277846/d788142d8k.htm)
- Macy's: a single employee "intentionally made erroneous accounting accrual entries to hide" "approximately $132 to $154 million of cumulative delivery expenses" "from the fourth quarter of 2021 through fiscal quarter ended November 2, 2024". The company delayed the earnings release itself and said it would report "by December 11, 2024". — [Macy's 8-K EX-99.1, SEC EDGAR, 2024-11-25](https://www.sec.gov/Archives/edgar/data/794367/000079436724000199/finalm3q24preliminaryearni.htm)
- Macy's outcome: "approximately $151 million of cumulative delivery expenses"; errors not material to any prior period, corrected "by adjusting prior period financial statements"; a material weakness; the prior-year internal control report and KPMG's related opinion "should no longer be relied upon". — [Macy's 8-K, SEC EDGAR, 2024-12-11](https://www.sec.gov/Archives/edgar/data/794367/000162828024050691/n-20241211.htm)

**B. Late, with an NT filing, during an investigation or review**

| Company and report | Due | NT filed | Report filed | Days late | Trigger | Restated? |
|---|---|---|---|---|---|---|
| Nvidia, Q2 FY2007 10-Q | 2006-09-08 | 2006-09-11 | 2006-11-29 | 82 | Audit Committee option-grant review; SEC information request | Yes: $199.6 million pre-tax |
| Nvidia, FY2002 10-K | 2002-04-29 (assuming the 90-day rule then in force) | 2002-04-29 | 2002-05-14 | within 15-day extension | SEC staff concerns; Audit Committee review | Yes: net +$1.3 million over 3 years |
| Apple, Q3 FY2006 10-Q | 2006-08-10 | 2006-08-11 | 2006-12-29 | 141 | Option-grant irregularities; special committee | Yes (Item 4.02 on 2006-08-04) |
| Broadcom, Q2 2006 10-Q | not computed | 2006-08-09 | 2007-01-23 | n/c | Option grants (Item 4.02 on 2006-07-14 and 2006-09-12) | Yes (10-K/A, 10-Q/A) |
| Dell, Q2 FY2007 10-Q | 2006-09-13 | 2006-09-14 | 2007-10-30 | 412 | SEC investigation; Audit Committee investigation; SDNY subpoena | Yes: FY2003 to Q1 FY2007 |
| Hertz, Q1 2014 10-Q | 2014-05-12 | 2014-05-13 | FY2014 10-K on 2015-07-16 | about 14 months to the restated annual report | Accounting errors found in close; Audit Committee review | Yes (Item 4.02 twice) |
| Marvell, Q2 FY2016 10-Q | 2015-09-10 | 2015-09-11 | 2016-07-21 | 315 | Audit Committee investigation of revenue "pull-ins"; auditor resigned | Not established from text read |
| Kraft Heinz, FY2018 10-K | 2019-02-27 | 2019-02-28 | 2019-06-07 | 100 | Internal procurement investigation after SEC subpoena | Yes: about $181 million cumulative |
| Tupperware, FY2022 10-K | not computed | 2023-03-16 | 2023-10-13 | n/c | Item 4.02 on same day as NT | Yes |
| ADM, FY2023 10-K | 2024-02-29 | 2024-03-01 | 2024-03-12 | within 15-day extension | Investigation of Nutrition intersegment sales after SEC document request | Segment data restated later (Item 4.02, 2024-11-05) |
| ADM, Q3 2024 10-Q | 2024-11-12 | 2024-11-12 | 2024-11-18 | within 5-day extension | Further intersegment errors | Yes: 10-K/A and two 10-Q/As |
| Super Micro, FY2024 10-K | 2024-08-29 | 2024-08-30 | 2025-02-25 | 180 | Board committee review; EY resigned 2024-10-24 | No restatement indicated |
| Lordstown, Q1 2021 10-Q | not computed | 2021-05-18 | 2021-06-08 | n/c | SPAC warrant accounting | Yes (10-K/A) |
| Tesla, FY2012 10-K | 2013-03-01 | 2013-03-04 | 2013-03-07 | within 15-day extension | Cash-flow classification error | Reclassification only |

Supporting quotes:

- Kraft Heinz NT 10-K: "At this time the Company does not expect matters subject to the investigation to be material to its current period or any prior period financial statements." Ten weeks later it restated: "several employees in the procurement area engaged in misconduct", cumulative misstatement about $181 million, and the investigation "did not identify any misconduct by any member of the senior management team". A second SEC subpoena followed on March 1, 2019. — [Kraft Heinz NT 10-K, 2019-02-28](https://www.sec.gov/Archives/edgar/data/1637459/000163745919000019/nt10-k.htm); [Kraft Heinz 8-K Items 2.02 and 4.02, 2019-05-06](https://www.sec.gov/Archives/edgar/data/1637459/000163745919000033/may2019form8-k.htm)
- Kraft Heinz was a 0-to-1-day filer before this episode (five of six prior reports), so the first visible sign was the same as Nvidia's: earnings on 2019-02-21 without the 10-K. — Kraft Heinz EDGAR feed
- Super Micro NT 10-K: "the Board of Directors has formed a committee to review certain of the Company's internal controls and other matters" and "the Company does not anticipate the 2024 Form 10-K will contain any material changes to its results". EY then resigned, citing "information that has recently come to our attention". The special committee found no "substantial concerns about the integrity of the Company's senior management". The 10-K was filed on the last day of Nasdaq's 180-day exception with the error-correction box unchecked. — [Super Micro NT 10-K, 2024-08-30](https://www.sec.gov/Archives/edgar/data/1375365/000137536524000031/smci-form12bx25nt10xkx2024.htm); [8-K Item 4.01, 2024-10-30](https://www.sec.gov/Archives/edgar/data/1375365/000137536524000036/smci-20241024.htm); [8-K, 2024-12-02](https://www.sec.gov/Archives/edgar/data/1375365/000137536524000044/smci-20241127.htm); [10-K, 2025-02-25](https://www.sec.gov/Archives/edgar/data/1375365/000137536525000004/smci-20240630.htm); [8-K Item 3.01, 2025-02-26](https://www.sec.gov/Archives/edgar/data/1375365/000137536525000007/smci-20250221.htm)
- ADM: CFO placed "on administrative leave, effective immediately"; investigation followed "a voluntary document request by the Securities and Exchange Commission"; later, prior filings "should no longer be relied upon" for segment disclosures, with no material impact expected on consolidated statements. — [ADM 8-K, 2024-01-22](https://www.sec.gov/Archives/edgar/data/7084/000119312524011608/d737314d8k.htm); [ADM NT 10-K, 2024-03-01](https://www.sec.gov/Archives/edgar/data/7084/000119312524054362/d33594dnt10k.htm); [ADM 8-K Item 4.02, 2024-11-05](https://www.sec.gov/Archives/edgar/data/7084/000000708424000034/adm-20241104.htm)
- Apple NT 10-Q: "the Company will likely need to restate its historical financial statements". — [Apple NT 10-Q, 2006-08-11](https://www.sec.gov/Archives/edgar/data/320193/000110465906053743/a06-16145_1nt10q.htm)
- Dell: delay stemmed from "questions raised in connection with the previously announced informal investigation by the U.S. Securities and Exchange Commission". The Audit Committee later found "evidence that certain adjustments appear to have been motivated by the objective of attaining financial targets"; cumulative net income reduction "between $50 million and $150 million". — [Dell NT 10-Q, 2006-09-14](https://www.sec.gov/Archives/edgar/data/826083/000095013406017769/d39660ntnt10vq.htm); [Dell 8-K Item 4.02, 2007-08-16](https://www.sec.gov/Archives/edgar/data/826083/000095013407018421/d49260e8vk.htm)
- Marvell: "the Audit Committee of the Company's Board of Directors is conducting an independent investigation of certain accounting and internal control matters"; the eventual 10-K cites "the resignation of our independent registered public accounting firm and an Audit Committee investigation" and says "we are also the subject of investigations by the Securities and Exchange Commission and the U.S. Attorney". — [Marvell NT 10-Q, 2015-09-11](https://www.sec.gov/Archives/edgar/data/1058057/000119312515317840/d64331dnt10q.htm); [Marvell 10-K, 2016-07-21](https://www.sec.gov/Archives/edgar/data/1058057/000119312516653778/d164959d10k.htm)
- Hertz: "the financial statements for 2011 should no longer be relied upon". — [Hertz 8-K Item 4.02, 2014-06-06](https://www.sec.gov/Archives/edgar/data/1364479/000110465914044345/a14-14905_18k.htm)
- Tesla and Lordstown NT narratives: — [Tesla NT 10-K, 2013-03-04](https://www.sec.gov/Archives/edgar/data/1318605/000119312513088624/d452995dnt10k.htm); [Lordstown NT 10-Q, 2021-05-18](https://www.sec.gov/Archives/edgar/data/1759546/000110465921068940/tm2116892d1_nt10q.htm)

**C. Candidates from the brief with no relevant EDGAR footprint**

- Boeing, GE, AMD, Under Armour and Chegg have never filed an NT 10-K or NT 10-Q (GE, Boeing, AMD: records back to 1994; Under Armour to 2005; Chegg to 2006). [FILING/ON-RECORD]
- Tesla's only NT is the 2013 one above.
- Other NT histories in the feed that were not investigated further: Krispy Kreme (NT 10-Q 2004-12-13, Item 4.02 on 2005-01-04, then NTs through 2006), Nortel (NTs from 2003-11-14 through 2007), Diebold (NTs 2007 to 2008, Item 4.02 on 2008-01-15, five reports filed together 2008-09-30), Symbol (NT 10-Q 2004-11-10, 10-Q five days later), Nikola (only NT is March 2025).
- Luckin (foreign private issuer) and Toshiba (not an SEC registrant in the relevant sense) were not checked.

### Inferences
- **Category A is the right comparison set for now**, and it is small and mixed. In the two cases where a normally fast filer visibly slowed down during an internal investigation but stayed inside the deadline (Mattel, Macy's), the 10-Q arrived on the very last timely day, came with accounting corrections, and came with a material weakness. In the cases where an investigation was external or unrelated to the books (Under Armour, Nikola, Boeing, GE), filing timing did not change at all. Nvidia's behaviour, a deliberate and pre-announced slowdown, looks more like the first group in form; but Mattel and Macy's each said up front that the accounting was the issue, and Nvidia has not.
- A tell worth watching: whether the 10-Q lands well before December 4 (as in August 2022) or on December 4 itself (Mattel and Macy's both used the full 40 days).
- In category B, company statements at the NT stage that results were not expected to change were right for Super Micro and wrong for Kraft Heinz. Early reassurance had limited predictive value in this sample.
- Within this hand-picked sample of 14 NT episodes, at least 11 ended with restated or corrected prior-period figures. That is not a base rate: the list was built from well-known problem cases.
- If Nvidia does file an NT 10-Q, Part III and Part IV(3) would force the first on-record explanation of the delay.

### Gaps
- **Base-rate studies were not retrieved.** No academic or Audit Analytics source was reachable. Leads from memory only, to be verified before any use: Alford, Jones and Zmijewski (1994) on late 10-K filers; Bartov and Konchitchki (2017, Accounting Horizons) on returns around NT filings; Cao, Chen and Higgs (2016, Review of Accounting Studies) on late 10-K filings and audit outcomes; Audit Analytics' periodic NT-filing reports. I am not stating any figures from them.
- Stock-price reactions for every precedent: not retrieved.
- "What triggered it" for Broadcom, Tupperware, Krispy Kreme, Nortel, Diebold and Symbol rests on item codes and dates only; their filings were not opened.
- Whether Marvell ultimately restated was not established from the portion of the 10-K read.
- Under Armour's SEC/DOJ disclosure text was not reached in its 10-Q; that the investigations were public by November 2019 is from memory. [UNVERIFIED]
- I did not find a systematic way to search for other "on time but slower than usual" cases; the category A list is limited to the companies named in the brief.
