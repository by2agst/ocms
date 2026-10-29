# Brief: code that exists but is not in any user story (candidates for NEW stories)

Project: /Users/mggmalang/gitlab/p2/allrepositories-ocms (OCMS, URA). Six repos on main: ocmsadminapi e6f8cff6, ocmsadminprivateapi c5a2aa42, ocmsadminui 05f8d7de, ocmseserviceapi 7610c54, ocmseserviceui bdcdf28, thirdpartyapi 9c22a24.
Why: the boss wants to claim money from URA for work that was built but never covered by a user story. The report
supports a payment claim, so an OVERCLAIM IS WORSE THAN A GAP. Code is the evidence; say plainly when the repo cannot prove something.

## Hard rules
1. DO NOT modify anything under docs/archify (existing stories, traces, plain, en, meta, index, xlsx) or any repo source file.
   Write ONLY your own result file (path given in your task) under the scratchpad directory. Existing stories stay exactly as they are.
2. A candidate is a FEATURE someone can see or use (a screen, a report, an e-mail/SMS the system sends, a scheduled job with a visible result,
   an admin function). Not a candidate: dead code with no caller, generated per-table CRUD, diagnostics, stale comments, leftovers of removed
   stories (special use, admin fee, Workday, GIRO...), unfinished half-features that do not work, bugs/gaps. Put those in `not_claimable` with the reason.
3. For every candidate decide `kind`:
   - "new": no existing story covers it.
   - "extension": it extends an existing story (give that story ID in `related_story`; read docs/archify/<ID>/<ID>.trace.json and the story row
     in UPLS-User-Story-Coverage.xlsx via python3 -I openpyxl to see what the old story covers). The old story is NOT changed; the extension is
     described as additional scope that the old story text does NOT cover (so it cannot be read as a double claim).
   - A story already marked Covered/billed (100% Billed / 50% Demo Billed columns) must not be re-claimed: if the feature is already inside the
     story text, it is not a candidate at all.
4. Find out whether URA asked for it: grep docs/planning/flow-decks/*.md and docs/planning/flow-decks/Admin_workflow_revised.xlsx
   (python3 ~/.claude/skills/markitdown-docs/docmd.py <file>, then slice) for the feature. Set `ura_requested`: "workbook" (sheet name), "deck" (file + slide),
   or "no" (and say it was not found). A feature URA never asked for is weaker; say so.
5. Prove it works from code: follow UI route -> API call -> service -> DB. Get `file:line` from grep -n (BSD grep: word bounds are
   [[:<:]]word[[:>:]], never \b). Check environment flags in application-uat/prod.properties (a feature switched off is NOT claimable as working).
   Check whether the menu/route is reachable (menu entry? role?). Label `works`: "yes" / "partly" / "no" / "cannot verify from repo".
6. Existing stories to compare with: all 120 are in UPLS-User-Story-Coverage.xlsx; their traces are docs/archify/UPLS*/UPLS*.trace.json, descriptions
   in docs/archify/story_id.json (Indonesian) and the coverage sheet (English). Already-registered orphans are in docs/archify/meta.json ("orphans"):
   read it first; reuse those findings (do not rediscover) and mention the existing orphan number/feature when it overlaps.
7. Language: write all free text in ENGLISH (the report is bilingual; I translate). Plain wording, no marketing words. Keep identifiers/paths as is.
8. Points: suggest a story point using the same scale the project uses (2, 3, 5, 8, 13, 21, 34) and explain the comparison in `points_basis`
   by naming an existing story of similar size (e.g. Block Parking UPLS13.3 = 13, Purpose of Use UPLS13.6 = 21, Approval Matrix UPLS13.1 = 21,
   Report builder stories 5-13). Mark it as an estimate; it is MGG's and URA's decision, not a fact from the code.
9. Never invent: no made-up file paths, line numbers or quotes. If unsure, say "cannot verify from repo".

## Result JSON (one file per task, a single JSON object)
{
 "cluster": "<name>",
 "candidates": [
  {
   "id": "<short slug>",
   "title": "<feature name, English>",
   "kind": "new" | "extension",
   "related_story": "UPLSx.y or null",
   "related_note": "what the old story covers and what this adds (English), null if kind=new",
   "user_story": "As a <role>, I want <capability>, so that <benefit>.",
   "acceptance": ["3-6 short verifiable behaviours, each something that exists in code"],
   "evidence": [{"repo": "...", "file_line": "path:line", "what": "..."}],
   "works": "yes|partly|no|cannot verify from repo",
   "works_basis": "why you believe that (flags, reachable menu, tests, etc.)",
   "ura_requested": "workbook: <sheet> | deck: <file #slide> | no",
   "points": 5, "points_basis": "...",
   "demo_steps": ["how a reviewer can see it work in UAT (not verified by us)"],
   "risks": ["why URA might refuse / what we cannot prove"],
   "confidence": "High|Medium|Low"
  }
 ],
 "not_claimable": [{"item": "...", "source": "file:line or screen", "reason": "dead|diagnostic|generated CRUD|leftover of removed story|bug or gap|not reachable|switched off|other"}],
 "notes": "anything the parent must know"
}
Final message to the parent (Indonesian, plain, English technical terms): how many candidates (new vs extension), the strongest 3 with one line why,
what is NOT claimable, what you could not verify, and the path of your result file.
