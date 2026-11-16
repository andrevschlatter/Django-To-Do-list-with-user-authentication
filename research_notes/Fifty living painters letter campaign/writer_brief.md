# Writer brief (shared by all letter writers)

## Who is writing the letters (use his own words; do not embellish his life)
- Lives in New York. Works in finance. Grew up in Toledo, Ohio, one of four brothers.
- His mom makes jewelry and used to take him to the Toledo Museum of Art ("great museum there").
- Why Basquiat, in his words: "big, colorful and bold".
- What happens in front of a painting, in his words: "It puts me in a creative frame of mind more than anything. A lot of architecture, fashion etc. is boring, but great art helps me think creatively."
- Recently inspired: spending more time at MoMA, the Met and galleries.
- No art on his walls right now.
- Lives in NYC and would travel to a studio if invited.
- DO NOT mention: wanting to paint, auction houses, anything about buying strategy.
- He has probably NOT seen these works in person. Never invent a sighting. Be honest about how he met the work: in a book, on the museum's or gallery's website, in a reproduction. EXCEPTION: if the notes show the work is viewable in New York right now or permanently (a current gallery show, a subway/public commission, a show open into 2027), the letter may say he went to see it, and you must set SEE_BEFORE_MAILING: yes so he actually goes first.
- Toledo Museum facts are in toledo_museum.md (search-summary level). The museum's galleries are closed for reinstallation until fall 2027, so never say a work "hangs" there now. Where the notes show the Toledo museum owns a work by this artist, that is a natural, true thing to mention ("the museum I grew up going to owns your ..."), phrased as ownership, not as something he saw, and only if the notes support it.

## Letter rules (hard)
1. Under one handwritten page: 110-180 words in the body. Plain American English ("colorful"). Short sentences. No em dashes, no semicolons, no bullet points, no exclamation marks.
2. Unmistakably about this one artist and ONE named work (title and year), with the concrete visual detail from the notes. If the detail in the notes is flagged as machine-generated alt text or unverified, use only what is safe (title, year, size, medium, colors named in a curator description) and add a CHECK note.
3. Ask for nothing. No questions that need an answer, no request for a reply, a signature, a meeting, advice or a response.
4. Never mention collecting, collectors, value, price, market, auction, investment, "acquire", "portfolio", or his budget.
5. Open exactly ONE door, once, lightly, as a hope and not a request: EITHER that he'd love to see the studio someday, OR that he hopes to own a print or small piece when he's able. Never both. Alternate between the two across your ten letters (five each). The door sentence should not be the last sentence of the letter.
6. The first sentence must start from the work itself or a specific moment with it, not from himself as a fan. Never open with "I am writing", "My name is", "I'm a big fan", "I hope this letter finds you", or "Dear X, I". The first sentence must name or describe something only this artist's work has.
7. The last sentence (before the sign-off) must also contain something specific to this artist or work, so it could not close any other letter.
8. No flattery or template language: no "genius", "master", "legend", "icon", "incredible", "amazing", "inspiring", "your work speaks to me", "I've always admired", "truly", "deeply", "resonates", "testament", "vibrant", "captivating". Say what he noticed and what it did to his thinking. One true, specific observation beats three compliments.
9. Use his biography sparingly and differently each time: at most one or two personal facts per letter (Toledo, mom's jewelry and the museum trips, four brothers, finance job, bare walls, living in New York), and not the same combination in consecutive letters. Some letters should carry no biography beyond one clause.
10. Do not explain the artist's work back to them, do not summarize their career, do not quote their own interviews at them. Do not mention Basquiat unless the notes document a real personal connection AND it is said in passing; never compare the artist to Basquiat.
11. Do not mention other artists on his list, or that he is writing to many artists.
12. Salutation "Dear Mr./Ms. Surname," is wrong for artists whose pronouns/titles are not established: use "Dear <First name Last name>,". Sign-off: vary it simply ("Sincerely," "With thanks," "Yours," "Best,") followed by "[Your name]" on its own line. No return-address or contact line in the body.
13. After drafting, reread each letter as the artist would, at the end of a studio day, and cut every sentence that could have been sent to someone else.

## Facts and sourcing rules for the dossier
- Use only facts in the notes files. Carry the source URL with every fact. Mark each fact OPENED or SNIPPET exactly as the notes do. Never add facts from memory. If the notes lack something, write "not found".
- Market notes go ONLY in the MARKET_NOTE field, never in the letter.

## Output format (exact; one block per artist, in the order given to you)
```
## ARTIST: <name>
WEEK: <n>
CATEGORY: <older artist | Basquiat's circle | blue-chip | mid-career>
ALIVE: <one line of evidence> [URL]
GALLERY: <primary gallery; other galleries>
MAIL_TO: <single-line postal address, starting "<Artist name>, c/o ...">
ADDRESS_STATUS: <"Verified on official page" + URL | "UNVERIFIED: check by hand" + reason + the page to check>
WORK: <title, year, medium, size; where it is or which book> [URL]
VISUAL_DETAIL: <the detail used in the letter> [URL] <CHECK note if weak>
WORK_2: <optional second work, same form, or "none">
SEE_BEFORE_MAILING: <yes: where and until when | no: met in reproduction>
DOOR: <studio | print or small piece>
MARKET_NOTE: <3-6 lines: price range, record, recent results, museum acquisitions/shows, verdict rising/stable/cooling, with URLs and OPENED/SNIPPET tags and "thin evidence" where true>
FLAGS: <anything he must know before mailing, or "none">
LETTER:
<<<
<letter text>
>>>
```
