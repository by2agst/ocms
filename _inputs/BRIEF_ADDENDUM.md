# Addendum to AGENT_BRIEF.md (facts verified in double check; read before tracing)

1. ocmsadminprivateapi/cronservice/ at the repo root is a STALE uncompiled copy. Cite only ocmsadminprivateapi/src/main/java/... and src/main/resources/...
2. Use unique scratch file names (include your first story id); other agents share the scratchpad.
3. Removed stories: every step that has code is Sebagian, never Sesuai; no diagram.
4. Convention for "code exists but is switched off by repo config": if the step's own execution is switched off in the prod properties (cron enabled=false, sms.enable=false, email.enableSmtp=false, sftp.upload.disabledServers=toppan, ...), the step is Sebagian and `detail` says which property and file:line. State the property value; say the real server value cannot be verified from the repo.
5. Facts already verified in code, do not re-derive or contradict without new evidence:
   - ToppanUploadJobsScheduler.executeDayEndJobs: the call toppanLettersGeneratorService.executeJob() is commented out (line ~119). The 00:15 schedule exists but letter generation only runs through the manual trigger POST /toppan/generate-letters. A step that says "the cron generates the letters daily" is at most Sebagian.
   - ToppanUploadJob.confirmDeliveryAndAdvanceStage: while sftp.upload.disabledServers=toppan the delivery gate is bypassed and the stage still advances without delivery (OCMS-DF-2026-192).
   - NotificationSmsEmailHelper skips the EMAIL channel for stages DN1, DN2 and DR3 ("no template available").
   - NotificationSmsEmailHelper.loadAllExcludedIds returns an empty set when the read fails (fail-open); refreshContactInfo runs for all records before the exclusion gate in NotificationSmsEmailJob.
   - ToppanUploadHelper.resetLetterAddressAfterToppan fallback chain is mha_reg -> lta_reg -> lta_mail and omits furnished_mail (possible bug for hirers with only a furnished address).
   - JwtFilter (ocmsadminapi) skips JWT for plus-* and webhook endpoints; protection depends on APIM, not visible in the repo.
   - OCMS_REPORT_REMINDER has no /v1/download/blob; OCMS_REPORT_DH_FIN and OCMS_REPORT_DH_UEN have no mapping in api-authorization.properties.
   - The business term "DOS" is not implemented as an integration in the backend code. The only occurrence is a staff UI screen "DOS Reports" (ocmsadminui/src/pages/Report/lists/ReportListDOS.tsx:82, resource `dosvaultrecords`) with no controller or authorization mapping in any repo. When a story names DOS, say "DOS = DataHive/LTA cannot be confirmed from the repo" and do not claim DOS code exists.
6. Plain files: `en` must be English and `id` Indonesian, never swapped; recheck by reading two entries before finishing.
