# Lab 6 — Pre-merge checks and linked issues

[← Lab 5](lab-05-finishing-actions.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 7](lab-07-ci-analysis.md)

## 6.0 Confirm the working repository

Run every command in this lab from the local clone of coderabbit-gitlab-lab-clone:

~~~bash
# Enter the learner-owned GitLab clone.
cd /path/to/coderabbit-gitlab-lab-clone

# Confirm that the working tree and remote are what you expect.
git status --short --branch
git remote -v
~~~

## 6.1 Goal

Test quality gates and issue-to-MR reasoning. GitHub users can compare this with required checks and linked issues on a pull request.

## 6.2 Add warning-mode checks

Create a configuration branch:

~~~bash
git switch main
git pull --ff-only
git switch -c lab6-pre-merge-checks
cp .coderabbit.yaml.example .coderabbit.yaml
~~~

Append this configuration under the existing reviews section. Start in warning mode so the check reports problems without blocking the MR:

~~~yaml
  pre_merge_checks:
    title:
      mode: warning
      requirements: "Use Conventional Commits format, for example fix(backup): validate source."
    description:
      mode: warning
    docstrings:
      mode: warning
      threshold: 80
    custom_checks:
      - name: No secrets in code
        mode: warning
        instructions: "Fail if the diff adds a password, token, API key, or private key literal."
      - name: Destructive shell operations guarded
        mode: warning
        instructions: "Fail if rm -rf, dd, or mkfs uses an unvalidated variable-built path."
~~~

If your current CodeRabbit schema differs, use the current official configuration reference and record the difference in your notes.

~~~bash
git add .coderabbit.yaml
git commit -m "test: add pre-merge checks"
git push -u origin lab6-pre-merge-checks
~~~

Open the MR into main:

1. Choose source branch lab6-pre-merge-checks.
2. Choose target branch main.
3. Use a clear title first so you can confirm the passing case.
4. Select **Create merge request**.
5. Read the walkthrough's pre-merge section.

> Screenshot 6.1 — Pre-merge checks shown in the walkthrough.

## 6.3 Create failing cases

Create separate branches or MRs for each test:

- title the MR “stuff”;
- omit the description template;
- add an undocumented public function; and
- add a fake credential-like literal.

For each MR, record whether the check is off, warning, or error.

> Screenshot 6.2 — A warning for an MR title or description.

## 6.4 Test linked issue assessment

1. In GitLab, select **Plan > Issues**.
2. Select **New issue**.
3. Use the title: **backup.sh should validate its source and log the operation**.
4. Describe two requirements: reject an empty source and log to syslog.
5. Select **Create issue**.
6. Create a branch that implements only one requirement and adds an unrelated README edit:

~~~bash
git switch main
git pull --ff-only
git switch -c lab6-linked-issue
printf '\nUnrelated documentation edit.\n' >> README.md
git add README.md
git commit -m "fix: partially address backup issue"
git push -u origin lab6-linked-issue
~~~

7. Open an MR into main.
8. In the description, include Closes #NUMBER, replacing NUMBER with the issue number.
9. State clearly which requirement you implemented.
10. Select **Create merge request**.
11. Ask CodeRabbit to assess whether the MR fulfills the linked issue.

> Screenshot 6.3 — Linked issue and MR relationship.

> Screenshot 6.4 — CodeRabbit assessment of the incomplete or out-of-scope change.

## 6.5 Cleanup

Close the experimental MRs and issue, or leave them open as evidence. Delete disposable branches.

[← Lab 5](lab-05-finishing-actions.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 7](lab-07-ci-analysis.md)
