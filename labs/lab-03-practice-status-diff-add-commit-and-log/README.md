# Lab 03 — Practice Status, Diff, Add, Commit and Log

**Exam domain:** Work with GitHub Repositories (10–15%)

**Objective:** Move changes deliberately from working tree to staging area to local history and the remote.

## Scenario

The repository needs small, reviewable commits rather than one uncontrolled upload.

## Deliverable

A three-commit repository history with selective staging, clear messages and command evidence

**Tools:** Git Bash or terminal, GitHub Desktop, text editor, GitHub.com, Excel command workbook

## Detailed procedure

1. Run git status and classify each file as untracked, modified, staged or unchanged.
2. Make two different changes to README.md and create notes.txt so there are multiple changes to inspect.
3. Run git diff and explain the plus/minus lines, file headers and unstaged scope.
4. Stage only README.md with git add README.md, then run git status again and compare staged versus untracked content.
5. Run git diff --staged and verify exactly what the next commit will contain.
6. Create a focused commit with git commit -m followed by an outcome-based message.
7. Run git cat-file -p HEAD and identify the tree, parent, author and committer lines of the commit object you just created.
8. Correct the message of that unshared commit with git commit --amend, then compare the old and new commit IDs and explain why amending after pushing is unsafe.
9. Stage notes.txt and use git add -p on a later README change to practise selective hunk staging.
10. Start a third unrelated edit, run git stash push -m "wip", confirm with git status that the tree is clean, then inspect git stash list.
11. Run git stash pop, verify the parked edit returns to the working tree and record when stashing is preferable to an unfinished commit.
12. Create two more focused commits, then inspect them with git log --oneline --graph --decorate and git show HEAD.
13. Push the commits and verify the same commit IDs and messages on GitHub and in GitHub Desktop History.
14. Complete the Excel command log with actual commands, outputs, resulting states and commit URLs.

## Evidence workbook

Open `Lab-03-Evidence-Starter.xlsx` before you begin. Record every action, result, URL or screenshot reference, status, and reviewer note. The completed workbook is a worked example only; replace sample URLs with your own evidence.

## Acceptance criteria

- [ ] Three focused commits exist
- [ ] Staged content was reviewed
- [ ] Amend and stash effects are evidenced
- [ ] History matches locally and remotely
- [ ] Command log records actual outputs

## Completion evidence

Submit the completed Excel workbook together with any screenshots requested by the trainer. Never paste passwords, personal access tokens, private keys, recovery codes, or real secrets into the workbook.
