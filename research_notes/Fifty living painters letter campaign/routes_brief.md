# Brief: find the best direct mailing route for each artist

Context: a private individual in New York is posting one sincere, handwritten fan letter to each of fifty living painters. The letters ask for nothing. He does NOT want to send them to the huge multi-city galleries, where mail is filtered. He wants, for each artist, the one postal address where the artist personally (or their own small studio team) is most likely to open the letter and perhaps reply. Every artist must end up with a DIFFERENT address from every other artist. Today is 16 November 2026.

## What counts as a good route, best first
1. The artist's OWN studio contact, as published by the artist or studio for professional contact: a studio website with a postal address, a studio company/LLC business address the studio itself publishes, a studio manager contact.
2. An organisation the artist founded or runs and is physically present at: a foundation, residency, project space, school, or their own gallery (examples of the kind of thing: an artist-run residency, an artist's foundation with a public office, a gallery the artist owns).
3. A post the artist actually holds: a university or academy department where they currently teach, with the department's postal address.
4. A small organisation that works with them hands-on and knows them personally: the print studio or print publisher that makes their editions, a small single-location gallery that has shown them for years, a non-profit they sit on the board of. (The letters mention hoping to own a print one day, so a print studio is a natural route.)
5. Only as a last resort: a larger gallery. If you must, pick the smallest gallery that currently represents them, and say plainly that it is a fallback.

EXCLUDE as recommendations: Gagosian, David Zwirner, Hauser & Wirth, Pace, White Cube, Lisson, Thaddaeus Ropac, Perrotin, Almine Rech, Gladstone, Marian Goodman, Sprüth Magers, Lévy Gorvy Dayan, Max Hetzler. Mention them only as "current mega-gallery, excluded".

HARD LIMIT on privacy: do NOT look for or record home addresses. Do not use property records, voter rolls, people-search or data-broker sites, or addresses that appear only because a journalist described where the artist lives. A studio address counts only if the artist, the studio, or an organisation they run publishes it as a contact point, or it is a registered public address of their foundation/company that they themselves list. If the only thing you can find is a home, write "no published direct route" and move to the next tier.

## Also record, if you find it
- Any evidence the artist reads or answers letters from strangers (an interview remark, a story about replying to mail, a studio FAQ).
- Any statement that a route does NOT accept unsolicited mail.
- Where the artist is physically based now (city only), so the route matches where they actually are.

## Tools and limits
- WebSearch works. HARD BUDGET: at most 30 searches for your whole batch (about 3 per artist). Write targeted queries, e.g. "<artist> studio contact address", "<artist> foundation", "<artist> professor university", "<artist> print publisher editions studio", "<artist> studio manager". If a search returns a limit error, stop and write up what you have.
- WebFetch does not work in this session. Plain `curl -sS -L -m 25 <url>` through the session proxy works ONLY for these hosts: en.wikipedia.org, whitney.org, www.theartnewspaper.com, karmakarma.org, jackshainman.com, www.petzel.com, www.victoria-miro.com, www.skarstedt.com, www.vitoschnabel.com, www.timothytaylor.com, www.yaresart.com, www.thomasdanegallery.com, www.paulacoopergallery.com. Do not spoof a user agent or try to get round blocks. Everything else will be search-summary level.
- Label every fact OPENED (you read the page) or SNIPPET (from a search summary of the cited URL). Never fill an address from memory. If you cannot find something, say "not found".

## Output: one block per artist, in the order given
```
## ARTIST: <name>
BASED: <city/country now> [URL]
ROUTE_1: <full postal address, written as it should appear on an envelope, starting with the artist's name> 
ROUTE_1_TYPE: <own studio | artist-run organisation | teaching post | print studio | small gallery | fallback larger gallery>
ROUTE_1_WHY: <one or two sentences: why the artist is likely to see it here>
ROUTE_1_SOURCE: <URL> <OPENED|SNIPPET>
ROUTE_1_CONFIDENCE: <high | medium | low> that the address is current and that mail there reaches the artist
ROUTE_2: <a second, different address of a different organisation, same sub-fields on following lines as ROUTE_2_TYPE etc., or "none found">
REPLIES_TO_MAIL: <evidence or "nothing found">
WARNINGS: <no-unsolicited-mail notices, conflicts between sources, anything to check by hand, or "none">
```
Give two routes wherever possible, because addresses will be de-duplicated across all fifty artists afterwards and a second option is needed when two artists share a first choice.
