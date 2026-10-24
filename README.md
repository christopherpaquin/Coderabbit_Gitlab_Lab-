# CodeRabbit + GitLab learning lab

This repository is a small, repeatable lab for learning two things at once:

1. How GitLab merge requests, branches, webhooks, permissions, and CI fit together; and
2. How CodeRabbit reviews code, explains findings, remembers team preferences, and proposes changes.

Each lab gives you a controlled experiment, an observation checklist, you can used with a with a self-managed GitLab instance.

## The short version

You create a branch, make a deliberately small change, push it to the local GitLab, and open a merge request (MR). CodeRabbit reviews the MR diff and posts a walkthrough plus findings as `@coderabbitai`. You inspect whether the review is accurate, reply to it, change the code or configuration, push again, and compare the next review.

CodeRabbit is the reviewer under test; GitLab is the system under test. Your job is not to make the sample code production-ready immediately. Your job is to measure what the tool notices, what it misses, how much noise it creates, and whether its suggested fixes are safe to accept.

## What CodeRabbit is doing

For an MR, CodeRabbit generally combines the diff with repository context, configuration, coding guidelines, and available static-analysis results. It then posts review output back to GitLab. Depending on the connected workspace and plan, that output may include:

- a high-level walkthrough and change summary;
- inline findings with severity and suggested fixes;
- pre-merge checks and merge-risk signals;
- replies to questions in MR discussions;
- incremental reviews after new commits; and
- finishing actions such as fixing comments or generating tests.

Treat all of these as hypotheses to evaluate. Product features, limits, command names, and plan entitlements can change, so the official documentation is the source of truth:

- [Self-managed GitLab](https://docs.coderabbit.ai/platforms/self-hosted-gitlab)
- [Review commands](https://docs.coderabbit.ai/reference/review-commands)
- [YAML configuration](https://docs.coderabbit.ai/getting-started/yaml-configuration)
- [Code guidelines](https://docs.coderabbit.ai/knowledge-base/code-guidelines)
- [Pre-merge checks](https://docs.coderabbit.ai/pr-reviews/pre-merge-checks)
- [CLI](https://docs.coderabbit.ai/cli)
- [Plans and pricing](https://docs.coderabbit.ai/management/plans)

## Environment: local GitLab plus a Cloudflare Tunnel

This checkout currently uses the LAN GitLab remote:

```text
git@gitlab.lab:ae35/ae35.git
```

Keep using that remote for clone, fetch, and push. The remote is for your workstation-to-GitLab traffic; it is not the address CodeRabbit uses to reach the server.

The expected integration path is:

```text
workstation --SSH/Git--> gitlab.lab (LAN GitLab)
                              ^
                              | GitLab webhooks/API through public HTTPS
CodeRabbit cloud <--- Cloudflare Tunnel / edge hostname
```

The tunnel must expose the GitLab web/API endpoints CodeRabbit needs through a stable HTTPS hostname. Do not put tunnel IDs, API tokens, PATs, IP addresses, or Access bypass details in this repository or in a public blog draft. Record only whether the check passed and keep operational secrets in your existing local credential store.

### One-time setup checklist

1. Confirm the checkout and remote:

   ```bash
   git remote -v
   git status
   ```

2. In GitLab, create or select the project that will host this lab. This repository is already the project for the exercises; do not create a second project unless you want a clean trial.

3. Add the CodeRabbit GitLab user to the project with the minimum role the current CodeRabbit onboarding requires. Confirm the account can read the repository and participate in MRs.

4. Complete the CodeRabbit self-managed GitLab onboarding in the CodeRabbit UI. Use the public HTTPS hostname that fronts GitLab through the tunnel. Do not substitute `gitlab.lab` for that hostname: CodeRabbit's cloud cannot resolve your LAN-only name.

5. Check the project's GitLab webhook page after installation. A successful recent delivery is more useful than assuming that the integration is installed.

6. Check the tunnel and public GitLab URL from a network that is not your LAN. If the public URL cannot load the GitLab sign-in page, stop there and repair the tunnel/edge policy before debugging CodeRabbit.

7. Review billing and usage settings before running many experiments. Do not assume that a trial, free tier, usage-based reviews, or rate limit is identical to the plan described in an older guide.

### Credentials and safety

- Use a dedicated GitLab identity or bot credential for the integration when possible.
- Give tokens only the scopes and project access the current onboarding requires; record the scopes you chose in your private notes.
- Never commit a PAT, OAuth secret, webhook secret, Cloudflare token, private key, or real customer data.
- The sample changes are intentionally flawed. Do not run them against a real backup source, production database, or network service.
- The repository already has pre-commit and `detect-secrets` hooks. Keep them enabled and do not bypass them with `--no-verify`.

## Repository map

```text
README.md                         this guide and experiment log template
samples/backup.sh                 safe baseline for the shell lab
samples/users.py                  safe baseline for the Python lab
samples/README.md                 warnings and sample usage
labs/answer-key.md                planted issues; read only after reviewing an MR
labs/patches/lab-01-planted-bugs.patch
                                  turns the clean samples into the baseline challenge
.coderabbit.yaml.example          starter configuration for Lab 4
```

The `main` branch is intentionally safe. The first review challenge is a patch you apply on a temporary branch, so CodeRabbit sees the vulnerable edits in an MR while the repository's default branch remains usable. Read the answer key only after recording your own findings.

## Start here: Lab 0, integration smoke test

Before testing review quality, prove that the plumbing works.

```bash
git switch main
git pull --ff-only
git switch -c lab0-smoke
printf '\nSmoke-test change for CodeRabbit.\n' >> README.md
git add README.md
git commit -m "test: verify CodeRabbit integration"
git push -u origin lab0-smoke
```

Open an MR from `lab0-smoke` into `main`. Confirm that:

- GitLab accepts the push and creates the MR;
- a webhook delivery appears in the project settings;
- CodeRabbit comments on the MR; and
- the comment is from the expected CodeRabbit account.

Delete or close the smoke-test MR after recording the time from push to review. If no review appears, use the troubleshooting section before proceeding.

## Lab 1: baseline review with planted defects

This is the control experiment. Apply the patch on a new branch; do not run the resulting files.

```bash
git switch main
git pull --ff-only
git switch -c lab1-planted-bugs
git apply labs/patches/lab-01-planted-bugs.patch
git diff --check
git add samples
git commit -m "test: add planted CodeRabbit review findings"
git push -u origin lab1-planted-bugs
```

Open an MR into `main`. Before reading `labs/answer-key.md`, record:

- time from push to first review;
- number of walkthrough, actionable, and nitpick comments;
- which shell and Python issues were found;
- whether tool attribution appears (for example, ShellCheck or Ruff);
- whether the dangerous interaction between `cd`, `tar`, and `rm -rf` was explained;
- whether the summary describes intent rather than only filenames; and
- whether each proposed fix is correct, minimal, and applicable.

Then compare with the answer key and calculate a detection rate. A miss is useful data; do not “help” the review by editing the branch until the observation is recorded.

## Lab 2: conversation and learnings

On the Lab 1 MR, ask questions in comments and save the answers in your evidence log:

```text
@coderabbitai why is this dangerous? Show me an example input that breaks it.
@coderabbitai explain what samples/backup.sh does step by step.
@coderabbitai generate a sequence diagram.
```

Disagree with one low-value suggestion using a real project preference, for example:

```text
@coderabbitai In this repo we use [[ ]] in Bash and require set -euo pipefail. Please remember this preference for future reviews.
```

Check whether the reply reports a learning, then test that preference in a later MR. A chat reply is not proof that the learning was persisted; verify the learning in the CodeRabbit UI and observe a later review.

## Lab 3: incremental review controls

Fix two findings on the same branch and push. Compare the new review with the first review:

- Did only the new commit or changed areas get revisited?
- Were addressed threads resolved?
- Did a new finding appear because the fix changed surrounding behavior?

Try the review commands documented for your GitLab integration, such as `review`, `full review`, `pause`, `resume`, `summary`, `configuration`, `rate limit`, and `help`. Record the exact command, where you posted it, the response, and whether it changed MR state. Do not assume every command is enabled for every plan or provider.

## Lab 4: configuration and coding guidelines

Create a separate MR that adds `.coderabbit.yaml`. Copy `.coderabbit.yaml.example` first, then change one setting at a time:

```yaml
language: en-US
tone_instructions: "Be concise and direct. Explain the risk, then the fix."
reviews:
  profile: assertive
  high_level_summary: true
  poem: false
  auto_review:
    enabled: true
    drafts: false
  path_instructions:
    - path: "**/*.sh"
      instructions: |
        Require set -euo pipefail. Flag unquoted variables, destructive commands
        using unvalidated input, and missing error handling after cd.
    - path: "**/*.py"
      instructions: |
        Require type hints on public functions and context managers for files.
        Flag broad except clauses.
  path_filters:
    - "!**/*.lock"
    - "!**/vendor/**"
```

Validate the syntax, then compare a `chill` and `assertive` review of the same challenge. Add a root `CLAUDE.md` or `AGENTS.md` in another MR with three concrete rules and test whether findings cite those rules. Keep configuration changes separate so you can attribute behavior changes.

## Lab 5: finishing actions

On the planted-bug MR, test only actions available in your connected workspace:

- fix comments;
- fix one inline finding;
- generate docstrings;
- generate unit tests;
- simplify code; and
- resolve a deliberately created merge conflict.

For every generated commit or MR, review the diff as if a junior developer wrote it. Check that tests assert behavior and do not merely increase coverage. Never merge an automated fix without understanding it.

## Lab 6: pre-merge checks and linked issues

Enable warning-mode checks in a dedicated configuration MR. Test one failure at a time:

- a vague MR title;
- an incomplete description;
- missing docstrings; and
- a custom check such as “no secret-like literals in the diff.”

Create a GitLab issue describing a small change, then open an MR that implements only half of it and includes an unrelated edit. Link the issue and evaluate whether CodeRabbit notices both the missing requirement and the out-of-scope change.

## Lab 7: CI/CD analysis (optional)

If this GitLab has a runner, add a small `.gitlab-ci.yml` that runs ShellCheck and Python tests. Break one test on a branch and observe whether CodeRabbit incorporates the failed pipeline into its review. If there is no runner, document that this experiment is unavailable; do not install infrastructure solely to make the blog narrative look complete.

## Lab 8: security experiment

Do this only on a disposable branch and use fake values. Add, in one MR:

- a clearly fake token-shaped string;
- an old dependency version selected from a current advisory; and
- a `subprocess` call using untrusted input with `shell=True`.

Record which scanner or reasoning path identifies each issue. Remove the branch after the experiment. Do not put a real secret or a token-shaped test value in `main`, this README, or the answer key.

## Lab 9: CLI review before push

Install the CLI only after reading the current official instructions. Then compare local review modes with the MR review:

```bash
coderabbit auth login
coderabbit review
coderabbit review --uncommitted
coderabbit review --committed
```

The current CLI documentation distinguishes tracked changes from untracked files; use the documented include/uncommitted options for your installed version and record the version in your notes. Compare speed, findings, output format, and whether the CLI is useful as input to another coding agent.

## Lab 10: real-world trial

Only after the controlled labs, use a non-sensitive real repository. Choose one with a meaningful but reversible change. Ask:

- Did CodeRabbit find something a human would likely miss?
- What percentage of comments were worth acting on?
- Did configuration and learnings reduce noise?
- Would you trust its generated fix or test without rewriting it?
- What information must be redacted before publishing screenshots or transcripts?

## Evaluation sheet

Keep one row per MR in a private notes file or spreadsheet. Suggested columns:

| Field | What to record |
| --- | --- |
| Lab/MR | branch, MR number, commit, date |
| Environment | GitLab version, CodeRabbit plan/workspace, CLI version |
| Timing | push time, first review time, follow-up time |
| Findings | expected, found, missed, false positive |
| Quality | severity accuracy, explanation, fix quality |
| Workflow | webhook, incremental review, command response |
| Configuration | profile, path rule, guideline, learning tested |
| Safety | secrets redacted, generated code reviewed, branch cleaned up |
| Blog evidence | screenshot/transcript worth keeping and why |

For each category, score 1–5: summary accuracy, bug finding, signal-to-noise, shell/Python depth, learnings, configuration, fixes, speed, security, and CLI usefulness. Keep “found” and “false positive” counts separate; a high comment count is not a high score.

## Troubleshooting

**No review appears:** confirm the MR targets the expected branch, CodeRabbit has project access, the webhook shows a recent successful delivery, the public HTTPS GitLab URL is reachable from outside the LAN, and the MR is not being skipped by draft/configuration rules.

**CodeRabbit cannot reach GitLab:** test the public HTTPS hostname from a non-LAN network, then inspect the tunnel and edge policy on the GitLab host. Do not make the entire GitLab service public as a debugging shortcut.

**A command is ignored:** run the documented help/configuration command for the current integration and check the plan/workspace feature matrix. The original command list is a hypothesis, not a compatibility guarantee.

**Configuration is ignored:** verify the file name, YAML syntax, branch contents, indentation, and the effective configuration report. Test one setting at a time.

**Secret scanning blocks a lab:** use a low-entropy placeholder or a narrowly documented allowlist annotation for a disposable experiment. Do not disable repository hooks or add a broad secrets baseline entry.

**Trial or review limits are unclear:** use the current CodeRabbit billing, usage, and rate-limit pages. Record the date and plan in your evidence log instead of hardcoding a number in this README.

## Cleanup

Close or delete disposable MRs and branches, remove fake credentials and vulnerable dependency experiments, revoke temporary tokens, and review the CodeRabbit project connection. If you are shutting down the lab, disable the project integration before stopping the tunnel, then confirm that no public GitLab hostname remains reachable unintentionally.

## Blog outline this repo supports

1. Why pair CodeRabbit with a self-managed GitLab?
2. The network boundary: LAN Git remote, public HTTPS webhook/API path, and tunnel controls.
3. What an AI review catches in a controlled baseline.
4. Teaching the reviewer with configuration, guidelines, and learnings.
5. Incremental reviews and agentic finishing actions.
6. Security, false positives, and why human approval still matters.
7. CLI versus MR review.
8. What changed after the trial: a measured recommendation, not a product brochure.

Before publishing, remove internal hostnames, IPs, account names, webhook URLs, screenshots with identifiers, and all credentials. Link readers to the official CodeRabbit documentation rather than copying plan limits that may have changed.
