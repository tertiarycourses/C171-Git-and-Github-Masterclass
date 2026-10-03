# Lab 05 — Synchronise with Fetch, Pull and Push

**Exam domain:** Work with GitHub Repositories (10–15%)

**Objective:** Distinguish remote-tracking updates from working-branch integration and outbound publication.

## Scenario

A teammate changed the remote README while the learner was working locally.

## Deliverable

A synchronised local and remote repository with tracking-branch evidence

**Tools:** Git Bash or terminal, GitHub.com, GitHub Desktop Fetch/Pull/Push controls, Excel workbook

## Detailed procedure

1. Run git remote -v and git branch -vv; identify origin, the current branch and its upstream tracking branch.
2. Edit README.md directly on GitHub to simulate a teammate commit and record its remote commit ID.
3. Run git fetch origin and explain why the working files do not change even though origin/main advances.
4. Use git log HEAD..origin/main --oneline and git diff HEAD..origin/main to inspect the incoming commit before integration.
5. Run git pull --ff-only origin main and confirm the working branch advances without an unexpected merge commit.
6. Create a new local branch, make and commit one change, then push it with git push -u origin <branch-name>.
7. Run git branch -vv again and explain the new upstream relationship and ahead/behind indicators.
8. Use GitHub Desktop to Fetch origin, inspect History and compare the GUI state with git status -sb.
9. Record fetch, pull and push effects separately in the Excel command/decision log.

## Evidence workbook

Open `Lab-05-Evidence-Starter.xlsx` before you begin. Record every action, result, URL or screenshot reference, status, and reviewer note. The completed workbook is a worked example only; replace sample URLs with your own evidence.

## Acceptance criteria

- [ ] Fetch is distinguished from pull
- [ ] Incoming commit is inspected
- [ ] Upstream tracking is verified
- [ ] Local and remote histories match

## Completion evidence

Submit the completed Excel workbook together with any screenshots requested by the trainer. Never paste passwords, personal access tokens, private keys, recovery codes, or real secrets into the workbook.
