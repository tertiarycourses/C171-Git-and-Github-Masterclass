# Lab 02 — Create and Clone a Training Repository

**Exam domain:** Understand Git and GitHub Basics (25–30%)

**Objective:** Create a remote repository and understand how clone establishes a local copy and origin remote.

## Scenario

The onboarding team needs a safe repository that every later lab can reuse.

## Deliverable

A public northstar-git-lab repository cloned locally with a verified origin remote

**Tools:** GitHub.com, Git Bash or terminal, GitHub Desktop, Markdown, Excel evidence workbook

## Detailed procedure

1. Create a public repository named northstar-git-lab with README.md and an appropriate .gitignore template.
2. Copy the HTTPS clone URL and identify the owner, repository name and protocol in the URL.
3. In Git Bash or a terminal, choose a training folder and run git clone <repository-url>.
4. Enter the cloned folder and run git status -sb to confirm the current branch and clean working tree.
5. Run git remote -v and explain why origin normally has both fetch and push URLs.
6. Open the same local repository in GitHub Desktop and locate the Current branch, History and Fetch origin controls.
7. Edit README.md with a project purpose, prerequisites and task list; save without committing.
8. Compare the changed-file view in GitHub Desktop with git status and git diff in Git Bash.
9. Record the remote URL, local folder, current branch and observed file state in Excel.

## Evidence workbook

Open `Lab-02-Evidence-Starter.xlsx` before you begin. Record every action, result, URL or screenshot reference, status, and reviewer note. The completed workbook is a worked example only; replace sample URLs with your own evidence.

## Acceptance criteria

- [ ] Remote repository exists
- [ ] Local clone has origin
- [ ] CLI and Desktop show the same change
- [ ] Workbook records paths and states

## Completion evidence

Submit the completed Excel workbook together with any screenshots requested by the trainer. Never paste passwords, personal access tokens, private keys, recovery codes, or real secrets into the workbook.
