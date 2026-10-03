# Lab 04 — Create Branches and Merge Changes

**Exam domain:** Work with GitHub Repositories (10–15%)

**Objective:** Use branch pointers to isolate work and merge a completed change into main.

## Scenario

A navigation improvement must be developed without destabilising the main branch.

## Deliverable

A feature branch, separate commit history, local merge, annotated release tag and readable commit graph

**Tools:** Git Bash or terminal, GitHub Desktop branch visualisation, GitHub Releases, Excel evidence workbook

## Detailed procedure

1. Run git branch and identify the current branch marker and the relationship between HEAD and the branch name.
2. Create and switch to feature/navigation with git switch -c feature/navigation.
3. Add a Navigation section to README.md, inspect the diff, stage it and commit it on the feature branch.
4. Create a second feature commit so the branch has a visible line of development.
5. Run git log --oneline --graph --all --decorate and interpret the HEAD, main and feature pointers.
6. Switch to main and verify that the feature content is not yet present.
7. Merge feature/navigation into main and classify the result as fast-forward or a merge commit from the output and graph.
8. Read the merge output and write down what git rebase main would have produced instead, and why rebasing a branch that teammates have already pulled would rewrite shared history.
9. Create an annotated release tag with git tag -a v1.0.0 -m "Release 1.0.0", then run git show v1.0.0 and identify the tagger, date and message that a lightweight tag would not carry.
10. Delete the merged local feature branch with git branch -d feature/navigation.
11. Push main and the tag with git push origin --tags, then open the tag on GitHub and draft a release from it.
12. Compare the graph in GitHub Desktop History and record branch, merge, rebase-decision and tag evidence in Excel.

## Evidence workbook

Open `Lab-04-Evidence-Starter.xlsx` before you begin. Record every action, result, URL or screenshot reference, status, and reviewer note. The completed workbook is a worked example only; replace sample URLs with your own evidence.

## Acceptance criteria

- [ ] Feature work is isolated
- [ ] Merge result is explained
- [ ] Rebase safety rule is recorded
- [ ] Annotated tag exists locally and on GitHub
- [ ] Merged branch is safely deleted

## Completion evidence

Submit the completed Excel workbook together with any screenshots requested by the trainer. Never paste passwords, personal access tokens, private keys, recovery codes, or real secrets into the workbook.
