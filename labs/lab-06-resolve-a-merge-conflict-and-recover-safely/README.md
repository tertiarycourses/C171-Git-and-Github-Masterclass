# Lab 06 — Resolve a Merge Conflict and Recover Safely

**Exam domain:** Work with GitHub Repositories (10–15%)

**Objective:** Diagnose conflict markers, complete a merge and choose a safe recovery command for common mistakes.

## Scenario

Two contributors changed the same README sentence and Git cannot decide which version to keep.

## Deliverable

A resolved merge conflict plus a tested restore, unstage, reset, revert and reflog recovery decision record

**Tools:** Git Bash or terminal, GitHub.com, GitHub Desktop conflict helper, text editor, Excel workbook

## Detailed procedure

1. Change one selected README sentence locally but do not push it yet.
2. Change the same sentence differently on GitHub and commit the remote edit.
3. Commit the local version, then run git pull and observe the conflict message without using a destructive reset.
4. Run git status and identify the unmerged path and the merge currently in progress.
5. Open README.md, locate the conflict markers and explain the current, separator and incoming sections.
6. Resolve the sentence deliberately, remove all markers, stage README.md and complete the merge commit.
7. Push the resolved history and verify both original commits plus the resolution in the graph.
8. Create a harmless unstaged edit and practise git restore; stage another harmless edit and practise git restore --staged.
9. On a throwaway branch, make one local commit and undo it with git reset --soft HEAD~1; run git status and record that the change is still staged.
10. Recommit it, then run git reset --hard HEAD~1 on that same throwaway branch and record that both the commit and the working-tree change are gone.
11. Run git reflog, locate the SHA of the commit you just discarded, and recover it with git switch -c rescue <sha>; confirm the content is back.
12. Create and push a harmless commit on main, then reverse it safely with git revert <commit> and push the revert.
13. Record the conflict cause, resolution decision and a comparison of restore, restore --staged, reset --soft, reset --hard, revert and reflog by the state each one changes and whether the history was shared.

## Evidence workbook

Open `Lab-06-Evidence-Starter.xlsx` before you begin. Record every action, result, URL or screenshot reference, status, and reviewer note. The completed workbook is a worked example only; replace sample URLs with your own evidence.

## Acceptance criteria

- [ ] Conflict markers are removed
- [ ] Merge completes without lost history
- [ ] Reset variants are distinguished by effect
- [ ] A discarded commit is recovered via reflog
- [ ] Resolution and revert are evidenced

## Completion evidence

Submit the completed Excel workbook together with any screenshots requested by the trainer. Never paste passwords, personal access tokens, private keys, recovery codes, or real secrets into the workbook.
