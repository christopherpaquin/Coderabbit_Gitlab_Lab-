# Lab 1 — Baseline review with planted defects

[← Lab 0](lab-00-smoke-test.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 2](lab-02-learnings.md)

## 1.0 Confirm the working repository

Run every command in this lab from your local learner-owned clone, not from the GitHub template. Replace the placeholder with the path where you cloned coderabbit-gitlab-lab-clone:

~~~bash
# Enter the learner-owned GitLab clone.
cd /path/to/coderabbit-gitlab-lab-clone

# Confirm the current branch and whether local files are changed.
git status --short --branch

# Confirm that origin points to your GitLab working project.
git remote -v
~~~

The status should show a clean branch before you continue. If origin points to GitHub, stop and return to [Lab 0](lab-00-smoke-test.md).

## 1.1 Goal

Create the control experiment for the course. You will apply a patch that introduces deliberately flawed Bash and Python code, push it to a new branch, and ask CodeRabbit to review the MR.

Do not run the planted code. The branch exists for review only.

## 1.2 What you need

- Lab 0 completed successfully.
- A clean working tree on main.
- The repository files from this project.
- A private notes document for observations.
- The answer key at labs/answer-key.md, which you must not read until after your first review.

Check your starting state:

~~~bash
git switch main
git pull --ff-only
git status --short
~~~

The status command should produce no output.

## 1.3 Create the challenge branch

~~~bash
git switch -c lab1-planted-bugs
git apply labs/patches/lab-01-planted-bugs.patch
git diff --check
git status --short
~~~

You should see changes to samples/backup.sh and samples/users.py. Do not execute either file.

Commit and push the change:

~~~bash
git add samples
git commit -m "test: add planted CodeRabbit review findings"
git push -u origin lab1-planted-bugs
~~~

## 1.4 Open the MR

1. Open the GitLab project.
2. Select **Code > Merge requests**.
3. Select **New merge request**.
4. Select source branch lab1-planted-bugs.
5. Select target branch main.
6. Select **Compare branches and continue**.
7. Set the title to **test: add planted CodeRabbit review findings**.
8. Add this description: **Baseline CodeRabbit challenge containing intentionally flawed Bash and Python changes. Do not execute the changed files.**
9. Confirm that the diff contains only the two sample files.
10. Select **Create merge request**.
11. Do not merge the MR.

> Screenshot 1.1 — GitLab MR creation screen showing source branch, target branch, title, and description.

## 1.5 Review CodeRabbit before reading the answer key

Wait for the first review. Read the walkthrough from top to bottom, then inspect the inline comments.

Record:

- push time and first-review time;
- number of walkthrough, actionable, and nitpick comments;
- which Bash and Python issues were found;
- whether ShellCheck, Ruff, or another tool is named;
- whether the dangerous interaction between cd, tar, and rm -rf is explained;
- whether the summary describes intent rather than only filenames;
- whether each proposed fix is correct and minimal; and
- whether any clean code is incorrectly reported as a defect.

> Screenshot 1.2 — CodeRabbit walkthrough at the top of the MR.

> Screenshot 1.3 — An inline CodeRabbit finding on samples/backup.sh.

> Screenshot 1.4 — An inline CodeRabbit finding on samples/users.py.

> Screenshot 1.5 — Any tool-attributed finding or pre-merge check.

Only after recording your observations, read [the answer key](answer-key.md). Compare expected issues with found, missed, duplicate, and false-positive findings.

## 1.6 What CodeRabbit is doing

This review tests multiple layers at once:

- deterministic tools may recognize quoting, syntax, or style patterns;
- security tools may recognize SQL injection or credential-like text;
- the language model may reason about the sequence of cd, archive creation, and destructive cleanup;
- the walkthrough tests whether it understood the change as a whole.

A useful review is not simply one that produces many comments. A useful review identifies real risks, explains why they matter, and proposes a safe correction.

## 1.7 Cleanup

Do not merge this MR. Keep the branch if you need it for Labs 2–5. To reset it later:

~~~bash
git switch main
git branch -D lab1-planted-bugs
~~~

If you delete the remote branch, recreate it by repeating section 1.3.

[← Lab 0](lab-00-smoke-test.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 2](lab-02-learnings.md)
