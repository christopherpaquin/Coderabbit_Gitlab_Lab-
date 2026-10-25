# Worklog

## 2026-10-24 19:34
**Task:** Build a repo-local CodeRabbit and GitLab learning lab from the original plan.
**Decision:** Keep main safe and reproducible: clean baseline samples plus explicit lab patches, an answer key, and generic tunnel documentation that uses the existing gitlab.lab remote without publishing private credentials or tunnel identifiers.
**Why:** CodeRabbit reviews merge request diffs, so the planted defects must be introduced on lab branches. The repository already has detect-secrets hooks, and the future blog should not accidentally disclose private infrastructure.
**Progress:** in-progress; README, samples, lab patches, and verification remain.

## 2026-10-24 19:37
**Task:** Complete verification for the CodeRabbit/GitLab learning lab.
**Decision:** Fixed the planted patch hunk count, added a narrow detect-secrets allowlist to the fake password, and expanded the answer key to distinguish additional valid shell findings.
**Why:** The final review correctly identified that the patch must apply cleanly and remain compatible with the repository hygiene hooks; otherwise the first CodeRabbit experiment would fail before review.
**Progress:** complete; pre-commit, Markdown link checks, clean-sample syntax checks, patch application in an isolated copy, and patched-sample syntax/security-hook checks passed.

## 2026-10-24 19:38
**Task:** Finalize the publishable CodeRabbit/GitLab lab documentation and sample artifacts.
**Decision:** Kept the LAN hostname as environment-specific setup context, but separated it from the public blog guidance; kept planted warnings out of the code under review so the baseline measures CodeRabbit more honestly.
**Why:** The lab should teach review judgment rather than pre-label every defect, while still warning users not to execute the intentionally unsafe patch. The answer key now scores the dropped destination/relative-path behavior explicitly.
**Progress:** complete; final pre-commit, diff, patch-apply, syntax, and detect-secrets checks passed after the last documentation and patch edits.

## 2026-10-25 12:43
**Task:** Apply the provider-neutral README redesign in the publishable GitHub clone.
**Decision:** Keep the GitHub clone synchronized with the LAN checkout at the README level while retaining the GitHub remote for publication.
**Why:** Readers should receive the same teaching material regardless of whether they start from the GitHub copy or the local GitLab copy.
**Progress:** in-progress; README updated, validation and commit/push remain.

## 2026-10-25 12:45
**Task:** Improve README visual hierarchy and discoverability in the GitHub copy.
**Decision:** Use compact factual badges, an at-a-glance table, collapsible contents, and focused callouts while preserving the teaching content.
**Why:** A long lab guide should be easy to scan in both GitHub and GitLab interfaces without adding decorative or unsupported claims.
**Progress:** in-progress; README updated, validation and commit/push remain.

## 2026-10-25 12:54
**Task:** Split the CodeRabbit/GitLab lab guide into navigable sub-pages in the GitHub copy.
**Decision:** Keep the GitHub README as the overview and add numbered lab pages with exact commands, GitLab UI steps, screenshot checkpoints, cleanup, and navigation.
**Why:** The public copy needs to be independently usable and ready to receive screenshots as the learner progresses.
**Progress:** in-progress; pages are synchronized, validation and commit/push remain.

## 2026-10-25 12:55
**Task:** Make the public lab procedures executable rather than conceptual.
**Decision:** Added copyable pre-merge configuration, a minimal GitLab CI pipeline, and a disposable security sample with exact commands.
**Why:** The GitHub copy must let a learner follow each lab without guessing what file to create or what UI state to reach.
**Progress:** in-progress; detailed pages synchronized, final validation and commit/push remain.
