# Lab 5 — Finishing actions

[← Lab 4](lab-04-configuration.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 6](lab-06-pre-merge-and-issues.md)

## 5.1 Goal

Evaluate whether CodeRabbit can turn findings into useful work without creating new defects. These actions are optional and may depend on your plan or GitLab integration.

## 5.2 What you need

Use the Lab 1 MR or a disposable copy of it. Do not run generated code until you have inspected it.

## 5.3 Try one action

1. Open the Lab 1 MR.
2. Read the unresolved findings.
3. In a top-level comment, try one action documented for your workspace, such as:

~~~text
@coderabbitai fix comments
~~~

4. If the action offers a stacked MR, prefer the separate MR option.
5. Wait for the commit or new MR.
6. Inspect every changed line.
7. Run applicable syntax checks and tests.
8. Record whether the fix addressed the finding without unrelated changes.

Other actions to test one at a time, if available:

~~~text
@coderabbitai generate docstrings
@coderabbitai generate unit tests
@coderabbitai simplify
@coderabbitai resolve merge conflict
~~~

For an inline fix, reply to one specific CodeRabbit comment with the documented fix command rather than requesting every finding at once.

> Screenshot 5.1 — The command and CodeRabbit response.

> Screenshot 5.2 — The generated commit or stacked MR.

> Screenshot 5.3 — A generated test or code fix under review.

## 5.4 Deliberately create a conflict

Use a disposable branch:

~~~bash
git switch main
git pull --ff-only
git switch -c lab5-conflict
printf '\nChange from the lab branch.\n' >> README.md
git add README.md
git commit -m "test: create lab conflict"
git push -u origin lab5-conflict
~~~

Open an MR into main. Separately edit the same final README line on main through GitLab's web editor or a separate clean clone, commit it, and push. Return to the MR and observe the conflict indicator. Only then try a conflict-resolution action if your workspace provides it.

## 5.5 What to record

- Was the generated change correct?
- Was it minimal?
- Did generated tests exercise the original defect?
- Did CodeRabbit create a commit or a separate MR?
- Did a human need to repair the output?

## 5.6 Cleanup

Do not merge generated code without review. Close disposable MRs and delete the conflict branch after recording the evidence.

[← Lab 4](lab-04-configuration.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 6](lab-06-pre-merge-and-issues.md)

