# Brief: trace OCMS stories against code (read fully before starting)

You trace the stories you are given (a chunk of 1-5 stories, same epic) against the code and write evidence files. The result supports a payment claim, so **an overclaim is worse than a gap**. Code is evidence; story text, decks and spreadsheets are claims.

## Inputs
- Project root: /Users/mggmalang/gitlab/p2/allrepositories-ocms. Archify dir: docs/archify.
- Story data: docs/archify/_inputs/stories.json (id, epic, points, status_with_ura, text, demo_remark). Epic text: user_stories.xlsx column "Epics" (epic rows); stories.json is enough for the stories.
- Maintenance tickets (bugs and service requests raised after go-live): docs/archify/_inputs/maintenance_tickets.csv. grep it with keywords of your story (feature name, table, cron, report, notice type). A ticket is a hint that behaviour was wrong or changed after the baseline; read the code for the current behaviour and cite the ticket number (e.g. OCMS-DF-2026-074) in `detail` when it changes a verdict (for example an open defect on that step lowers Sesuai to Sebagian). It is not a requirement and not proof that code is right.
- Repos on main, read-only, never edit: ocmsadminapi e6f8cff6, ocmsadminprivateapi c5a2aa42, ocmsadminui 05f8d7de, ocmseserviceapi 7610c54, ocmseserviceui bdcdf28, thirdpartyapi 9c22a24. `code_commit` = all six joined by ", " (name:commit).
- Method and JSON shapes: ~/.claude/skills/story-evidence-report/SKILL.md section "1. Trace one story" and "Pitfalls". Finished OCMS examples: docs/archify/OCMS49.2/ (trace, sequence), plain/OCMS49.2.plain.json, en/OCMS49.2.en.json. Do NOT copy their facts.
- Diagrams: ~/.claude/skills/archify/SKILL.md (type sequence). Never run visual-check.

## Rules (all learned the hard way)
1. There is NO OCMS flow deck. Every step has flow_file exactly "User story (tidak ada di flow deck)" and slide "". Steps (5-15, never padded; a 1-point story may have 3-5) come from the story text. "Sesuai" therefore means: code does what the story text says.
2. Layer map: ocmseserviceui/ocmseserviceapi = Online Customer Portal (offender/public). ocmsadminui = staff portal UI, ocmsadminapi = staff API, ocmsadminprivateapi = intranet backend/cron/batch, thirdpartyapi = external agency interfaces. DB-side behaviour: look for entities, repositories, SQL, cron classes, properties.
3. Find candidates with `graphify query "..."` run inside a repo dir (graphify-out/graph.json exists), then READ the real code and take lines from `grep -n`. Judge by what a condition does, not by a method name, comment or UI string. Check properties files for flags; trust the properties file over a comment. Staff-side authorization may live only in the UI; check the server annotation before saying "role X only". Seeding that is off at startup means "data exists" is false on a fresh environment.
4. Fit per step, exactly one of: Sesuai, Sebagian, Beda dari flow, Tidak ada code. Evidence % = (Sesuai + 0.5 x Sebagian) / steps; recompute from your own file.
5. **Consistency**: a generic shared page/mechanism that exists but is not what the story names (for example the Payment page login when the story is about another service) is Sebagian at best, not Sesuai. Two steps that are the same fact in sibling stories get the same fit.
6. If the repo cannot prove it (Singpass, payment gateway, SFTP partner, per-environment property value, DB-only rows), write "cannot verify from repo" in `detail`; do not guess.
7. Status "User Story Removed" (status_with_ura in stories.json): still grep for code, write steps from the story text, fit Tidak ada code / Sebagian as found, recommendation "Tidak diklaim (Removed)", NO diagram (no sequence files, no html). Log similar code in the orphans file (type "Removed tapi mirip"). The verdict stays Removed even when code exists.
8. A story whose status is "No requirement" or blank is traced normally (say in `note` that the requirement is not given / status blank).
9. Do not claim from a comment; do not claim "not built" from one failed grep: try at least 3 synonyms/entity names and both layers (UI and API) before writing Tidak ada code.
10. Language: `detail` and `note` in Indonesian with English technical terms; `en/*.en.json` is a faithful full English translation (file names, file:line, identifiers unchanged); plain.json `en`/`id` max ~14 words, `why_*` only for non-Sesuai (max ~22 words), no file names or code words (server, API, endpoint, payload, table names); check en and id are not swapped. `code_ref` = full repo-relative path (starting with the repo folder) + `:line` or `:start-end`; every line must exist (check `wc -l`).

## Files you write (only these, only for your stories)
- docs/archify/<ID>/<ID>.trace.json, docs/archify/plain/<ID>.plain.json, docs/archify/en/<ID>.en.json
- unless Removed: docs/archify/<ID>/<ID>.sequence.json (EN) and <ID>.id.sequence.json (ID), then validate and deliver to <ID>.html and <ID>.id.html with the archify commands. archify only accepts meta.locale "en" or "zh-CN": use "en" in both specs, Indonesian labels in the .id one.
- docs/archify/_inputs/story_id/<ID>.json: {"<ID>": "<Indonesian translation of the story text, faithful, technical terms in English>"}
- docs/archify/_inputs/orphans/<FIRST_ID_OF_CHUNK>.json: list of {feature, source, story, type, verified, note, note_en} for code that exists but belongs to no story you were given, or Removed-but-similar code. [] if none. Never edit meta.json.
Never run build.py or build_index.py.

## Final answer (short, no essay)
Per story: id, steps by fit, Evidence %, one-line gap summary, maintenance tickets used (numbers), what you could not verify. Plus orphans count.
