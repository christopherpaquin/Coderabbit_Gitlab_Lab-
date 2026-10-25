# Lab 3 — Incremental reviews and controls

[← Lab 2](lab-02-learnings.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 4](lab-04-configuration.md)

## 3.1 Goal

See how CodeRabbit behaves when an existing MR receives new commits. Then test review-control commands and learn when to pause, resume, or request a full review.

## 3.2 What you need

Keep the Lab 1 MR and branch available. If you deleted them, repeat Lab 1.

## 3.3 Fix two findings

Choose two findings you understand. Make the fixes on the Lab 1 branch using your editor. Do not ask CodeRabbit to make these fixes yet; this step tests how the review responds to your own commit.

Check and push:

~~~bash
git switch lab1-planted-bugs
git status --short
git diff --check
git add samples
git commit -m "fix: address two review findings"
git push
~~~

## 3.4 Compare the second review

1. Open the existing Lab 1 MR.
2. Open the **Changes** tab and identify the new commit.
3. Check whether the addressed discussions are marked resolved.
4. Compare the new review with the original walkthrough.
5. Record whether CodeRabbit reviewed only new changes or revisited more of the MR.

> Screenshot 3.1 — The branch commit list showing the original and fix commits.

> Screenshot 3.2 — An original finding resolved after the fix.

> Screenshot 3.3 — The incremental-review summary.

## 3.5 Test review commands

Post one command at a time as a new top-level MR comment. Use the exact command syntax shown in the current CodeRabbit documentation if your integration differs.

~~~text
@coderabbitai help
@coderabbitai rate limit
@coderabbitai configuration
@coderabbitai review
~~~

For pause, resume, full review, summary, and ignore, test only the commands available in your workspace:

~~~text
@coderabbitai pause
@coderabbitai resume
@coderabbitai full review
~~~

After each command:

1. Wait for a reply or status change.
2. Record the exact command and timestamp.
3. Record whether the MR review state changed.
4. Capture a screenshot if the command produces a distinct result.

> Screenshot 3.4 — Help or configuration response.

> Screenshot 3.5 — A pause or resume status change.

## 3.6 What to record

- How long the incremental review took.
- Whether addressed comments resolved automatically.
- Whether new findings appeared.
- Which commands worked.
- Which commands were unavailable or plan-dependent.
- Whether full review actually revisited the complete MR.

## 3.7 Cleanup

Leave the branch available for Labs 4 and 5, or close the MR after saving your notes.

[← Lab 2](lab-02-learnings.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 4](lab-04-configuration.md)
