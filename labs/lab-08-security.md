# Lab 8 — Security experiment

[← Lab 7](lab-07-ci-analysis.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 9](lab-09-cli.md)

## 8.0 Confirm the working repository

Run the security experiment only in the local clone of coderabbit-gitlab-lab-clone. Do not use the GitHub template checkout:

~~~bash
# Enter the learner-owned GitLab clone.
cd /path/to/coderabbit-gitlab-lab-clone

# Confirm the working tree and GitLab remote before creating the disposable branch.
git status --short --branch
git remote -v
~~~

## 8.1 Goal

Compare secret scanning, static analysis, dependency analysis, and CodeRabbit's reasoning on a disposable security MR.

## 8.2 Safety rules

- Use fake values only.
- Never use a real token, password, private key, or customer data.
- Do not merge the branch.
- Delete the branch after recording results.
- Do not put token-shaped test values in main, the README, or the answer key.

## 8.3 Create the disposable branch

~~~bash
git switch main
git pull --ff-only
git switch -c lab8-security
~~~

Add the following disposable files. The token is intentionally fake and the dependency version is for scanner testing only:

~~~bash
cat > security_demo.py <<'EOF'
import subprocess

DEMO_TOKEN = "glpat-" + "EXAMPLE-NOT-A-CREDENTIAL"

def run_user_command(user_input):
    return subprocess.call(user_input, shell=True)
EOF

printf 'requests==2.19.0\n' > requirements.txt
~~~

Keep the files small and explain in the MR description that all values are fake. Do not use a real token or run the script.

Commit and push:

~~~bash
git add .
git commit -m "test: exercise CodeRabbit security findings"
git push -u origin lab8-security
~~~

## 8.4 Open and inspect the MR

1. Open **Code > Merge requests**.
2. Select **New merge request**.
3. Choose source lab8-security and target main.
4. Select **Compare branches and continue**.
5. Use the title **test: exercise security findings**.
6. State that all credentials are fake and the branch must not be merged.
7. Select **Create merge request**.
8. Wait for CodeRabbit and any security tools.

> Screenshot 8.1 — Security experiment MR diff with fake values visible.

> Screenshot 8.2 — Secret-scanner finding.

> Screenshot 8.3 — Static-analysis or subprocess finding.

> Screenshot 8.4 — Dependency or vulnerability finding.

## 8.5 What to record

For each finding, record:

- which scanner or reasoning layer found it;
- whether the severity is appropriate;
- whether the explanation is understandable;
- whether the suggested fix removes the risk; and
- whether a human reviewer would have caught it.

## 8.6 Cleanup

Close the MR, delete the remote branch, and remove local test files:

~~~bash
git switch main
git branch -D lab8-security
git push origin --delete lab8-security
~~~

[← Lab 7](lab-07-ci-analysis.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 9](lab-09-cli.md)
