# Group 2 — older painters (b): Pindell, Dine, Katz, Wylie, Poons, Bradley, Williams (Heilmann deceased)

Checked 16 November 2026.

## Summary table

| Artist | Alive evidence | Primary gallery | Mailing address | Address verified on official page | Work 1 |
|---|---|---|---|---|---|
| Howardena Pindell (b. 1943) | Wikipedia: no death date, "Living people"; White Cube page says "lives and works in New York"; in *Hard Art*, MoMA PS1, opened 5 Nov 2026 | Garth Greenan Gallery, New York (also White Cube) | Garth Greenan: 10 or 25 Greene Street, New York (ZIP and which door not confirmed). Verified fallback: White Cube, 1002 Madison Avenue, New York, NY 10075 | **No** for Garth Greenan (site not reachable). **Yes** for White Cube | *Untitled*, 1970, acrylic on canvas, 69 × 79 1/8 in, Whitney 71.173, not on view |
| Jim Dine (b. 1935) | Wikipedia: no death date, "Living people". No dated 2026 activity opened | Templon (Paris–Brussels) and Cristea Roberts (London), per Wikipedia; neither site reachable | None confirmed | **No** | *Double Isometric Self Portrait (Serape)*, 1964, Whitney 76.35, not on view |
| Alex Katz (b. 1927) | Wikipedia: no death date; it cites a New York Times interview dated 7 Nov 2026 and a Musée Matisse Nice show from 28 Oct 2026 | Gladstone Gallery, New York (also Timothy Taylor, Thaddaeus Ropac) | Gladstone, 515 West 24th Street, New York, NY 10011 (from search summary) | **No** (Gladstone site not reachable) | *The Red Smile*, 1963, oil on linen, 78 7/8 × 115 in, Whitney 83.3, not on view |
| Rose Wylie (b. 1934) | Wikipedia: no death date; Zwirner page says she "lives and works in Kent"; latest dated show ended 23 May 2026 | David Zwirner (since 2017) | David Zwirner, 24 Grafton Street, London W1S 4EZ (or 537 West 20th Street, New York, New York 10011) | **Yes** | No New York museum work found; book: *Rose Wylie: Which One*, David Zwirner Books, 2023 |
| Larry Poons (b. 1937) | Wikipedia: no death date; Yares lists a 2026 painting; Almine Rech Paris solo to 21 May 2026 | Yares Art, New York ("exclusive global representative"); Almine Rech also lists him | Yares Art, 745 Fifth Avenue, 4th Floor, New York, NY 10151 | **Yes** | *Untitled*, 1966, acrylic and graphite pencil on canvas, 130 × 90 in, Whitney 66.84, not on view |
| Peter Bradley (b. 1940) | Wikipedia: no death date, "Living people"; Karma solo to 28 Aug 2026; Karma page shows *Hard Art* (PS1, from 5 Nov 2026) | Karma, New York | Karma, 549 West 26th Street, New York, NY 10001 | **Yes** | *Ruling Light*, 1973, acrylic on canvas, 39 3/4 × 87 in, Whitney 2024.322, not on view |
| William T. Williams (b. 1942) | Wikipedia: no death date, "Living people"; Whitney lists "1942–". No dated 2026 activity opened | Michael Rosenfeld Gallery, New York (from search summary) | 100 Eleventh Avenue at 19th Street, New York, NY 10011 (from search summary) | **No** (gallery site not reachable) | *Drawing for an Epic Idea (Coonograph)*, 1970, watercolour drawing, Whitney 71.47, not on view (a small drawing, not a painting) |
| Mary Heilmann | **Died 14 August 2026** | n/a | n/a | n/a | n/a |

## How this was checked, and what could not be opened

- **Labels.** OPENED = I read the page itself in this run. SNIPPET = carried over from the earlier notes, which came from web-search summaries and were never read on the page.
- **Method.** The WebFetch tool failed on every host with a DNS error. Pages were instead downloaded with plain `curl` through the session's own network proxy (default client identity, nothing spoofed) and read as text. WebSearch was not used.
- **Wikipedia** was read as article source (`?action=raw`), so the dates come straight from the infobox. URLs below are the normal article addresses.
- **Hosts that would not open, with what happened:**
  - `www.garthgreenan.com` redirects to `garthgreenan.com`, which the network policy refuses. Nothing on the Garth Greenan site was read.
  - `www.gladstonegallery.com` redirects to `gladstonegallery.com`, refused. Nothing on the Gladstone site was read.
  - `www.michaelrosenfeldart.com` redirects to `michaelrosenfeld.com`, refused. Nothing on the Michael Rosenfeld site was read.
  - `www.moma.org` returned a "Vercel Security Checkpoint" browser check (HTTP 403) on every collection page. No MoMA page was read.
  - `www.metmuseum.org` returned the same checkpoint (HTTP 429) on two attempts. No Met page was read.
  - `www.hauserwirth.com` returned 429 on its home page; not needed further.
  - Templon, Cristea Roberts, Gray, Thaddaeus Ropac, auction houses: not on the allowed list, not tried.
- **Consequence.** All New York museum works below are from the Whitney, the only New York museum site that opened. None of them is on view. MoMA and Met entries are SNIPPET only.
- **To finish the open items**, the bare domains `garthgreenan.com`, `gladstonegallery.com`, `michaelrosenfeld.com`, plus `templon.com` and `cristearoberts.com`, need to be allowed.

---

## 1. Howardena Pindell

### Alive? Birth, residence, latest dated activity
- Born 14 April 1943, Philadelphia; death date fields empty; article is in "Living people" — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Howardena_Pindell)
- Conflict: the Whitney's own field gives "Date of birth April 4, 1943", while quoting Wikipedia's 14 April on the same page — OPENED [Whitney artist page](https://whitney.org/artists/1028). The Whitney lists her as "1943–".
- "Lives and works in New York"; a White Cube film shows her "studio in the Bronx, New York" — OPENED [White Cube artist page](https://www.whitecube.com/artists/howardena-pindell)
- Professor of art at Stony Brook University, teaching there since 1979 — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Howardena_Pindell); OPENED [The Art Newspaper, 1 Jul 2022](https://www.theartnewspaper.com/2022/07/01/howardena-pindell-interview-kettles-yard-cambridge)
- Latest dated activity: included in *Hard Art*, MoMA PS1, Queens, 5 November 2026 – 15 March 2027 (item posted 5 Nov 2026) — OPENED [White Cube news](https://www.whitecube.com/news/richard-hunt-at-moma-ps1)
- Latest gallery solo on White Cube's page: *Off the Grid*, Bermondsey, London, 21 November 2025 – 18 January 2026 — OPENED [White Cube artist page](https://www.whitecube.com/artists/howardena-pindell)
- No page read gives a direct sighting of her after June 2026 (Art Basel Awards ceremony, 17 June 2026).

### Galleries
- Garth Greenan Gallery, New York: gallery site not reachable. Indirect confirmation: the Whitney credits her image "Courtesy the artist and Garth Greenan Gallery, New York" — OPENED [Whitney](https://whitney.org/collection/works/298); The Art Newspaper captions her works "Courtesy the artist, Garth Greenan Gallery and Victoria Miro" (2022) — OPENED [The Art Newspaper](https://www.theartnewspaper.com/2022/07/01/howardena-pindell-interview-kettles-yard-cambridge)
- White Cube: full artist page, two gallery solos (Hong Kong 2024–25, London 2025–26), and a news item titled "Howardena Pindell joins White Cube" (item itself not opened) — OPENED [White Cube artist page](https://www.whitecube.com/artists/howardena-pindell), [White Cube news archive](https://www.whitecube.com/news/archive/artists/howardena-pindell)
- Victoria Miro: credited alongside Garth Greenan in 2022; whether still current is UNVERIFIED (Victoria Miro site not opened) — OPENED [The Art Newspaper](https://www.theartnewspaper.com/2022/07/01/howardena-pindell-interview-kettles-yard-cambridge)
- Michael Rosenfeld Gallery page for her: SNIPPET, site not reachable — [Michael Rosenfeld](https://michaelrosenfeldart.com/artists/howardena-pindell-b1943)

### Mailing address
- **Garth Greenan, not verified.** The gallery has left West 20th Street and taken "two storefronts across from each other on Greene Street in Soho", at 10 and 25 Greene Street — OPENED [The Art Newspaper, 15 Sep 2026](https://www.theartnewspaper.com/2026/09/15/new-york-galleries-moving-manhattan-soho-rising-chelsea-tribeca-endure). The article gives no ZIP, suite, or which door takes mail. Its old block is being re-let (47 Canal at 529 West 20th Street), so do not post to West 20th Street.
- The gallery's own contact page could not be opened (`garthgreenan.com` refused). Old-notes detail (545 West 20th Street, tel 212.929.1351, info@garthgreenan.com) is SNIPPET and out of date.
- **Verified fallback:** White Cube New York, 1002 Madison Avenue, New York, NY 10075 — OPENED, site footer on [White Cube](https://www.whitecube.com/news/archive/artists/howardena-pindell)

### Works to see in New York
- *Untitled*, 1970, acrylic on canvas, 69 × 79 1/8 in (175.3 × 201 cm), Whitney Museum, accession 71.173, "Purchase, with funds from the Albert A. List Family". **Not on view.** Image description on the page: "Innumerable specks of pink, orange, yellow, green, and blue, densely accumulated into a soft and smooth polychromatic abstraction" — OPENED [Whitney](https://whitney.org/collection/works/298)
- The Whitney holds three works by her (one painting, one print, the video *Free, White and 21*, 1980); the artist page shows "Not on view" — OPENED [Whitney artist page](https://whitney.org/artists/1028)
- On view now, but work details not obtained: *Hard Art*, MoMA PS1, to 15 March 2027 — OPENED [White Cube news](https://www.whitecube.com/news/richard-hunt-at-moma-ps1). The two titles in the old notes (*Untitled*, 1969–73; *Feast Day of Iemanja II*, 1980) are SNIPPET.
- Day trip: Dia Art Foundation acquired 21 works; long-term exhibition at Dia Beacon opens **30 January 2027**, large paintings from the mid- to late 1970s — OPENED [White Cube news, posted 24 Nov 2025](https://www.whitecube.com/news/howardena-pindell-at-dia-beacon). This corrects the old notes, which said December 2026.
- MoMA *Memory: Past* (1980–81) and four Met works: SNIPPET, pages blocked.

### Market and institutions
- Named a Medallist in the "Icon Artists" category of the 2026 Art Basel Awards; ceremony 17 June 2026 — OPENED [White Cube news](https://www.whitecube.com/news/theaster-gates-julie-mehretu-and-howardena-pindell-named-2026-art-basel-awards-medallists). This confirms the old low-authority Masterworks item.
- American Federation of Arts Cultural Leadership Award, gala 10 November 2025 — OPENED [White Cube news](https://www.whitecube.com/news/howardena-pindell-to-receive-cultural-leadership-award-from-the-american-federation-of-the-arts)
- Museum solos since 2022: Fruitmarket Edinburgh touring to Kettle's Yard, Spike Island and IMMA Dublin (2022–23); Baltimore Museum of Art (2022); Museum of Fine Arts Houston (2022) — OPENED [White Cube artist page](https://www.whitecube.com/artists/howardena-pindell)
- Bourse de Commerce, Paris, 8 October 2025 – 19 January 2026 (with Lygia Pape, per the link title) — OPENED [White Cube news archive](https://www.whitecube.com/news/archive/artists/howardena-pindell)
- Auction prices: none found on any reachable page.

### Quote
- "I love beauty and have been criticised for making works that are too beautiful." — OPENED [The Art Newspaper, 1 Jul 2022](https://www.theartnewspaper.com/2022/07/01/howardena-pindell-interview-kettles-yard-cambridge)
- On Josef Albers's colour course at Yale: "The colour course changed my life. I don't know where my eye would be without it." — same source.
- "The advice I would give to young artists is not to give up." — OPENED [White Cube artist page](https://www.whitecube.com/artists/howardena-pindell)

### Gaps
- Garth Greenan's exact postal line. Titles and details of her works in *Hard Art*. Auction data.

---

## 2. Jim Dine

### Alive? Birth, residence, latest dated activity
- Born 16 June 1935, Cincinnati, Ohio (birth name James Lewis Dine); the infobox has no death date; article is in "Living people" — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Jim_Dine)
- The Whitney's artist page shows no death year and credits "© Jim Dine/Artists Rights Society (ARS), New York" — OPENED [Whitney](https://whitney.org/artists/361?q%5Bclassification_cont%5D=Paintings)
- Residence: not stated in the Wikipedia article. Old-notes detail (Montrouge near Paris, Göttingen, Walla Walla) is SNIPPET.
- Latest dated activity: none on any page opened. The Art Newspaper's "Jim Dine" keyword page lists only a 2021 article — OPENED [The Art Newspaper](https://www.theartnewspaper.com/keywords/jim-dine). The Palm Springs Art Museum show (21 Nov 2026 – 19 Apr 2027) is SNIPPET.
- Alive evidence is therefore weaker than for the others: absence of a death record on Wikipedia, nothing positive from 2026.

### Galleries
- Wikipedia's "long-term collaborations" list — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Jim_Dine):
  - Daniel Templon, Paris–Brussels, 2000–present
  - Alan Cristea (now Cristea Roberts Gallery), London, 1979–present
  - Pace Gallery, New York, 1978–2016 (ended)
  - Richard Gray, Chicago, 1983–2018; Gray Gallery, Chicago, 2016–2021 (ended)
  - Publisher Gerhard Steidl, Göttingen, 1998–present
- Pace: he is not on Pace's current artist list, and `/artists/jim-dine/` returns "not found" — OPENED [Pace artists](https://www.pacegallery.com/artists/)
- Templon, Cristea Roberts and Gray sites are not on the allowed list; current representation there is UNVERIFIED on an official page.
- On this evidence he has **no New York gallery** at present.

### Mailing address
- **None verified.** No official gallery page for Dine could be opened.
- Unofficial lead only: Cristea Roberts Gallery "is located at 43 Pall Mall, London" (no postcode given) — OPENED [Wikipedia, Cristea Roberts Gallery](https://en.wikipedia.org/wiki/Cristea_Roberts_Gallery). Not from an official page; check before use.
- Templon's Paris address: not obtained (no Wikipedia article at "Galerie Templon"; site not reachable).

### Works to see in New York
- *Double Isometric Self Portrait (Serape)*, 1964, oil on canvas with metal hardware and dowels, overall 57 3/8 × 84 5/8 in (145.7 × 214.9 cm), two canvases each with a 51 3/4 in chain. Whitney Museum, accession 76.35, "Gift of Helen W. Benjamin in memory of her husband, Robert M. Benjamin". **Not on view.** Image description: "Two colorful robe-shaped panels with bold geometric color blocks and hanging pull chains" — OPENED [Whitney](https://whitney.org/collection/works/2735)
- *The Black Rainbow*, 1959–1960, oil and corrugated cardboard on paperboard, 39 5/8 × 59 3/4 in (100.7 × 151.8 cm). Whitney Museum, accession 74.112, "Gift of Andy Warhol". **Not on view.** Image description: "Concentric black and gray painted arches with gold accents and the words 'The Black Rainbow' at the top" — OPENED [Whitney](https://whitney.org/collection/works/2462)
- The Whitney holds 93 works by him, six classed as paintings (also *Afternoon Robe*, 1976; *Long Island Landscape*, 1963; *The Toaster*, 1962; *A Black Shovel, Number 2*, 1962) — OPENED [Whitney](https://whitney.org/artists/361?q%5Bclassification_cont%5D=Paintings)
- MoMA, Met and Guggenheim hold his work per Wikipedia's collections list; no page opened.

### Market and institutions
- Nothing on any reachable page. Artnet lot listings without prices: SNIPPET.
- Museum shows since 2022: none confirmed on an opened page.

### Quote
- No quote about painting found. Nearest: on first seeing German Expressionist woodcuts in 1954, "I was shocked by them" — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Jim_Dine) (Wikipedia quoting Dine's book; secondary).

### Gaps
- Positive 2026 evidence of life; residence; any official gallery address; market. He is the weakest entry for a letter sent "care of gallery", and the route would be Paris or London, not New York.

---

## 3. Alex Katz

### Alive? Birth, residence, latest dated activity
- Born 24 July 1927, Brooklyn, New York; death date fields empty — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Alex_Katz)
- Wikipedia cites a New York Times piece dated 7 November 2026, "'It Gave Me a Lot of Anxiety': Alex Katz on Sharing the Room With Matisse", about *Henri Matisse – Alex Katz. The Silence of Painting*, Musée Matisse Nice, 28 October 2026 – 18 January 2027 — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Alex_Katz). The NYT article itself was not opened. The old notes gave 21 October as the opening date; Wikipedia says 28 October.
- Photographed "in his downtown studio, New York City, 2024"; biography says "b. 1927, Brooklyn, New York" — OPENED [Timothy Taylor](https://www.timothytaylor.com/artists/alex-katz/)
- Latest dated shows on a gallery's own page: *Various Trees*, Timothy Taylor London, 5 March – 11 April 2026 (landscapes of 2023–2025); group show *Timothy Taylor: 30 Years*, 23 April – 30 May 2026 — OPENED [Timothy Taylor](https://www.timothytaylor.com/artists/alex-katz/)
- Residence "New York and Maine" and the PBS 99th-birthday segment: SNIPPET.

### Galleries
- "Katz is represented by Gladstone Gallery in New York, Timothy Taylor Gallery in London, and Galerie Thaddaeus Ropac in Paris/Salzburg"; earlier Pace (10 years) and Marlborough (30 years) — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Alex_Katz)
- Timothy Taylor: artist page confirmed — OPENED [Timothy Taylor](https://www.timothytaylor.com/artists/alex-katz/)
- Gladstone: artist page **not opened** (site refused). Gladstone solos of 2021, 2023–24 and 30 Oct – 20 Dec 2025 are SNIPPET.
- Ropac: not on the allowed list.

### Mailing address
- **Not verified on an official page.** Gladstone's site could not be opened.
- SNIPPET, from the old notes: 515 West 24th Street, New York, NY 10011 (tel 212 206 9300); 530 West 21st Street, New York, NY 10011; 130 East 64th Street, New York, NY 10065 — [Gladstone](https://gladstonegallery.com/en/about/)
- Which location takes artist mail is not stated anywhere read.

### Works to see in New York
- *The Red Smile*, 1963, oil on linen, 78 7/8 × 115 in (200.3 × 292.1 cm). Whitney Museum, accession 83.3, "Purchase, with funds from the Painting and Sculpture Committee". **Not on view.** The page describes "a profile of his wife Ada's face, set against a smooth red background", "nearly 7 x 10 feet"; image description: "A woman wearing red lipstick smiles softly, her face in profile against a more vivid red background" — OPENED [Whitney](https://whitney.org/collection/works/407)
- The Whitney holds 83 works by Katz, including *Bill 3* (2017; "Two large brown faces lean toward each other against a bright yellow background") and *Black Scarf* (1996) — OPENED [Whitney artist page](https://whitney.org/artists/676). On-view status of those not checked.
- MoMA *Passing* (1962–63): SNIPPET, page blocked.

### Market and institutions
- Museum shows since 2022 — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Alex_Katz), [Timothy Taylor](https://www.timothytaylor.com/artists/alex-katz/):
  - *Alex Katz: Gathering*, Guggenheim, 21 Oct 2022 – 20 Feb 2023
  - Thyssen, Madrid, 2022 (first show in Spain)
  - *Theater and Dance*, Colby, then touring to Naples FL, Seattle, San Diego, Wichita (to 10 May 2026)
  - *Dancing with Reality*, Kunsthalle Tübingen, 28 Mar – 13 Sep 2026
  - *Out of Sight: A Drawing Survey*, Colby, 21 May – 11 Oct 2026
  - *Quick Things Passing*, Colby, 12 Mar 2026 – 17 Jan 2027
  - Musée Matisse Nice, 28 Oct 2026 – 18 Jan 2027
- National Medal of Arts awarded by President Biden — headline dated 21 Oct 2024, OPENED [The Art Newspaper keyword page](https://www.theartnewspaper.com/keywords/alex-katz) (article not opened)
- Auction prices: none found on any reachable page.

### Quote
- "I always try to paint in the present tense. If you paint stories, you're painting in the past tense." — OPENED [Timothy Taylor](https://www.timothytaylor.com/artists/alex-katz/)
- On *The Red Smile*'s effect: the "immediate sensation you see before you focus" — OPENED [Whitney](https://whitney.org/collection/works/407)

### Gaps
- Gladstone address and artist page on the official site. A New York work confirmed on view. He turns 100 on 24 July 2027.

---

## 4. Rose Wylie

### Alive? Birth, residence, latest dated activity
- Born 14 October 1934, Hythe, Kent; death date fields empty — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Rose_Wylie)
- "Wylie lives and works in Kent, England" — OPENED [David Zwirner artist page](https://www.davidzwirner.com/artists/rose-wylie). Wikipedia: she moved to Newnham, Kent in 1968.
- Interviewed aged 91 by The Art Newspaper, published 24 February 2026 — OPENED [The Art Newspaper](https://www.theartnewspaper.com/2026/02/24/rose-wylie-artist-interview)
- Latest dated shows: *The Picture Comes First*, Royal Academy of Arts, London, 28 February – 19 April 2026 (more than 90 works); *Henri, Egypt...Bette, Bear*, David Zwirner Paris, 2026 — OPENED [David Zwirner artist page](https://www.davidzwirner.com/artists/rose-wylie). Paris dates 2 April – 23 May 2026 are SNIPPET.
- A 2026 work on paper, *Bear and Bette*, is listed as available; a 2026 video "Lunch with Rose Wylie (Part II)" was filmed after the RA opening — same page.
- Nothing dated after May 2026 was found.

### Galleries
- "The artist's work has been represented by David Zwirner since 2017" — OPENED [David Zwirner artist page](https://www.davidzwirner.com/artists/rose-wylie)
- Earlier: Union Gallery (Wikipedia, marked "citation needed") — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Rose_Wylie)
- Jarilager Gallery is credited for a privately owned painting in the RA show; representation UNVERIFIED — OPENED [The Art Newspaper](https://www.theartnewspaper.com/2026/02/24/rose-wylie-artist-interview)

### Mailing address
- **London (natural route for a Kent artist):** David Zwirner, 24 Grafton Street, London W1S 4EZ; tel +44 203 538 3165; london@davidzwirner.com — OPENED [David Zwirner London](https://www.davidzwirner.com/galleries/london)
- **New York:** David Zwirner, 537 West 20th Street, New York, New York 10011; tel +1 212 517 8677; newyork@davidzwirner.com — OPENED [David Zwirner New York](https://www.davidzwirner.com/galleries/new-york)
- Also: 519, 525 & 533 West 19th Street, New York, New York 10011; tel 1 212 727 2070 — OPENED [David Zwirner 19th Street](https://www.davidzwirner.com/galleries/new-york/19th-street)
- Flag: both location pages state "we do not accept unsolicited materials". That is aimed at artist submissions, but a fan letter may or may not be forwarded.

### Works to see in New York / in a book
- No New York museum work found. A Whitney collection search for "Rose Wylie" returns "No matching works" — OPENED [Whitney search](https://whitney.org/collection/works?q%5Bsearch_cont%5D=Rose+Wylie). Zwirner's list of collections holding her work names no New York museum — OPENED [David Zwirner artist page](https://www.davidzwirner.com/artists/rose-wylie). MoMA and Met could not be searched.
- Monograph: *Rose Wylie: Which One*, David Zwirner Books, 2023, hardcover, 218 pages, ISBN 9781644230756; foreword by Nicholas Serota, texts by Judith Bernstein, David Salle and Barry Schwabsky, interview by Hans Ulrich Obrist — OPENED [David Zwirner Books](https://www.davidzwirner.com/collect/rose-wylie-which-one-book)
- Also listed: *Rose Wylie: The Picture Comes First* (Royal Academy of Arts); *Rose Wylie* (Lund Humphries) — OPENED [David Zwirner artist page](https://www.davidzwirner.com/artists/rose-wylie). Years not shown.
- Large paintings named on the gallery page (location not New York): *Ballet Backdrop*, 2024, oil on canvas in four parts, 144 1/8 × 119 3/4 in (366 × 304 cm); *HAND, Drawing as Central*, 2022, triptych, 72 7/8 × 158 7/8 in, collection of S.M.A.K., Ghent — same page.
- Works named in the RA show: *Yellow Strip* (2006); *Kill Bill (Film Notes)* (2007) — OPENED [The Art Newspaper](https://www.theartnewspaper.com/2026/02/24/rose-wylie-artist-interview)

### Market and institutions
- "The first woman painter, and only the second female artist, to occupy the main galleries" of the Royal Academy — OPENED [The Art Newspaper](https://www.theartnewspaper.com/2026/02/24/rose-wylie-artist-interview)
- Museum solos since 2022: S.M.A.K. Ghent (26 Nov 2022 – 30 Apr 2023); Zentrum Paul Klee, Bern (19 Jul – 5 Oct 2025); Royal Academy (2026) — OPENED [David Zwirner artist page](https://www.davidzwirner.com/artists/rose-wylie)
- Zwirner took on her representation in November 2017, per an Art Newspaper headline cited by Wikipedia (article not opened) — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Rose_Wylie)
- Auction prices: none found on any reachable page.

### Quote
- "It's very, very fragile where a painting ends. All the time it sits on a precarious edge." — OPENED [The Art Newspaper, 24 Feb 2026](https://www.theartnewspaper.com/2026/02/24/rose-wylie-artist-interview)
- "I love crossings-out. I love the first decision being left." — same source.
- "The painting isn't illustrating an idea—the painting is the thing." — same source.

### Gaps
- Evidence of life after May 2026. A work viewable in New York. Auction data.

---

## 5. Larry Poons

### Alive? Birth, residence, latest dated activity
- Born 1 October 1937, Tokyo, Japan; death date fields empty — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Larry_Poons). The Whitney lists "1937–" and the same birth date — OPENED [Whitney](https://whitney.org/artists/1040)
- "Poons splits his time between studios in New York City and East Durham, New York" — OPENED [Yares Art](https://www.yaresart.com/artists/larry-poons). Almine Rech: "Lives and works in New York, NY, US" — OPENED [Almine Rech](https://www.alminerech.com/artists/353-larry-poons)
- Latest dated activity: *Kentucky Cols.*, Almine Rech Paris, 21 March – 21 May 2026 — OPENED [Almine Rech](https://www.alminerech.com/artists/353-larry-poons)
- A 2026 painting is listed by Yares (see below); Yares' current group show *Fields of Color X* runs 1 July 2026 – 1 January 2027 (his inclusion not confirmed) — OPENED [Yares Art](https://www.yaresart.com/artists/larry-poons)
- Latest Yares solo: *Provocation, Iliad: Powers + Spells*, 5 April – 15 August 2025 — OPENED [Yares exhibitions](https://www.yaresart.com/exhibitions)
- Nothing dated after May 2026 names him directly.

### Galleries
- "Yares Art is the exclusive global representative of Larry Poons" — OPENED [Yares Art contact page](https://www.yaresart.com/contact)
- Almine Rech lists him on its artists index, with his own page and a 2026 Paris solo — OPENED [Almine Rech artists](https://www.alminerech.com/artists), [Almine Rech](https://www.alminerech.com/artists/353-larry-poons). The two claims sit side by side; how they are arranged is not stated.
- Historic: Green Gallery, then Leo Castelli — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Larry_Poons)

### Mailing address
- **Verified:** Yares Art, 745 Fifth Avenue, 4th Floor, New York, NY 10151; tel 212-256-0969; info@yaresart.com; Monday–Friday 10 am – 6 pm — OPENED [Yares Art contact page](https://www.yaresart.com/contact) (the page prints it once as "New York, NY, 10151" and once as "New York, NY 10151")
- Other Yares offices: 1570 Pacheco St., Suite A1, Santa Fe, NM 87505; 479 Rodeo Drive, Beverly Hills, CA 90210 — same page.

### Works to see in New York
- *Untitled*, 1966, acrylic and graphite pencil on canvas, 130 × 90 in (330.2 × 228.6 cm). Whitney Museum, accession 66.84, "Purchase". **Not on view.** Image description: "Teal background with evenly scattered small rounded leaf shapes in muted green, orange, and pink" — OPENED [Whitney](https://whitney.org/collection/works/412)
- *Untitled*, 1967, acrylic on canvas, 78 3/4 × 127 1/8 in (200 × 322.9 cm). Whitney Museum, accession 98.20, "Gift of Larry L. Aldrich". **Not on view.** Image description: "Orange background with scattered multicolored oval shapes falling diagonally across the canvas" — OPENED [Whitney](https://whitney.org/collection/works/11713)
- Recent work at his gallery: *I Face the Moon*, 2026, acrylic on canvas, 65 1/2 × 75 3/4 in (166.4 × 192.4 cm) — OPENED [Yares Art](https://www.yaresart.com/artists/larry-poons)
- MoMA *Night on Cold Mountain* (1962) and Met *Number 23* (1972): SNIPPET, pages blocked.

### Market and institutions
- The Art Newspaper (2018) describes "his work's modest rise at auction in recent years" and says the market preferred his early "dot paintings" — OPENED [The Art Newspaper, 11 Nov 2018](https://www.theartnewspaper.com/2018/11/11/larry-poons-art-isnt-business)
- Featured in the HBO documentary *The Price of Everything* (2018) — OPENED [Yares Art](https://www.yaresart.com/artists/larry-poons)
- No museum solo since 2022 found on any opened page.
- Artnet lots through 2026 without prices: SNIPPET.

### Quote
- "There is no process except getting out of bed in the morning and feeling like painting and going to paint. The process is just painting." — OPENED [The Art Newspaper, 11 Nov 2018](https://www.theartnewspaper.com/2018/11/11/larry-poons-art-isnt-business)
- "Success is in the studio. That's the only success there is." — same source.
- "First colour, best colour. Next colour, next colour." — same source.

### Gaps
- Direct evidence after May 2026. A New York work on view. Auction figures.

---

## 6. Peter Bradley

### Alive? Birth, residence, latest dated activity
- Born 15 September 1940, Connellsville, Pennsylvania; no death date; article is in "Living people" — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Peter_Bradley_(artist))
- "Bradley lives in Upstate New York" — OPENED [Karma bio](https://karmakarma.org/artists/peter-bradley/bio/)
- Latest solo: *Burning On*, Karma, 549 West 26th Street, New York, 9 July – 28 August 2026; before it *Ten Sculptures*, 188 East 2nd Street, 20 February – 14 March 2026 — OPENED [Karma exhibitions](https://karmakarma.org/artists/peter-bradley/exhibitions/)
- Latest dated activity: Karma's artist page leads with installation views of *Hard Art*, MoMA PS1, 5 November 2026 – 15 March 2027 — OPENED [Karma artist page](https://karmakarma.org/artists/peter-bradley/)
- "Now 85" in July–August 2026 reviews: SNIPPET.

### Galleries
- Karma (works, bio, exhibitions, publications pages) — OPENED [Karma artist page](https://karmakarma.org/artists/peter-bradley/)
- "Bradley is currently represented by the Karma Gallery in New York City" — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Peter_Bradley_(artist))
- No other representing gallery found. Parker Gallery co-published a 2024 book with Karma; not evidence of representation.

### Mailing address
- **Verified:** Karma, 549 West 26th Street, New York, NY 10001; tel (212) 717-1671; Tuesday–Saturday 10 am – 6 pm; info@karmakarma.org — OPENED [Karma information page](https://karmakarma.org/information/)
- Second New York space: 38 White Street, New York, NY 10013 — same page.
- The East 2nd Street addresses in the old notes are not on the current information page. Karma has no `/contact/` page (404); the address page is `/information/`.

### Works to see in New York
- *Ruling Light*, 1973, acrylic on canvas, 39 3/4 × 87 in (101 × 221 cm). Whitney Museum, accession 2024.322, "Purchase, with funds from the Jack E. Chachkes Endowed Purchase Fund". **Not on view.** Image description: "Abstract horizontal painting with pale background and sweeping orange and yellow paint strokes" — OPENED [Whitney](https://whitney.org/collection/works/68836). It is the Whitney's only Bradley, bought in 2024.
- On view now, work titles not obtained: *Hard Art*, MoMA PS1, to 15 March 2027 — OPENED [Karma artist page](https://karmakarma.org/artists/peter-bradley/)
- *Chinese Snowball II*, 1972, oil on canvas, 76 × 51 in, Studio Museum in Harlem, gift of Andre Emmerich, 2001.17 — OPENED [Karma artist page](https://karmakarma.org/artists/peter-bradley/). On-view status not checked.
- Karma lists MoMA and the Met among collections holding his work — OPENED [Karma bio](https://karmakarma.org/artists/peter-bradley/bio/). No titles; museum pages blocked.
- Monograph: *Peter Bradley: Ruling Light*, texts by Dieter Buchhart, Mia Matthias and Nancy Princenthal, Karma, New York, 2023. Also *Peter Bradley*, Karma, New York, 2022 — OPENED [Karma publications](https://karmakarma.org/artists/peter-bradley/publications/)

### Market and institutions
- Museum acquisitions since 2022: Whitney bought *Ruling Light* (accession 2024.322) — OPENED [Whitney](https://whitney.org/collection/works/68836); LACMA owns *Coravilas*, 2021, 77 × 131 in, shown in *New Abstracts: Recent Acquisitions*, 12 Nov 2022 – 29 May 2023 — OPENED [Karma artist page](https://karmakarma.org/artists/peter-bradley/)
- Curated *The De Luxe Show*, Houston, 1971, one of the first racially integrated exhibitions in the United States — OPENED [Karma bio](https://karmakarma.org/artists/peter-bradley/bio/)
- No Art Newspaper keyword page exists for him (404). Auction prices: none found.

### Quote
- Colour, "in his words 'supersedes subject'" — OPENED [Karma bio](https://karmakarma.org/artists/peter-bradley/bio/). A two-word quotation inside the gallery's text; no longer quote found.
- Checkable detail: he embeds "glass, flowers, and butterfly wings into acrylic" and exposes canvases to the weather — same source. Titles such as *Miles Ahead*, *Love Supreme*, *Sun Ra* and *Scrapple From The Apple* appear on the works page; the bio says he draws on "the improvisatory and responsive language of jazz".

### Gaps
- Which Bradley paintings hang in *Hard Art*. Auction data. A longer first-person quote.

---

## 7. William T. Williams

### Alive? Birth, residence, latest dated activity
- Born 17 July 1942, Cross Creek, North Carolina; no death date; article is in "Living people" — OPENED [Wikipedia](https://en.wikipedia.org/wiki/William_T._Williams)
- The Whitney lists "1942–" and the same birth date — OPENED [Whitney](https://whitney.org/artists/1428)
- "Williams lives in both New York City and Connecticut" — OPENED [Wikipedia](https://en.wikipedia.org/wiki/William_T._Williams)
- 2024 Murray Reich Distinguished Artist Award, New York Foundation for the Arts — same source.
- Latest dated activity: none on any page opened in this run. *Word of Eye* at Michael Rosenfeld Gallery (early 2026, dates conflicting between 7 Feb – 4 Apr and 19 Mar – 26 Apr) is SNIPPET; the gallery site would not open.

### Galleries
- Michael Rosenfeld Gallery as exclusive representative since 2016: SNIPPET. Wikipedia cites the gallery's artist page as a source, which is consistent — OPENED [Wikipedia](https://en.wikipedia.org/wiki/William_T._Williams)
- No Art Newspaper keyword page exists for him (404).

### Mailing address
- **Not verified on an official page.** SNIPPET: Michael Rosenfeld Gallery, 100 Eleventh Avenue at 19th Street, New York, NY 10011; tel 212.247.0082 — [Michael Rosenfeld](https://www.michaelrosenfeldart.com/about)
- New finding: `www.michaelrosenfeldart.com/contact` now redirects to `michaelrosenfeld.com/contact` (observed 16 Nov 2026). The gallery appears to have moved to the shorter domain, so the email info@michaelrosenfeld.com in the old notes is consistent with it rather than suspect.

### Works to see in New York
- *Drawing for an Epic Idea (Coonograph)*, 1970, pen and ink and watercolour on paper, sheet 17 1/2 × 23 in (44.5 × 58.4 cm). Whitney Museum, accession 71.47, "Purchase". **Not on view.** Image description: "Bright abstract painting with repeating fan and diamond shapes in red, pink, green, and blue" — OPENED [Whitney](https://whitney.org/collection/works/3333). It is the Whitney's only Williams and is a small drawing.
- MoMA acquired his painting *Elbert Jackson L.A.M.F., Part II* in 1969 — OPENED [Wikipedia](https://en.wikipedia.org/wiki/William_T._Williams) (secondary; MoMA page blocked, so medium, size and on-view status are UNVERIFIED).
- Whether he is in *Hard Art* at MoMA PS1: UNVERIFIED.
- Monograph: UNVERIFIED (gallery publications page not reachable).

### Market and institutions
- His 1971 first solo at Reese Palley Gallery "resulted in the sale of every painting"; work in more than thirty museum collections — OPENED [Wikipedia](https://en.wikipedia.org/wiki/William_T._Williams)
- Nothing on recent prices or museum shows since 2022 on any reachable page.

### Quote
- No quote about painting found. Nearest, on founding the Studio Museum's residency: "I wanted to create a context, namely an Artist-in-Residence program, through which money could be funnelled to artists" — OPENED [Wikipedia](https://en.wikipedia.org/wiki/William_T._Williams) (quoting a Studio Museum magazine piece; secondary).

### Gaps
- Official address; any 2026 dated activity read on a page; a painting viewable in New York; market; a quote about painting. Everything specific to the gallery waits on `michaelrosenfeld.com` being reachable.

---

## Deceased — Mary Heilmann

- Died 14 August 2026, aged 86; Wikipedia gives the place as Riverhead, New York — OPENED [Wikipedia](https://en.wikipedia.org/wiki/Mary_Heilmann)
- Gallery announcements and obituaries listed in the earlier notes are SNIPPET — [Hauser & Wirth](https://www.hauserwirth.com/news/in-memoriam-mary-heilmann-1940-2026/), [The Art Newspaper, 17 Aug 2026](https://www.theartnewspaper.com/2026/08/17/mary-heilmann-fearless-colourist-singular-painter-obituary)
- No letter. Jim Dine takes her place on the list.

---

## Cross-cutting notes

### Corrections to the earlier notes
- Dia Beacon's Pindell exhibition opens 30 January 2027, not December 2026.
- *Hard Art* at MoMA PS1 opened 5 November 2026; Pindell is in it, and Karma shows it on Bradley's page.
- Karma's addresses are 549 West 26th Street (NY 10001) and 38 White Street (NY 10013), not East 2nd Street.
- Pindell's Art Basel "Icon Artists" medal is confirmed by White Cube.
- Poons is listed by Almine Rech as one of its artists as well as by Yares.
- Katz's Musée Matisse show opened 28 October 2026 per Wikipedia.
- Dine is no longer with Pace or Gray; his current dealers are in Paris/Brussels and London.

### Inferences
- Three addresses are safe to write on an envelope today: Yares (Poons), Karma (Bradley), David Zwirner London or New York (Wylie). Pindell can go via White Cube New York if Garth Greenan's line cannot be confirmed.
- Katz, Williams and Dine still need an address read on an official page.
- No painting by any of the seven is confirmed on view in a Manhattan museum. The only current New York showing confirmed is *Hard Art* at MoMA PS1 (Pindell, Bradley).
- Market momentum can be inferred only from institutions: strongest for Pindell (Dia acquisition of 21 works, Art Basel medal) and Bradley (Whitney and LACMA purchases since 2022); no price evidence for anyone.

### Gaps
- Auction results and records for all seven: no reachable source.
- MoMA and Met collection pages for all seven: blocked by a browser check.
- Garth Greenan, Gladstone, Michael Rosenfeld, Templon and Cristea Roberts official pages: not reachable.
