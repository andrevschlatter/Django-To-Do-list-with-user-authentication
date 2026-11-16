# Brief: full work-up for replacement artists

Today is 16 November 2026. You are adding new artists to a finished fifty-artist letter campaign. For each artist do ALL of the following, then write the letter.

Read first, and follow exactly:
- writer_brief.md (who the letter writer is, the hard letter rules, sourcing rules)
- routes_brief.md (how to choose the mailing address: no mega-galleries, no home addresses, ranking of routes)
- addresses_in_use.md (addresses you may NOT reuse)
- toledo_museum.md (only to see what kind of Toledo facts exist; do one check per artist for a Toledo Museum of Art holding only if budget allows)

Per artist:
1. LIVING: confirm alive as of today. `curl -sS -L -m 25 -A "artist-research-script/1.0 (curl)" "https://en.wikipedia.org/wiki/<Title>"` works through the session proxy (space requests 20 seconds apart; the site rate-limits). Record birth date, absence of a death date, where they live, and one piece of dated 2026 activity from a search.
2. ROUTE: the single best postal address under routes_brief.md, different from every address in addresses_in_use.md and from your other artists. Give a confidence and what to check by hand.
3. WORK: one specific named work (title, year, medium, size) with a concrete, checkable visual detail from a curator's or gallery's description, not from memory. Prefer something viewable in New York (whitney.org pages open with curl) or a widely available book; say honestly whether it is on view.
4. PRICE: auction record; two or three recent priced results; your own estimated typical painting price (median of cited results, labelled as your estimate, with low-high and the number of results); typical print or small-work price if found; market direction with one line of evidence.
5. LETTER: write it under writer_brief.md. He has not seen the work in person unless it is currently viewable in New York (then SEE_BEFORE_MAILING: yes). Open one door only.

Tools: WebSearch works; HARD BUDGET 28 searches for your whole batch (7 per artist). WebFetch does not work. curl works only for: en.wikipedia.org, whitney.org, www.theartnewspaper.com, karmakarma.org, jackshainman.com, www.petzel.com, www.victoria-miro.com, www.skarstedt.com, www.vitoschnabel.com, www.timothytaylor.com, www.yaresart.com, www.thomasdanegallery.com, www.paulacoopergallery.com. Do not spoof a browser or work round blocks. Tag every fact OPENED or SNIPPET with its URL. Never fill a fact, address or number from memory; write "not found".

Output: one block per artist, exactly these fields in this order:
```
## ARTIST: <name>
CATEGORY: <older artist | Basquiat's circle | blue-chip | mid-career>
ALIVE: ...
GALLERY: <current galleries, noting which are mega-galleries>
MAIL_TO: <full envelope address starting with the artist's name>
ROUTE_WHY: <one line>
ROUTE_CONFIDENCE: <High | Medium | Low-medium | Low>
ROUTE_CHECK: <what to confirm by hand, with the page>
ADDRESS_STATUS: <"Verified on official page" + URL | "UNVERIFIED: check by hand" + reason>
WORK: ...
VISUAL_DETAIL: ...
WORK_2: <or none>
SEE_BEFORE_MAILING: <yes: where/until | no: met in reproduction>
DOOR: <studio | print or small piece>
PRICE_ESTIMATE: <single US$ figure, or "none">
PRICE_LOW: <US$ or none>
PRICE_HIGH: <US$ or none>
PRICE_RESULTS: <number of results behind the estimate>
PRINT_OR_SMALL_WORK: ...
RECORD: ...
PRICE_BASIS: <the results used, one line, with URLs>
PRICE_CONFIDENCE: ...
MARKET_DIRECTION: <Rising | Stable | Cooling | Unknown>
MARKET_NOTE: <3-5 lines with URLs>
FLAGS: ...
LETTER:
<<<
<letter>
>>>
```
