# Lab 0 — Integration smoke test

[← Lab index](README.md) · [Main README](../README.md) · Next: [Lab 1](lab-01-planted-bugs.md)

## 0.1 Goal

Prove that GitLab can deliver a merge request (MR) event to CodeRabbit and that CodeRabbit can read and comment on the project. GitHub users can think of an MR as a pull request (PR).

Do not evaluate review quality yet. This lab tests connectivity and permissions only.

## 0.2 What you need

- A GitLab project containing this repository.
- Permission to create branches, push commits, and open an MR.
- CodeRabbit installed for the project.
- A public HTTPS GitLab web/API path reachable by CodeRabbit. GitLab.com already provides this; self-managed GitLab may need a public endpoint, tunnel, reverse proxy, or other supported connector.
- A local clone with the correct Git remote.

Check the remote:

~~~bash
git remote -v
git status --short --branch
~~~

## 0.3 Create the smoke-test branch

Run these commands from the repository root:

~~~bash
git switch main
git pull --ff-only
git switch -c lab0-smoke
printf '\nSmoke-test change for CodeRabbit.\n' >> README.md
git diff -- README.md
git add README.md
git commit -m "test: verify CodeRabbit integration"
git push -u origin lab0-smoke
~~~

The last command publishes the branch to GitLab. In GitHub terminology, this is the branch you would use to open a PR.

## 0.4 Open the merge request in GitLab

1. Open the GitLab project in your browser.
2. Select **Code > Merge requests** in the left navigation.
3. Select **New merge request**.
4. Set **Source branch** to lab0-smoke.
5. Set **Target branch** to main.
6. Select **Compare branches and continue**.
7. Review the changed README line.
8. Enter the title: **test: verify CodeRabbit integration**.
9. Add this description: **Smoke test to verify GitLab, webhooks, permissions, and CodeRabbit connectivity.**
10. Select **Create merge request**.
11. Do not merge it yet.

> Screenshot 0.1 — GitLab MR creation screen showing the source branch, target branch, title, and description.

## 0.5 Verify CodeRabbit

Wait a few minutes, then inspect the MR:

1. Open the MR's **Overview** tab.
2. Look for a comment from the CodeRabbit account.
3. Open **Settings > Webhooks** for the project in another tab.
4. Check the recent delivery for the MR event, if your installation uses project webhooks.
5. Record the time between the push and the first CodeRabbit response.

> Screenshot 0.2 — GitLab MR overview showing the source branch, target branch, and title.

> Screenshot 0.3 — CodeRabbit's first response on the smoke-test MR.

> Screenshot 0.4 — GitLab webhook delivery showing the event succeeded, if applicable.

## 0.6 What the result means

- If the MR exists but no webhook delivery appears, investigate GitLab integration setup.
- If delivery appears but CodeRabbit does not comment, investigate CodeRabbit access, endpoint reachability, and plan/workspace configuration.
- If a walkthrough appears, the basic plumbing works. That does not prove that every CodeRabbit capability is enabled.

Record:

- GitLab hosting type;
- GitLab version, if self-managed;
- CodeRabbit workspace or plan;
- branch name and MR number;
- push time;
- first review time; and
- any error message.

## 0.7 Cleanup

Close the MR without merging, or merge only if you want the smoke-test line in the default branch. Delete the branch from GitLab after recording the result:

~~~bash
git switch main
git branch -D lab0-smoke
git push origin --delete lab0-smoke
~~~

[← Lab index](README.md) · [Main README](../README.md) · Next: [Lab 1](lab-01-planted-bugs.md)
