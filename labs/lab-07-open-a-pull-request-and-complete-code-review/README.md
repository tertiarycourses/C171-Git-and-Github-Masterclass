# Lab 07 — Open a Pull Request and Complete Code Review

**Exam domain:** Collaborate Using GitHub (10–15%)

**Objective:** Connect command-line branch work to a traceable pull request, review and merge.

## Scenario

A learner onboarding checklist requires peer review and issue traceability before release.

## Deliverable

A linked issue, pushed branch, reviewed pull request, controlled merge and local clean-up

**Tools:** Git Bash, GitHub pull requests, GitHub Desktop, Excel evidence workbook

## Detailed procedure

1. Create an issue describing the onboarding-checklist improvement and its acceptance criteria.
2. Create feat/onboarding-checklist, make a focused change and commit it after reviewing git diff --staged.
3. Push the branch with -u and verify the upstream tracking relationship.
4. Open a pull request whose body uses Closes #<issue-number> and explains verification evidence.
5. Inspect the Commits, Checks and Files changed views; request a review and leave one constructive comment.
6. Apply the feedback in a new local commit and push it; verify the existing pull request updates automatically.
7. Merge only after review/check expectations pass, then delete the remote branch.
8. Switch to main locally, pull with --ff-only, verify the linked issue closed and delete the local branch.
9. Capture issue, PR, review, check, merge and clean-up evidence in Excel.

## Evidence workbook

Open `Lab-07-Evidence-Starter.xlsx` before you begin. Record every action, result, URL or screenshot reference, status, and reviewer note. The completed workbook is a worked example only; replace sample URLs with your own evidence.

## Acceptance criteria

- [ ] PR links to issue
- [ ] Review changes the branch
- [ ] Main is refreshed locally
- [ ] Both branch copies are cleaned up

## Completion evidence

Submit the completed Excel workbook together with any screenshots requested by the trainer. Never paste passwords, personal access tokens, private keys, recovery codes, or real secrets into the workbook.
