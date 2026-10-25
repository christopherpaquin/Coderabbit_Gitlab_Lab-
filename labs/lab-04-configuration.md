# Lab 4 — Configuration and coding guidelines

[← Lab 3](lab-03-incremental-reviews.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 5](lab-05-finishing-actions.md)

## 4.0 Confirm the working repository

Run every command below from the local clone of coderabbit-gitlab-lab-clone:

~~~bash
# Enter the learner-owned GitLab clone.
cd /path/to/coderabbit-gitlab-lab-clone

# Confirm that origin points to the GitLab working project.
git remote -v
~~~

## 4.1 Goal

Test version-controlled review rules. You will add a CodeRabbit YAML configuration and a coding-guideline file in separate MRs so you can see which rule changes behavior.

## 4.2 What you need

- The Lab 1 branch or a fresh branch from main.
- The example file at .coderabbit.yaml.example.
- A way to compare two reviews of similar code.

## 4.3 Add the starter configuration

Start from main:

~~~bash
git switch main
git pull --ff-only
git switch -c lab4-configuration
cp .coderabbit.yaml.example .coderabbit.yaml
git diff -- .coderabbit.yaml
git add .coderabbit.yaml
git commit -m "test: add CodeRabbit review configuration"
git push -u origin lab4-configuration
~~~

Open an MR from lab4-configuration into main:

1. Open **Code > Merge requests**.
2. Select **New merge request**.
3. Choose source branch lab4-configuration and target branch main.
4. Select **Compare branches and continue**.
5. Use the title **test: add CodeRabbit review configuration**.
6. Explain that the file sets tone, review profile, path instructions, and path filters.
7. Select **Create merge request**.
8. Wait for CodeRabbit to review the configuration change.

> Screenshot 4.1 — MR showing the new .coderabbit.yaml file.

## 4.4 Test path instructions

Create a second branch from main containing the Lab 1 patch and the configuration:

~~~bash
git switch main
git pull --ff-only
git switch -c lab4-configured-review
cp .coderabbit.yaml.example .coderabbit.yaml
git apply labs/patches/lab-01-planted-bugs.patch
git add .coderabbit.yaml samples
git commit -m "test: compare configured CodeRabbit review"
git push -u origin lab4-configured-review
~~~

Open the MR using the same GitLab steps from section 4.3, with source branch lab4-configured-review and target main.

Compare the findings with Lab 1. Look specifically for references to the Bash and Python path instructions.

> Screenshot 4.2 — A finding that uses a path instruction.

## 4.5 Add coding guidelines

Create a third branch:

~~~bash
git switch main
git pull --ff-only
git switch -c lab4-guidelines
cat > /tmp/AGENTS.md <<'EOF'
All Bash scripts must support --help.
Python public functions require type hints.
Every script change must include a test plan in the MR description.
EOF
cp /tmp/AGENTS.md AGENTS.md
git add AGENTS.md
git commit -m "test: add repository coding guidelines"
git push -u origin lab4-guidelines
~~~

Open an MR into main. In the description, state which rules the branch adds. Test the guidelines with a follow-up branch that violates one rule.

> Screenshot 4.3 — CodeRabbit finding that cites a repository guideline.

## 4.6 What to record

- Which settings changed the review.
- Whether chill and assertive profiles differ.
- Whether path instructions appear in reasoning.
- Whether AGENTS.md is read and cited.
- Whether a configuration finding is correct or merely echoing the YAML.

## 4.7 Cleanup

Do not merge experimental configuration unless you want it as the repository's policy. Close or delete the experimental branches after recording results.

[← Lab 3](lab-03-incremental-reviews.md) · [Lab index](README.md) · [Main README](../README.md) · Next: [Lab 5](lab-05-finishing-actions.md)
