# Lab 7 — CI/CD pipeline analysis

[← Lab 6](lab-06-pre-merge-and-issues.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 8](lab-08-security.md)

## 7.0 Confirm the working repository

Run the pipeline commands from the local clone of coderabbit-gitlab-lab-clone:

~~~bash
# Enter the learner-owned GitLab clone.
cd /path/to/coderabbit-gitlab-lab-clone

# Confirm the GitLab remote before creating a pipeline branch.
git remote -v
~~~

## 7.1 Goal

See whether CodeRabbit uses failed automation results when explaining an MR. GitLab calls this automation a pipeline; GitHub users may know it as a GitHub Actions workflow.

This lab is optional and requires a GitLab runner.

## 7.2 Check for a runner

1. Open the GitLab project.
2. Select **Build > Pipelines**.
3. Check whether the project has a runner available.
4. If no runner is available, record that this lab is unavailable and skip to Lab 8.

> Screenshot 7.1 — GitLab runner or pipeline availability.

## 7.3 Add a small pipeline

Create a branch:

~~~bash
git switch main
git pull --ff-only
git switch -c lab7-ci
~~~

Create .gitlab-ci.yml with this minimal pipeline:

~~~bash
cat > .gitlab-ci.yml <<'EOF'
stages:
  - test

shellcheck:
  image: koalaman/shellcheck-alpine:stable
  stage: test
  script:
    - shellcheck samples/backup.sh

python-syntax:
  image: python:3.12-slim
  stage: test
  script:
    - python -m py_compile samples/users.py
EOF
~~~

If your runner cannot use these container images, substitute images available in your environment and record the change. Commit and push:

~~~bash
git add .gitlab-ci.yml
git commit -m "test: add CodeRabbit CI analysis pipeline"
git push -u origin lab7-ci
~~~

Open an MR from lab7-ci into main using **Code > Merge requests > Create merge request**.

> Screenshot 7.2 — Pipeline jobs for the MR.

## 7.4 Break one check

On the branch, introduce a deliberate test or syntax failure, then commit and push:

~~~bash
git add .
git commit -m "test: create a pipeline failure"
git push
~~~

Wait for the pipeline and CodeRabbit review. Record whether the walkthrough references the failed job and whether its recommendation matches the actual failure.

> Screenshot 7.3 — Failed pipeline job.

> Screenshot 7.4 — CodeRabbit explanation that references the pipeline result.

## 7.5 Cleanup

Close the MR and delete the branch. Remove the pipeline file if you do not want it in the default branch.

[← Lab 6](lab-06-pre-merge-and-issues.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 8](lab-08-security.md)
