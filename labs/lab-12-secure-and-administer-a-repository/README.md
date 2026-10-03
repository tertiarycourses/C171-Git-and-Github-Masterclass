# Lab 12 — Secure and Administer a Repository

**Exam domain:** Understand Privacy, Security and Administration (10–15%)

**Objective:** Apply identity, access, branch and supply-chain controls to a repository.

## Scenario

The release repository must prevent unsafe changes and surface security findings early.

## Deliverable

A repository security baseline with authentication comparison, access rationale, ruleset design, CODEOWNERS and scanning evidence

**Tools:** Authentication settings, PAT and SSH key configuration, security settings, Dependabot, code scanning, secret scanning concepts, roles, rulesets, Excel workbook

## Detailed procedure

1. Run git remote -v on the training clone and identify whether the remote is HTTPS or SSH, and which credential each protocol requires.
2. Create a fine-grained personal access token scoped to the training repository with the minimum permissions, note its expiry, and record why username-and-password authentication is no longer accepted for Git operations.
3. Generate an SSH key with ssh-keygen -t ed25519, add the public key to the GitHub account, verify with ssh -T git@github.com and switch the remote with git remote set-url origin.
4. Compare classic PAT, fine-grained PAT, SSH key and deploy key on scope, expiry, revocation and best-fit use case, and state where a deploy key is preferable for a CI server. Never record any token or private key in the workbook.
5. Review the account's 2FA configuration and compare security keys, TOTP apps, SMS and passkeys on strength and recovery risk.
6. Confirm repository visibility and explain public, private and internal visibility boundaries.
7. Review collaborator or team roles and apply least-privilege reasoning to sample personas using the read, triage, write, maintain and admin levels.
8. Design or configure a main-branch ruleset requiring a pull request and status checks.
9. Add a CODEOWNERS file that assigns a reviewer to a documentation path and verify that a pull request touching that path requests the owner.
10. Add a .gitignore entry for a build or secret path, then demonstrate with git rm --cached why an already-tracked file keeps being committed until it is untracked.
11. Enable the dependency graph and Dependabot alerts where available, and distinguish alerts, security updates and version updates.
12. Configure Dependabot version updates using .github/dependabot.yml on a branch and review through a pull request.
13. Enable default code scanning setup or review the instructor demonstration, and note the difference between default and advanced setup and the push, pull_request and schedule triggers.
14. Review secret-scanning and push-protection behaviour without committing a real secret.
15. Add a SECURITY.md file describing how to report a vulnerability, and locate where a security advisory would be raised.
16. Compare organisation-owned accounts, Enterprise Managed Users and personal accounts.
17. Record control, threat, evidence, owner and residual risk in Excel.

## Evidence workbook

Open `Lab-12-Evidence-Starter.xlsx` before you begin. Record every action, result, URL or screenshot reference, status, and reviewer note. The completed workbook is a worked example only; replace sample URLs with your own evidence.

## Acceptance criteria

- [ ] Authentication methods are compared with a chosen default
- [ ] Least privilege is justified
- [ ] Branch rule and CODEOWNERS are documented
- [ ] Security features are distinguished
- [ ] No real secret, token or key is recorded

## Completion evidence

Submit the completed Excel workbook together with any screenshots requested by the trainer. Never paste passwords, personal access tokens, private keys, recovery codes, or real secrets into the workbook.
