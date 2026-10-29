# Brief 3: independent REVIEW of proposed new stories (read-only)

Project: /Users/mggmalang/gitlab/p2/allrepositories-ocms. Code baseline: working tree at commit the six commits listed in AGENT_BRIEF.md.
You did NOT write these proposals. Your job is to find what is wrong, overstated or missing in them, by reading the code yourself.
The proposals support a payment claim to URA: AN OVERCLAIM IS WORSE THAN A GAP. Do not defend the proposals; try to break them.

## Inputs (read these)
- /Users/mggmalang/gitlab/p2/allrepositories-ocms/docs/archify/new_stories.json : list of proposals; find yours by "id_proposed". Fields: en/id (title, user_story,
  adds, acceptance[], demo[], risks[], ura, points_basis), evidence[] (file:line), works, tier, kind, related (existing story id or ""), points, src.
- /Users/mggmalang/gitlab/p2/allrepositories-ocms/docs/archify/proposed/<ID>/<ID>.proposal.json : the traced steps (fit, code_ref, detail en/id), note, corrections.
- For kind "extension", the existing story text: python3 -I with openpyxl on /Users/mggmalang/gitlab/p2/allrepositories-ocms/UPLS-User-Story-Coverage.xlsx
  (sheet User Stories; columns: User Story, Points, 100% Billed, 50% Demo Billed, Status, Description, ...), and its trace docs/archify/<related>/<related>.trace.json.
- Existing stories are all 735 stories in docs/archify/_inputs/stories.json; use grep over their descriptions to see whether a proposal is already covered by a story text.

## What to check for EACH proposal assigned to you (use grep -n; BSD grep: word bounds are [[:<:]]word[[:>:]], never \b)
1. Every step in proposal.json: re-open the code_ref lines, read the condition that executes and decide whether the step's `fit`
   (Sesuai / Sebagian / Beda dari flow / Tidak ada code) is right. A step marked Sesuai that only has a name match, a comment, or a UI string without
   the server check is WRONG. Say what you read.
2. Every sentence of acceptance[], user_story, adds and risks[] in new_stories.json (English side is enough; the id side is a translation, but flag an
   Indonesian sentence whose meaning differs from the English one): is it true in the code? Quote the line that proves or contradicts it.
3. Every evidence[] file:line and every code_ref: does the file exist, is the line in range, does it show what is claimed?
4. Properties flags (application-uat/prod.properties) or environment switches that would switch the feature off.
5. Is it ALREADY covered by an existing story text (not just a trace)? For an extension, does `adds` really name something the related story text does NOT say?
   Could URA read this proposal as a second claim for something already billed (50% Demo Billed / 100% Billed columns)?
6. Is `works` (yes/partly) and `points` plausible compared with the similar existing stories (name the comparison)?
7. Anything important the proposal MISSES (a gap that makes the claim weaker) that you found while reading the code.

## Rules
- READ ONLY. Do not edit any file in the repo, do not run tools/evidence-xlsx/*.py, do not run visual-check, do not touch docs/archify.
- Write your findings ONLY to the scratchpad file named in your task (JSON), and send a short final message.
- Say plainly what you could not verify from the repo. Never invent a path, a line number or a quote.

## Result JSON (one file, a single object)
{ "reviewer_group": "...", "proposals": [ {
   "id": "OCMS52.N",
   "verdict": "OK" | "NEEDS FIXES" | "REMOVE OR REWRITE",
   "wrong_or_overstated": [ {"where": "acceptance[2] | step 4 | risks[1] | evidence[3] ...", "claim": "...", "finding": "what the code shows", "proof": "file:line", "suggested_fix": "..."} ],
   "missing_gaps": [ {"gap": "...", "proof": "file:line"} ],
   "already_covered_by": "existing story id or null, with the reason",
   "step_fit_changes": [ {"step": 3, "from": "Sesuai", "to": "Sebagian", "reason": "...", "proof": "file:line"} ],
   "points_view": "plausible | too high | too low, because ...",
   "could_not_verify": ["..."] } ] }
Final message to the parent (Indonesian, plain, English technical terms): per proposal the verdict and the 2-3 most important findings, nothing else.

## OCMS overrides (win over the text above)
- Existing stories: docs/archify/_inputs/stories.json (id, epic, points, status_with_ura, text). The related story trace is docs/archify/<related>/<related>.trace.json. Billing status = status_with_ura ("Paid", "Demo paid", ...); user_stories.xlsx has Billing remarks. Ignore every "UPLS-User-Story-Coverage.xlsx / Billed columns" wording above.
- Proposals: docs/archify/new_stories.json (find by id_proposed OCMS52.N) and docs/archify/proposed/OCMS52.N/OCMS52.N.proposal.json. The proposal.json `corrections` list was written by the tracer: check whether each correction is right and whether new_stories.json still has the wrong statement.
- Maintenance tickets: docs/archify/_inputs/maintenance_tickets.csv. A Closed, Prod deployed defect ticket on the feature means URA may consider it already paid as maintenance: say so.
- Rules of docs/archify/_inputs/AGENT_BRIEF.md and BRIEF_ADDENDUM.md apply (stale root cronservice/ copy never cited, prod-properties switch-off, cannot verify from repo).
- Write findings only to the scratchpad JSON file named in your task. Final message in Indonesian.
