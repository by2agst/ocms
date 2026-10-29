# Brief 2: trace one PROPOSED new story and draw its Archify diagram (proof for the claim)

Project: /Users/mggmalang/gitlab/p2/allrepositories-ocms. Code baseline: working tree at commit the six commits in AGENT_BRIEF.md (name:commit joined by ", ") (code_commit "the six commits in AGENT_BRIEF.md (name:commit joined by ", ")").
The proposals are in /Users/mggmalang/gitlab/p2/allrepositories-ocms/docs/archify/new_stories.json (a list; item "no" = N, "id_proposed" = OCMS52.N,
fields en / id hold the texts; "evidence" is a list of file:line, "related" is an existing story or empty). Read your item first.
The report supports a payment claim: AN OVERCLAIM IS WORSE THAN A GAP. Code is the evidence; say plainly when the repo cannot prove something.
Follow the method of /Users/mggmalang/.claude/skills/story-evidence-report/SKILL.md (section 1) and docs/archify/_inputs/AGENT_BRIEF.md + BRIEF_ADDENDUM.md (read it): steps, fit values, pitfalls, diagram rules.
Here there is no flow deck for the proposal: the "flow" is the proposal's own user story and acceptance list (judge the code against them). Mention in `detail`
where a URA deck or workbook sheet says something different (the item's `ura` text names them).

## What to do
1. Read your item. Re-open the evidence files at the given lines (get line numbers with grep -n; BSD grep: word bounds are [[:<:]]word[[:>:]], never \b).
   Trace the whole chain (UI route/menu -> API call -> service -> DB / job) and check properties files (application-uat/prod.properties) for flags.
2. Write 4-8 STEPS from the acceptance list (split or merge items so each step is one verifiable behaviour; do NOT pad with trivial steps to raise the
   percentage; every acceptance item must be covered). Judge each step honestly:
   - "Sesuai"   : the code does exactly what the step says (you read the condition that executes);
   - "Sebagian" : it does part of it, or only under conditions (empty seed data, flag, only one path...);
   - "Beda dari flow": the code does something different;
   - "Tidak ada code": nothing does it.
   If an acceptance statement in new_stories.json turns out wrong or too strong, mark the step accordingly and list it under `corrections` (the parent will fix the item).
3. Write ONE file: /Users/mggmalang/gitlab/p2/allrepositories-ocms/docs/archify/proposed/OCMS52.N/OCMS52.N.proposal.json (create the folder):
   {
    "id": "OCMS52.N", "code_commit": "the six commits in AGENT_BRIEF.md (name:commit joined by ", ")",
    "steps": [ {"step": {"en": "...", "id": "..."}, "fit": "Sesuai", "code_ref": "path/from/repo/root.ext:line",
                "detail": {"en": "what the code does, with the condition you read", "id": "same in Indonesian"}} ],
    "note": {"en": "gaps and what is not provable from the repo", "id": "..."},
    "corrections": ["statements in new_stories.json that must change, or []"]
   }
   Language: "en" fields English; "id" fields natural Indonesian (relaxed, plain), keeping file names, identifiers, quoted UI strings and technical terms
   (endpoint, job, flag, payload...) in English. code_ref: full repo-relative path and :line (a range like :10-20 is fine), no "...", one or two refs per step.
4. Draw the Archify sequence diagram (type sequence) from what the code does INCLUDING the gaps. Use the archify skill at /Users/mggmalang/.claude/skills/archify
   (read its SKILL.md; run node commands from that directory with absolute paths). Write two specs next to the proposal file:
   OCMS52.N.sequence.json (English, meta.locale "en") and OCMS52.N.id.sequence.json (Indonesian, no locale; keep identifiers/endpoints as is).
   Shape (same as docs/archify/OCMS49.2/OCMS49.2.sequence.json and its .id twin: copy their structure): <= 6 participants, <= 12 messages, viewBox [1080, ~620],
   column_fit "spread", quality_profile "showcase", message y >= 160, <= 520 and >= 30 apart, three segments, three cards (emerald = what matches,
   rose = gap, orange = to verify), taken from YOUR steps, not invented. Then from the archify dir:
     node bin/archify.mjs validate sequence <spec> --quality showcase --json
     node bin/archify.mjs deliver  sequence <spec> <out.html> --quality showcase --json
   Outputs: OCMS52.N.html (EN) and OCMS52.N.id.html (ID) in the same folder. NEVER run visual-check. If NO step has code at all (all "Tidak ada code") skip the diagram and say so.
5. Do NOT modify anything else: not new_stories.json, not docs/archify/*.json, not any repo source, not the xlsx/index, and do not run tools/evidence-xlsx/*.py.
   Other agents trace the other proposals in parallel; write only inside docs/archify/proposed/OCMS52.N/.

## Final message to the parent (Indonesian, plain, English technical terms)
Evidence percent computed from your steps ((Sesuai + 0.5 x Sebagian) / steps) with the counts; what is not proven by the repo; the `corrections` list;
files written; one line confirming the diagram validate/deliver result. Do not paste the JSON.

## OCMS overrides (win over the text above)
- Repos: ocmsadminapi, ocmsadminprivateapi, ocmsadminui, ocmseserviceapi, ocmseserviceui, thirdpartyapi under /Users/mggmalang/gitlab/p2/allrepositories-ocms. Cite only ocmsadminprivateapi/src/main/java (never the stale root cronservice/ copy). `code_commit` field = all six "name:commit" joined by ", " as in AGENT_BRIEF.md.
- Reference diagram shape: docs/archify/OCMS49.2/OCMS49.2.sequence.json and its .id twin.
- Rules of AGENT_BRIEF.md + BRIEF_ADDENDUM.md apply (fit values, prod-properties switch-off convention => Sebagian, "cannot verify from repo", unique scratch names containing your first id).
- The proposal list is docs/archify/new_stories.json (item "no" = N, "id_proposed" = OCMS52.N). The "ura" text is "no (no flow deck exists in repo)" or a ticket hint; tickets are in docs/archify/_inputs/maintenance_tickets.csv.
- Write only inside docs/archify/proposed/OCMS52.N/ for your assigned N. Do not edit new_stories.json (put wrong statements under `corrections`). Never run build.py/build_index.py/visual-check.
