# Lab 9 — CLI review before push

[← Lab 8](lab-08-security.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 10](lab-10-real-world.md)

## 9.1 Goal

Review local changes before they are pushed to GitLab. This lets you compare an early command-line interface (CLI) review with a later GitLab MR review.

## 9.2 Install and authenticate

Read the current [CodeRabbit CLI documentation](https://docs.coderabbit.ai/cli) before installing. Then install using the documented method for your operating system.

After installation, confirm the command exists:

~~~bash
coderabbit --version
~~~

Authenticate using the command shown by the current documentation:

~~~bash
coderabbit auth login
~~~

Some current documentation uses the shorter cr alias. Use whichever command your installed version provides.

## 9.3 Create local changes

Use a disposable branch and make a small change:

~~~bash
git switch main
git pull --ff-only
git switch -c lab9-cli
printf '\nCLI review experiment.\n' >> README.md
~~~

Do not commit yet. Check the working tree:

~~~bash
git status --short
git diff -- README.md
~~~

## 9.4 Run local review modes

Run one mode at a time and save the output:

~~~bash
coderabbit review
coderabbit review --uncommitted
coderabbit review --committed
coderabbit review --include-untracked
~~~

The exact option behavior can change. The current CLI documentation distinguishes tracked changes from untracked files, so record the installed version and the command output.

> Screenshot 9.1 — CLI version and authentication status.

> Screenshot 9.2 — Review of uncommitted changes.

> Screenshot 9.3 — A CLI finding that matches or differs from the MR review.

## 9.5 Compare with an MR

Commit and push the same change:

~~~bash
git add README.md
git commit -m "test: compare CLI and MR reviews"
git push -u origin lab9-cli
~~~

Open an MR from lab9-cli into main. Compare the CLI findings with the CodeRabbit MR findings and record:

- what was found locally first;
- what appeared only in the MR;
- response time;
- output usefulness to a coding agent; and
- false positives.

## 9.6 Cleanup

Close the MR and remove the branch:

~~~bash
git switch main
git branch -D lab9-cli
git push origin --delete lab9-cli
~~~

[← Lab 8](lab-08-security.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 10](lab-10-real-world.md)

