# Brief: evidence ledger for proposed new stories (verbatim quotes, adversarial)

Project root /Users/mggmalang/gitlab/p2/allrepositories-ocms, archify dir docs/archify. Six repos on main (commits in docs/archify/_inputs/AGENT_BRIEF.md). Read AGENT_BRIEF.md and BRIEF_ADDENDUM.md first for the rules (cite only src/main/java, never the stale root `ocmsadminprivateapi/cronservice/`; switched-off-in-prod = Sebagian; "cannot verify from repo").

The proposals support a payment claim: AN OVERCLAIM IS WORSE THAN A GAP. You are the second, independent check. Earlier agents already traced and reviewed; do NOT trust them. Your job is to make every claim PROVABLE by quoting the code.

## Inputs
- docs/archify/new_stories.json : find your item by `id_proposed` (en/id user_story, acceptance[], demo[], risks[], adds, evidence[], points, works, tier, kind, related).
- docs/archify/proposed/<ID>/<ID>.proposal.json : traced steps (fit, code_ref, detail), note.
- docs/archify/_inputs/stories.json (existing stories, status_with_ura), maintenance_tickets.csv.

## What to do for EACH proposal assigned to you
1. For EVERY acceptance[i] (en) and EVERY step in proposal.json: open the cited file, read around the cited lines, and copy ONE verbatim code line (or property line) that proves the claim (max 160 chars, exactly as in the file, no paraphrase) with its exact file path and line number. Use `sed -n 'Np' file` or `grep -n` to get the real line; the quote must be found at exactly that line number (you will be machine-checked).
2. Classify each acceptance/step: `proved` (the quote shows the executing condition), `partly` (quote proves only part; say what is missing), `not_proved` (cannot find proof, or code contradicts it: quote the contradicting line), or `cannot_verify_from_repo`.
3. For each `not_proved`/`partly` write the exact corrected wording (en) that WOULD be provable; the parent will apply it.
4. Check the fit of every step again (Sesuai only if you quoted the line that executes the behaviour; UI string or comment alone is NOT proof) and state `fit_ok` true/false with your proposed fit.
5. Overlap: for the proposal, read the 3 most similar existing stories the parent lists in your task and say whether URA could read the proposal as a second claim (yes/no/maybe + reason).
6. Check `works` and the prod/uat property flags that gate the feature (quote the property line).

## Output (only these files; do not edit anything else)
Write docs/archify/proposed/<ID>/<ID>.evidence.json :
{ "id": "OCMS52.N", "checked_by": "ledger-<your group>",
  "acceptance": [ {"i":0,"claim":"<acceptance text>","status":"proved|partly|not_proved|cannot_verify_from_repo","file":"repo/path.ext","line":123,"quote":"verbatim line","missing":"","fix_en":""} ],
  "steps": [ {"i":0,"fit_in_file":"Sesuai","fit_ok":true,"proposed_fit":"Sesuai","file":"...","line":123,"quote":"verbatim line","note":""} ],
  "flags": [ {"file":"...","line":1,"quote":"cron.x.enabled=true","meaning":""} ],
  "overlap": [ {"story":"OCMSx.y","status":"...","second_claim_risk":"yes|no|maybe","reason":""} ],
  "verdict": "SOLID | FIX WORDING | WEAK" }
Never invent a path, line number or quote. If the claim has no provable line, say not_proved.
Final message to the parent (Indonesian, short, English technical terms): per proposal: verdict, count proved/partly/not_proved, and the acceptance/step wording that must change.
