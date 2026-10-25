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

## 2026-10-25 12:55
**Task:** Resolve repository secret scanning on the new Lab 8 documentation in the GitHub copy.
**Decision:** Construct the fake token prefix in the disposable sample instead of storing a token-shaped literal in tracked documentation.
**Why:** The public lab should teach secret detection without committing a credential-like string that blocks repository hygiene hooks.
**Progress:** in-progress; corrected pages are synchronized, commits and pushes remain.

## 2026-10-25 13:06
**Task:** Clarify the canonical GitHub template versus learner-owned GitLab working clone.
**Decision:** Lab 0 now creates coderabbit-gitlab-lab-clone, installs CodeRabbit there, clones it locally, verifies the GitLab remote, and runs the smoke-test MR there. Every later lab has a working-directory preflight.
**Why:** The public instructions must distinguish the GitHub source repository from the learner workspace where CodeRabbit experiments occur.
**Progress:** in-progress; documentation synchronized, validation and commits remain.

## 2026-10-25 19:06
**Task:** Clarify exactly where and how learners install CodeRabbit.\n**Decision:** Lab 0 now distinguishes the GitHub template, the GitLab working project, and the local clone; it gives separate GitLab.com and self-managed onboarding paths and uses the public HTTPS URL for CodeRabbit while retaining the LAN SSH remote for Git operations.\n**Why:** The previous instruction did not tell the learner which project to connect, which URL to enter, or how self-managed onboarding relates to the Git remote.\n**Progress:** in-progress; clarified Lab 0 synchronized, validation and commits remain.

## 2026-10-25 19:08
**Task:** Add the learner-provided Lab 0 screenshot at checkpoint 0.1.\n**Decision:** Store the GitLab Create blank project screenshot at assets/screenshots/lab-00-01-create-project.png and embed it directly below the 0.1 placeholder in Lab 0.\n**Why:** The image documents the exact project-creation screen and clarifies the blank-project path while leaving the import path available for readers using GitLab project import.\n**Progress:** in-progress; screenshot and documentation synchronized, validation and commits remain.

## 2026-10-25 19:08
**Task:** Add the learner-provided Lab 0 screenshot at checkpoint 0.2.\n**Decision:** Store the working-project screenshot at assets/screenshots/lab-00-02-working-project.png and embed it below the 0.2 placeholder.\n**Why:** The image demonstrates the learner-owned GitLab project and its imported lab contents, making the separation from the GitHub template concrete.\n**Progress:** in-progress; screenshot and documentation synchronized, validation and commits remain.

## 2026-10-25 19:14
**Task:** Add Lab 0 screenshot 0.4 and clarify CodeRabbit repository installation versus review settings.\n**Decision:** Treat the supplied CodeRabbit Review settings screen as evidence that coderabbit-gitlab-lab-clone is already connected; direct learners to Connected repositories for adding projects and Review settings for configuring connected projects.\n**Why:** The screenshot shows the repository selected and the Connected repositories breadcrumb, but the previous lab wording did not distinguish installation from post-installation configuration.\n**Progress:** in-progress; screenshot and documentation synchronized, validation and commits remain.

## 2026-10-25 19:15
**Task:** Correct Lab 0 terminology and add the repository-installation step.\n**Decision:** Treat Connected repositories as access visibility, not installation. Lab 0 now requires selecting coderabbit-gitlab-lab-clone, choosing Sync Repositories, and waiting for Installed before continuing.\n**Why:** The supplied CodeRabbit screen showed the project as Uninstalled, proving that the previous documentation incorrectly treated repository visibility as review enablement.\n**Progress:** in-progress; screenshot 0.5 and corrected instructions synchronized, validation and commits remain.

## 2026-10-25 19:16
**Task:** Add Lab 0 screenshot 0.6 for the CodeRabbit installation confirmation dialog.\n**Decision:** Place the screenshot between repository synchronization and installed-state verification, then renumber later checkpoints so the installation sequence is explicit.\n**Why:** The dialog is the actual user action that changes coderabbit-gitlab-lab-clone from visible in Connected repositories to installed for reviews.\n**Progress:** in-progress; screenshot and documentation synchronized, validation and commits remain.
