# Lab 2 — Conversation and learnings

[← Lab 1](lab-01-planted-bugs.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 3](lab-03-incremental-reviews.md)

## 2.1 Goal

Learn how to ask CodeRabbit for explanations and test whether a stated preference becomes a stored learning.

## 2.2 What you need

Keep the Lab 1 MR open. Do not resolve or delete its discussions before completing this lab.

## 2.3 Ask questions in the MR

1. Open the Lab 1 MR.
2. On an inline CodeRabbit comment, select **Reply**.
3. Enter the following mention and question, replacing the example with the finding you are viewing:

~~~text
@coderabbitai why is this dangerous? Show me an example input that breaks it.
~~~

4. Select **Comment**.
5. In a new top-level MR comment, enter:

~~~text
@coderabbitai explain what samples/backup.sh does step by step.
~~~

6. Add another top-level comment:

~~~text
@coderabbitai generate a sequence diagram.
~~~

Wait for each reply before posting the next question.

> Screenshot 2.1 — Inline question and CodeRabbit reply.

> Screenshot 2.2 — Top-level explanation of backup.sh.

> Screenshot 2.3 — Sequence diagram response.

## 2.4 Teach a preference

Reply to a low-value suggestion with a real project convention:

~~~text
@coderabbitai In this repo we use [[ ]] in Bash and require set -euo pipefail. Please remember this preference for future reviews.
~~~

Record the exact comment and reply. Look for a statement that a learning was added or proposed.

Then:

1. Open the CodeRabbit web interface.
2. Open the organization or repository's **Learnings** area.
3. Find the new learning.
4. Record its scope and status.
5. Do not delete it until you have tested it in a later MR.

> Screenshot 2.4 — Learning entry showing its scope or status.

A reply agreeing with you is not proof that a learning was persisted. The later review is the real test.

## 2.5 What to record

- Was the explanation technically correct?
- Did the example input actually demonstrate the risk?
- Did the sequence diagram describe the code accurately?
- Was the learning stored, pending approval, or absent?
- Did CodeRabbit distinguish a repository preference from a one-off request?

## 2.6 Cleanup

Keep the learning for Lab 4 or delete it from the CodeRabbit Learnings page after recording the result.

[← Lab 1](lab-01-planted-bugs.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 3](lab-03-incremental-reviews.md)
