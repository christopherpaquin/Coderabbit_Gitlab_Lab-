# CodeRabbit + GitLab learning lab

[![GitLab](https://img.shields.io/badge/GitLab-merge%20request%20lab-FC6D26?logo=gitlab&logoColor=white)](https://about.gitlab.com/)
[![CodeRabbit](https://img.shields.io/badge/CodeRabbit-AI%20code%20review-6E56CF)](https://www.coderabbit.ai/)
[![Bash](https://img.shields.io/badge/Bash-sample%20code-4EAA25?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![Python](https://img.shields.io/badge/Python-sample%20code-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pre--commit](https://img.shields.io/badge/pre--commit-hooks-FAB040?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Markdown](https://img.shields.io/badge/docs-Markdown-000000?logo=markdown&logoColor=white)](https://www.markdownguide.org/)

> A GitLab-first learning lab for GitHub users who want to understand CodeRabbit by testing it on purposefully reviewable changes.

This repository is a hands-on course for learning two related skills:

1. how GitLab organizes source code, branches, merge requests, issues, webhooks, and pipelines; and
2. how CodeRabbit uses artificial intelligence (AI) to review code, explain risks, learn team preferences, and help with software-development tasks.

The lab is written especially for people who are comfortable with GitHub but new to GitLab. It also gives you a controlled way to evaluate CodeRabbit before trusting it on a real project.

## At a glance

| | |
| --- | --- |
| **Audience** | GitHub users learning GitLab and CodeRabbit |
| **Format** | Guided merge-request experiments with intentionally reviewable code |
| **You will practice** | GitLab workflow, AI review, configuration, learnings, security review, and CLI review |
| **Safety rule** | The planted-bug branch is for review only; never run it against real data |
| **End product** | Your own measured recommendation and optional blog material |

<details>
<summary><strong>Contents</strong></summary>

- [What you will learn](#what-you-will-learn)
- [A GitHub user's translation guide](#a-github-users-translation-guide)
- [What CodeRabbit does](#what-coderabbit-does)
- [How CodeRabbit connects to GitLab](#how-coderabbit-connects-to-gitlab)
- [Repository map](#repository-map)
- [Labs 0–10](#start-here-lab-0-integration-smoke-test)
- [Evaluation sheet](#evaluation-sheet)
- [Troubleshooting](#troubleshooting)
- [Cleanup](#cleanup)
- [Blog outline](#blog-outline-this-repo-supports)

</details>

## What you will learn

By the end, you should be able to:

- create a branch and open a GitLab merge request (MR);
- understand that an MR is GitLab's name for what GitHub calls a pull request (PR);
- connect CodeRabbit to a GitLab repository;
- read a CodeRabbit walkthrough, inline finding, severity, and merge-risk signal;
- ask CodeRabbit questions in an MR discussion;
- compare an incremental review with a full review;
- influence reviews with configuration, coding guidelines, and learnings;
- evaluate suggested fixes and generated tests instead of accepting them blindly;
- compare a GitLab MR review with a local CodeRabbit command-line interface (CLI) review; and
- measure signal, noise, speed, and safety well enough to write an evidence-based blog post.

The sample code is intentionally small. The point is not to build an application. The point is to create changes whose risks you understand, then see what CodeRabbit notices, misses, misunderstands, or proposes to change.

## A GitHub user's translation guide

GitLab and GitHub use different names for many familiar ideas.

| GitLab term | GitHub equivalent | Meaning |
| --- | --- | --- |
| project | repository | The hosted source-code workspace |
| merge request (MR) | pull request (PR) | A proposed change from one branch into another |
| default branch | default branch | Usually `main`; the normal integration target |
| issue | issue | A request, bug, or piece of planned work |
| pipeline | GitHub Actions workflow | Automated jobs that run after a push or MR/PR event |
| runner | GitHub Actions runner | A machine that executes pipeline/workflow jobs |
| project member | repository collaborator | A person or bot with access to the project |
| protected branch | branch protection rule | Rules controlling who can push, merge, or approve |
| merge | merge | Integrating the source branch into the target branch |
| webhook | webhook | An HTTP callback that tells another service an event occurred |
| GitLab CI/CD | GitHub Actions | The platform's built-in automation system |

When this guide says “open an MR,” GitHub users should read that as “open a PR.” The workflow is familiar: create a branch, make a commit, push it, open a review request, discuss feedback, update the branch, and merge when the change is ready. The user interface and permission names differ, so learning those differences is part of this lab.

## What CodeRabbit does

Think of CodeRabbit as an AI review partner that sits beside your normal human review process. It is not the owner of your repository, not a replacement for tests, and not a final approver. Its value is that it can examine a change quickly and consistently, then give you another perspective before the code is merged.

For a repository review, CodeRabbit can use several kinds of context:

- the change itself: the diff, changed files, and surrounding code;
- repository instructions: a `.coderabbit.yaml` file, `AGENTS.md`, `CLAUDE.md`, or other supported guidance;
- earlier conversations and stored learnings about review preferences;
- linked issues and the relationship between the requested work and the actual change;
- available pipeline results; and
- static-analysis or security-tool output, when enabled for your plan and repository.

Depending on the CodeRabbit product surface, plan, workspace, and Git provider, you may see some or all of these capabilities:

### Explain a change

A walkthrough summarizes the purpose of an MR and may describe changes by file or by flow. This is useful for checking whether the reviewer understood intent rather than merely repeating filenames.

### Find problems

Inline comments can point to security risks, correctness bugs, reliability problems, maintainability issues, missing tests, or lower-priority style concerns. A finding may include severity, reasoning, tool attribution, and a suggested code change.

### Review the review

You can ask questions in the MR discussion, request an explanation or sequence diagram, disagree with a suggestion, and ask CodeRabbit to reconsider a finding. This is an important part of the lab: you are learning how to judge an AI review, not just how to receive one.

### Remember preferences

Natural-language conversations can create “learnings”: stored review preferences associated with a repository or organization. For example, you might teach CodeRabbit that this project requires strict Bash mode or prefers a particular error-handling pattern. Test whether a learning appears in a later review; do not assume that one agreeable reply means it was persisted.

### Apply repository rules

A version-controlled YAML configuration can set review tone, profile, path-specific instructions, path filters, automatic-review behavior, and selected tools. Coding-guideline files such as `AGENTS.md` or `CLAUDE.md` can provide normal project rules that CodeRabbit reads as repository context.

### Check readiness

Pre-merge checks can assess things such as the MR title, description, docstrings, linked-issue fit, and custom natural-language requirements. These are quality signals, not a substitute for a human approval policy or a passing test suite.

### Review local work

The CodeRabbit CLI can review local Git changes before you push them. This creates a second workflow: use CodeRabbit early while coding, then use the GitLab MR review to evaluate the complete proposed change and its collaboration context.

### Help with follow-up work

Depending on your plan and integration, CodeRabbit may offer actions such as fixing review comments, generating docstrings or unit tests, simplifying code, or resolving a merge conflict. Treat generated commits as untrusted contributions: inspect the diff, run tests, and decide whether the result is actually correct.

Capabilities and limits change. The official documentation is the authority for your account:

- [Self-managed GitLab integration](https://docs.coderabbit.ai/platforms/self-hosted-gitlab)
- [Review commands](https://docs.coderabbit.ai/reference/review-commands)
- [YAML configuration](https://docs.coderabbit.ai/getting-started/yaml-configuration)
- [Code guidelines](https://docs.coderabbit.ai/knowledge-base/code-guidelines)
- [Learnings](https://docs.coderabbit.ai/knowledge-base/learnings)
- [Pre-merge checks](https://docs.coderabbit.ai/pr-reviews/pre-merge-checks)
- [CLI](https://docs.coderabbit.ai/cli)
- [Plans and pricing](https://docs.coderabbit.ai/management/plans)

## How CodeRabbit connects to GitLab

CodeRabbit is a cloud service, so it must be able to communicate with the GitLab installation that hosts the repository. The important distinction is:

- your Git remote is where your workstation pushes and fetches code; and
- CodeRabbit needs an HTTPS-accessible GitLab web/API endpoint so it can receive events, read the MR, and post review results.

Your Git remote may use SSH or HTTPS and may point to an internal hostname. That does not automatically make the GitLab web application reachable from CodeRabbit.

> **Key idea:** your workstation can push successfully while CodeRabbit still cannot review the MR. Git transport and web/API reachability are separate paths.

### Choose the setup that matches your GitLab

| Your GitLab setup | What you need | Typical experience |
| --- | --- | --- |
| GitLab.com | A GitLab.com project and the CodeRabbit GitLab integration | Simplest path; GitLab is already internet-accessible |
| Self-managed GitLab with a public HTTPS URL | A stable hostname, valid TLS certificate, reachable GitLab web/API endpoints, and CodeRabbit onboarding | Similar to GitLab.com, but you own availability and access control |
| Private self-managed GitLab exposed through a tunnel or reverse proxy | A controlled public HTTPS entry point, tunnel/proxy rules, and CodeRabbit-compatible webhook/API access | Useful for a home lab or private network; this is the approach used by the original author |
| GitLab reachable only on a private network | A connectivity change | CodeRabbit cannot review it until the required web/API path is available |

A Cloudflare Tunnel is one solution, not a requirement. Other organizations may use a reverse proxy, load balancer, VPN or private connector supported by their security model, or a public GitLab deployment. The design goal is the same: expose only the required integration surface, use HTTPS, authenticate it properly, and avoid opening more of GitLab than necessary.

### The original author's example

This lab was first tested against a self-managed GitLab on a private LAN. The Git remote used an internal hostname, while a Cloudflare Tunnel provided the public HTTPS path that CodeRabbit needed. Your setup may be different. Use the following diagram as a concept, not as a required topology:

```text
your workstation --SSH or HTTPS Git--> GitLab
                                      ^
                                      | HTTPS webhooks and API
CodeRabbit cloud <--- public HTTPS endpoint
                         ^
                         |
          tunnel, reverse proxy, load balancer, or GitLab.com
```

Do not copy private hostnames, IP addresses, tunnel identifiers, access policies, OAuth secrets, or personal access tokens (PATs) into this repository or a public blog post.

### Connectivity checklist

Before investigating review quality, prove the integration plumbing:

1. You can open the GitLab web interface for the project.
2. The GitLab version and CodeRabbit integration requirements are compatible. Check the current [self-managed GitLab documentation](https://docs.coderabbit.ai/platforms/self-hosted-gitlab).
3. The project is installed or connected in CodeRabbit.
4. The CodeRabbit identity or integration has the project access it needs.
5. The project's webhook page shows recent successful deliveries, if your onboarding uses project webhooks.
6. The public HTTPS GitLab URL is reachable from outside your private network.
7. Your edge controls allow the required CodeRabbit webhook/API traffic without exposing unrelated administrative services.
8. Billing, usage, and rate limits are understood for the account you are using.

If the endpoint is not reachable from outside your network, fix that before changing code. A missing review caused by networking is not evidence that CodeRabbit misunderstood the code.

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

The `main` branch is intentionally safe. The first review challenge is a patch you apply on a temporary branch, so CodeRabbit sees the unsafe edits in an MR while the default branch remains usable. Read the answer key only after recording your own findings.

## Start here: Lab 0, integration smoke test

Before testing review quality, prove that the plumbing works. The commands below use GitLab terminology; on GitHub, opening an MR means opening a PR.

First inspect the remote instead of assuming its hostname:

```bash
git remote -v
git status
```

Then create a temporary branch and make a harmless documentation change:

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
- a webhook delivery appears in the project settings, when applicable;
- CodeRabbit comments on the MR; and
- the comment is from the expected CodeRabbit account.

Delete or close the smoke-test MR after recording the time from push to review. If no review appears, use the troubleshooting section before proceeding.

## Lab 1: baseline review with planted defects

This is the control experiment. Apply the patch on a new branch; do not run the resulting files.

> **Safety:** this branch exists to give CodeRabbit something interesting to review. Do not execute the planted shell script or connect the planted Python code to a real database.

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

Open an MR into `main`—a PR into the default branch in GitHub language. Before reading `labs/answer-key.md`, record:

- time from push to first review;
- number of walkthrough, actionable, and nitpick comments;
- which shell and Python issues were found;
- whether tool attribution appears, for example ShellCheck or Ruff;
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

Check whether the reply reports a learning, then test that preference in a later MR. A chat reply is not proof that the learning was persisted; verify the learning in the CodeRabbit interface and observe a later review. This is the same idea as teaching a code-review bot a repository convention, not training a new AI model yourself.

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

## Lab 7: CI/CD pipeline analysis (optional)

Continuous integration and continuous delivery (CI/CD) means automated jobs build, test, scan, or deploy code. GitLab calls its automation a pipeline; GitHub users may know the same idea as a GitHub Actions workflow.

If this GitLab has a runner, add a small `.gitlab-ci.yml` that runs ShellCheck and Python tests. Break one test on a branch and observe whether CodeRabbit incorporates the failed pipeline into its review. If there is no runner, document that this experiment is unavailable; do not install infrastructure solely to make the blog narrative look complete.

## Lab 8: security experiment

Do this only on a disposable branch and use fake values. Add, in one MR:

- a clearly fake token-shaped string;
- an old dependency version selected from a current advisory; and
- a `subprocess` call using untrusted input with `shell=True`.

Record which scanner or reasoning path identifies each issue. Remove the branch after the experiment. Do not put a real secret or a token-shaped test value in `main`, this README, or the answer key.

Security findings may come from different layers: a secret scanner can recognize credential-like text, a static-analysis tool can recognize a dangerous API, and CodeRabbit's reasoning can connect the code to a broader exploit path. Record which layer found what. Do not treat the presence of a scanner label as proof that the explanation is correct.

## Lab 9: CLI review before push

Install the CLI only after reading the current official instructions. Then compare local review modes with the MR review:

```bash
coderabbit auth login
coderabbit review
coderabbit review --uncommitted
coderabbit review --committed
coderabbit review --include-untracked
```

The current CLI documentation distinguishes tracked changes from untracked files; use the documented options for your installed version and record the version in your notes. Compare speed, findings, output format, and whether the CLI is useful as input to another coding agent.

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
| Environment | GitLab hosting type, CodeRabbit plan/workspace, CLI version |
| Timing | push time, first review time, follow-up time |
| Findings | expected, found, missed, false positive |
| Quality | severity accuracy, explanation, fix quality |
| Workflow | webhook, incremental review, command response |
| Configuration | profile, path rule, guideline, learning tested |
| Safety | secrets redacted, generated code reviewed, branch cleaned up |
| Blog evidence | screenshot/transcript worth keeping and why |

For each category, score 1–5: summary accuracy, bug finding, signal-to-noise, shell/Python depth, learnings, configuration, fixes, speed, security, and CLI usefulness. Keep “found” and “false positive” counts separate; a high comment count is not a high score.

## Troubleshooting

**No review appears:** confirm the MR targets the expected branch, CodeRabbit has project access, the webhook shows a recent successful delivery when applicable, the GitLab web/API endpoint is reachable from the internet, and the MR is not being skipped by draft or configuration rules.

**CodeRabbit cannot reach self-managed GitLab:** test the public HTTPS hostname from a network outside the private network, then inspect the tunnel, reverse proxy, firewall, or load balancer. Do not make the entire GitLab service public as a debugging shortcut.

**A command is ignored:** run the documented help/configuration command for the current integration and check the plan/workspace feature matrix. The command list in this guide is a learning checklist, not a compatibility guarantee.

**Configuration is ignored:** verify the file name, YAML syntax, branch contents, indentation, and the effective configuration report. Test one setting at a time.

**Secret scanning blocks a lab:** use a low-entropy placeholder or a narrowly documented allowlist annotation for a disposable experiment. Do not disable repository hooks or add a broad secrets baseline entry.

**Trial or review limits are unclear:** use the current CodeRabbit billing, usage, and rate-limit pages. Record the date and plan in your evidence log instead of hardcoding a number in this README.

## Cleanup

Close or delete disposable MRs and branches, remove fake credentials and vulnerable dependency experiments, revoke temporary tokens, and review the CodeRabbit project connection. If you are shutting down a tunneled lab, disable the project integration before removing the public endpoint, then confirm that no GitLab hostname remains reachable unintentionally.

## Blog outline this repo supports

1. Why pair CodeRabbit with GitLab?
2. GitHub-to-GitLab translation: what changes and what stays familiar.
3. How internet reachability affects CodeRabbit integrations.
4. What an AI review catches in a controlled baseline.
5. Teaching the reviewer with configuration, guidelines, and learnings.
6. Incremental reviews and agentic finishing actions.
7. Security, false positives, and why human approval still matters.
8. CLI versus MR review.
9. What changed after the trial: a measured recommendation, not a product brochure.

Before publishing, remove internal hostnames, IPs, account names, webhook URLs, screenshots with identifiers, and all credentials. Link readers to the official CodeRabbit documentation rather than copying plan limits that may have changed.
