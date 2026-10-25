# CodeRabbit + GitLab learning lab

[![GitLab](https://img.shields.io/badge/GitLab-merge%20request%20lab-FC6D26?logo=gitlab&logoColor=white)](https://about.gitlab.com/)
[![CodeRabbit](https://img.shields.io/badge/CodeRabbit-AI%20code%20review-6E56CF)](https://www.coderabbit.ai/)
[![Bash](https://img.shields.io/badge/Bash-sample%20code-4EAA25?logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)
[![Python](https://img.shields.io/badge/Python-sample%20code-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pre--commit](https://img.shields.io/badge/pre--commit-hooks-FAB040?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Markdown](https://img.shields.io/badge/docs-Markdown-000000?logo=markdown&logoColor=white)](https://www.markdownguide.org/)

> A GitLab-first learning lab for GitHub users who want to understand CodeRabbit by testing it on purposefully reviewable changes.

This repository is a hands-on course for learning GitLab workflow and CodeRabbit. It is written for people who know GitHub but are new to GitLab, and for anyone who wants to evaluate AI code review before trusting it on a real project.

## Start here

1. Read the connectivity requirements and choose a GitLab setup.
2. Review the GitHub-to-GitLab translation guide.
3. Use the lab selector below or open the [lab index](labs/README.md).
4. Work through Lab 0 before opening the planted-bug review in Lab 1.
5. Capture screenshots at the numbered checkpoints in each lab.

## At a glance

| | |
| --- | --- |
| Audience | GitHub users learning GitLab and CodeRabbit |
| Format | Guided merge-request experiments |
| Practice | Git workflow, AI review, configuration, learnings, security, and CLI review |
| Safety rule | The planted-bug branch is for review only; never run it against real data |
| Outcome | A measured recommendation and optional blog material |

## What you will learn

- Create a GitLab merge request (MR), which is GitLab's name for a GitHub pull request (PR).
- Connect CodeRabbit to a GitLab repository and confirm the integration works.
- Read walkthroughs, inline findings, severity, merge-risk signals, and tool output.
- Ask questions in an MR discussion and test whether CodeRabbit remembers preferences.
- Compare incremental reviews with full reviews.
- Configure review behavior with YAML, coding guidelines, and learnings.
- Evaluate automated fixes and generated tests instead of accepting them blindly.
- Compare an MR review with a local CodeRabbit command-line interface (CLI) review.
- Measure signal, noise, speed, and safety well enough to write an evidence-based article.

## GitHub-to-GitLab translation

| GitLab term | GitHub equivalent | Meaning |
| --- | --- | --- |
| project | repository | Hosted source-code workspace |
| merge request (MR) | pull request (PR) | Proposed change from one branch into another |
| pipeline | GitHub Actions workflow | Automated jobs after a push or MR/PR event |
| runner | GitHub Actions runner | Machine that executes automation jobs |
| project member | repository collaborator | Person or bot with project access |
| protected branch | branch protection rule | Rules controlling push, merge, or approval |
| webhook | webhook | HTTP callback notifying another service |
| GitLab CI/CD | GitHub Actions | Built-in automation platform |

When this guide says “open an MR,” GitHub users should read that as “open a PR.” The workflow is familiar: create a branch, commit, push, open a review request, discuss feedback, update the branch, and merge when ready.

## What CodeRabbit does

Think of CodeRabbit as an AI review partner beside your normal human review process. It is not a final approver, a replacement for tests, or a guarantee that code is safe. Its value is a fast second perspective before a change is merged.

For a repository review, CodeRabbit may combine:

- the diff, changed files, and surrounding code;
- repository instructions such as a CodeRabbit YAML file, AGENTS.md, or CLAUDE.md;
- earlier conversations and stored learnings;
- linked issues;
- available pipeline results; and
- static-analysis or security-tool output enabled for your plan.

Depending on the product surface, plan, workspace, and Git provider, you may see:

- walkthroughs explaining what changed;
- inline findings about security, correctness, reliability, maintainability, tests, or style;
- severity, reasoning, tool attribution, and suggested code changes;
- chat replies in MR discussions;
- incremental reviews after new commits;
- configuration, coding-guideline, and learning support;
- pre-merge checks for titles, descriptions, docstrings, linked issues, and custom rules;
- local reviews through the CodeRabbit CLI; and
- optional actions such as fixing comments, generating tests or docstrings, simplifying code, or resolving conflicts.

Treat every finding and generated change as a hypothesis to evaluate. CodeRabbit can be useful and still be wrong. The purpose of this lab is to measure both its strengths and its failure modes.

Capabilities and limits change. Use the official [CodeRabbit documentation](https://docs.coderabbit.ai/) as the authority for your account, especially the pages for [self-managed GitLab](https://docs.coderabbit.ai/platforms/self-hosted-gitlab), [review commands](https://docs.coderabbit.ai/reference/review-commands), [YAML configuration](https://docs.coderabbit.ai/getting-started/yaml-configuration), [learnings](https://docs.coderabbit.ai/knowledge-base/learnings), [pre-merge checks](https://docs.coderabbit.ai/pr-reviews/pre-merge-checks), [CLI](https://docs.coderabbit.ai/cli), and [plans](https://docs.coderabbit.ai/management/plans).

## How CodeRabbit connects to GitLab

CodeRabbit is a cloud service, so it must communicate with the GitLab installation hosting the repository. Your Git remote is where your workstation pushes and fetches code. CodeRabbit also needs an HTTPS-accessible GitLab web and application programming interface (API) endpoint so it can receive events, read the MR, and post review results.

> **Key idea:** your workstation can push successfully while CodeRabbit still cannot review the MR. Git transport and web/API reachability are separate paths.

### Choose your setup

| GitLab setup | What you need |
| --- | --- |
| GitLab.com | A GitLab.com project and the CodeRabbit GitLab integration |
| Self-managed GitLab with public HTTPS | Stable hostname, valid TLS certificate, reachable web/API endpoints, and CodeRabbit onboarding |
| Private self-managed GitLab | A controlled public HTTPS entry point through a tunnel, reverse proxy, load balancer, or supported private connector |
| GitLab reachable only privately | A connectivity change before CodeRabbit can review it |

A Cloudflare Tunnel is one solution, not a requirement. The original author used one for a private home-lab GitLab. Other readers may use GitLab.com, a public self-managed deployment, or another controlled network boundary.

### Connectivity checklist

Before investigating review quality:

1. Open the GitLab web interface for the project.
2. Check current CodeRabbit requirements for your GitLab version.
3. Install or connect the project in CodeRabbit.
4. Give the CodeRabbit identity or integration the access it needs.
5. Confirm recent successful webhook deliveries, when applicable.
6. Confirm the public HTTPS GitLab URL works from outside the private network.
7. Allow required CodeRabbit traffic without exposing unrelated services.
8. Understand billing, usage, and rate limits for your account.

Do not copy private hostnames, IP addresses, tunnel identifiers, access policies, OAuth secrets, or personal access tokens (PATs) into this repository or a public blog post.

## Repository map

| Path | Purpose |
| --- | --- |
| labs/README.md | Numbered lab selector and navigation hub |
| labs/lab-00-smoke-test.md through labs/lab-10-real-world.md | Individual lab instructions |
| labs/answer-key.md | Lab 1 findings; read only after reviewing the MR |
| labs/patches/lab-01-planted-bugs.patch | Turns clean samples into the Lab 1 challenge |
| samples/backup.sh | Safe baseline for the shell lab |
| samples/users.py | Safe baseline for the Python lab |
| .coderabbit.yaml.example | Starter configuration for Lab 4 |

The main branch is intentionally safe. The first challenge is a patch applied on a temporary branch, so CodeRabbit sees unsafe edits in an MR while the default branch remains usable.

## Lab selector

Use the [lab index](labs/README.md) to choose a lab. The recommended sequence is Lab 0 through Lab 10 because later experiments depend on observations and configuration from earlier ones.

| Lab | Topic | Direct link |
| ---: | --- | --- |
| 0 | Integration smoke test | [Open Lab 0](labs/lab-00-smoke-test.md) |
| 1 | Baseline review with planted defects | [Open Lab 1](labs/lab-01-planted-bugs.md) |
| 2 | Conversation and learnings | [Open Lab 2](labs/lab-02-learnings.md) |
| 3 | Incremental reviews and controls | [Open Lab 3](labs/lab-03-incremental-reviews.md) |
| 4 | Configuration and coding guidelines | [Open Lab 4](labs/lab-04-configuration.md) |
| 5 | Finishing actions | [Open Lab 5](labs/lab-05-finishing-actions.md) |
| 6 | Pre-merge checks and linked issues | [Open Lab 6](labs/lab-06-pre-merge-and-issues.md) |
| 7 | CI/CD pipeline analysis | [Open Lab 7](labs/lab-07-ci-analysis.md) |
| 8 | Security experiment | [Open Lab 8](labs/lab-08-security.md) |
| 9 | CLI review before push | [Open Lab 9](labs/lab-09-cli.md) |
| 10 | Real-world trial | [Open Lab 10](labs/lab-10-real-world.md) |

## Evaluation sheet

Keep one row per MR in a private notes file or spreadsheet.

| Field | What to record |
| --- | --- |
| Lab/MR | Branch, MR number, commit, date |
| Environment | GitLab hosting type, CodeRabbit plan/workspace, CLI version |
| Timing | Push time, first review time, follow-up time |
| Findings | Expected, found, missed, false positive |
| Quality | Severity accuracy, explanation, fix quality |
| Workflow | Webhook, incremental review, command response |
| Configuration | Profile, path rule, guideline, learning tested |
| Safety | Secrets redacted, generated code reviewed, branch cleaned up |
| Blog evidence | Screenshot or transcript worth keeping and why |

Score 1–5 for summary accuracy, bug finding, signal-to-noise, shell/Python depth, learnings, configuration, fixes, speed, security, and CLI usefulness. Keep found and false-positive counts separate.

## Troubleshooting

**No review appears:** confirm the MR targets the expected branch, CodeRabbit has project access, webhook delivery succeeds when applicable, the GitLab web/API endpoint is reachable from the internet, and the MR is not skipped by draft or configuration rules.

**CodeRabbit cannot reach self-managed GitLab:** test the public HTTPS hostname from outside the private network, then inspect the tunnel, reverse proxy, firewall, or load balancer. Do not make all of GitLab public as a debugging shortcut.

**A command is ignored:** check the current help/configuration command and plan/workspace feature matrix. The command list is a learning checklist, not a compatibility guarantee.

**Configuration is ignored:** verify the file name, YAML syntax, branch contents, indentation, and effective configuration report. Test one setting at a time.

**Secret scanning blocks a lab:** use a low-entropy placeholder or a narrowly documented allowlist annotation for a disposable experiment. Do not disable repository hooks or add a broad secrets baseline entry.

**Trial or review limits are unclear:** use current CodeRabbit billing, usage, and rate-limit pages. Record the date and plan in your evidence log instead of hardcoding a number here.

## Cleanup

Close or delete disposable MRs and branches, remove fake credentials and vulnerable dependency experiments, revoke temporary tokens, and review the CodeRabbit project connection. If you are shutting down a tunneled lab, disable the project integration before removing the public endpoint.

## Blog outline

1. Why pair CodeRabbit with GitLab?
2. GitHub-to-GitLab translation: what changes and what stays familiar.
3. How internet reachability affects CodeRabbit integrations.
4. What an AI review catches in a controlled baseline.
5. Teaching the reviewer with configuration, guidelines, and learnings.
6. Incremental reviews and agentic finishing actions.
7. Security, false positives, and why human approval still matters.
8. CLI versus MR review.
9. What changed after the trial: a measured recommendation, not a product brochure.
