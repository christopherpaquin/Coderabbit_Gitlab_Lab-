# Lab 10 — Real-world trial

[← Lab 9](lab-09-cli.md) · [Lab index](README.md) · [Main README](../README.md)

## 10.1 Goal

Apply what you learned to a real but non-sensitive repository and decide whether CodeRabbit provides enough value for your workflow.

## 10.2 Choose the repository and change

Choose a repository that:

- contains no secrets or customer data;
- has a reversible change;
- uses a language CodeRabbit can review;
- is small enough to understand; and
- is not business-critical.

Good candidates include a Bash-heavy infrastructure repository or a small Python utility. Avoid starting with a large production migration.

Create a branch:

~~~bash
git switch main
git pull --ff-only
git switch -c lab10-real-world
~~~

Make one meaningful change, then inspect it locally:

~~~bash
git diff --check
git status --short
git diff
git add .
git commit -m "test: evaluate CodeRabbit on a real change"
git push -u origin lab10-real-world
~~~

## 10.3 Open the MR

1. Open the repository in GitLab.
2. Select **Code > Merge requests**.
3. Select **New merge request**.
4. Choose source lab10-real-world and target main.
5. Select **Compare branches and continue**.
6. Write a description that explains intent, testing, and risk.
7. Select **Create merge request**.
8. Wait for the review.
9. Read it as a human reviewer would.

> Screenshot 10.1 — Real-world MR overview and CodeRabbit walkthrough.

> Screenshot 10.2 — The most valuable finding.

> Screenshot 10.3 — A false positive or noisy suggestion, if present.

## 10.4 Make the recommendation

Answer these questions:

- Did CodeRabbit find something a human reviewer would likely miss?
- What percentage of comments were worth acting on?
- Did configuration and learnings reduce noise?
- Would you trust a generated fix or test without rewriting it?
- Did the review arrive fast enough to fit your workflow?
- What information must be redacted before publishing screenshots or transcripts?
- Would you keep using MR reviews, CLI reviews, or both?

Write a short recommendation with evidence rather than a general impression.

## 10.5 Cleanup

Close or merge the MR according to your normal review process. Delete the experiment branch if it is no longer needed:

~~~bash
git switch main
git branch -D lab10-real-world
git push origin --delete lab10-real-world
~~~

[← Lab 9](lab-09-cli.md) · [Lab index](README.md) · [Main README](../README.md)
