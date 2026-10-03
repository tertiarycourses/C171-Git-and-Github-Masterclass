# Lab 09 — Build and Diagnose a GitHub Actions Check

**Exam domain:** Apply Modern Development Practices (10–15%)

**Objective:** Automate a repeatable pull-request validation and use run evidence to diagnose failure.

## Scenario

Every documentation pull request must prove that README.md and SECURITY.md exist.

## Deliverable

A pull-request Actions workflow with successful and failed run evidence

**Tools:** GitHub Actions, YAML, Git Bash, workflow logs, Excel workbook

## Detailed procedure

1. Inspect Actions workflow, event, job, step, action and runner relationships.
2. Create .github/workflows/validate.yml on a branch with pull_request and workflow_dispatch triggers.
3. Add checkout and shell-validation steps for README.md and SECURITY.md.
4. Commit and push the workflow branch, then open a pull request to trigger the run.
5. Inspect the run, job and step logs and record the commit SHA that the run evaluated.
6. Deliberately change the validation condition in a safe branch to produce one failed run.
7. Use the log evidence to correct the workflow and push a new commit.
8. Verify the pull request updates to a passing check and capture both run URLs.
9. Record trigger, job, failing step, diagnosis, correction and final status in Excel.

## Evidence workbook

Open `Lab-09-Evidence-Starter.xlsx` before you begin. Record every action, result, URL or screenshot reference, status, and reviewer note. The completed workbook is a worked example only; replace sample URLs with your own evidence.

## Acceptance criteria

- [ ] Workflow triggers on PR
- [ ] Failure is diagnosed from logs
- [ ] Corrected run passes
- [ ] Run URLs and SHAs are captured

## Completion evidence

Submit the completed Excel workbook together with any screenshots requested by the trainer. Never paste passwords, personal access tokens, private keys, recovery codes, or real secrets into the workbook.
