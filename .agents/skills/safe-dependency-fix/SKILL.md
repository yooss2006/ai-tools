---
name: safe-dependency-fix
description: Safely find, report, plan, and fix dependency/package vulnerabilities with OSV Scanner and ecosystem-native audit tools. Use when Codex is asked to scan dependencies for CVEs, run osv-scanner, npm audit, pnpm audit, yarn audit, pip-audit, govulncheck, cargo audit, bundle audit, Maven/Gradle/.NET vulnerability checks, remove vulnerable packages, update vulnerable dependencies, or produce a safe package vulnerability remediation plan. Default to dry-run analysis and require explicit user approval before changing files.
---

# Safe Dependency Fix

Find dependency vulnerabilities, propose the smallest safe remediation plan, and modify files only after explicit user approval.

## Response Language

Respond in Korean by default. Write dry-run reports, approval prompts, fix plans, final results, risk notes, and verification summaries in Korean unless the user explicitly requests another language.

## Core Rule

Run in two phases:

1. **Dry-run analysis**: inspect, run read-only scans, and report. Do not modify files.
2. **Approved fix**: modify files only after the user says exactly `수정 승인` or `실제 변경 진행`.

Do not treat "continue", "proceed", "go ahead", "확인해줘", "진행", or similar wording as fix approval.

`osv-scanner` installation approval is separate from vulnerability fix approval.

## Before Scanning

Read project instructions first: `AGENTS.md`, `CLAUDE.md`, `.codex/`, `.cursor/rules`, and nearby repo docs when present.

Detect project layout and package managers before running audit commands. For monorepos, identify workspaces first and report the scan scope.

Read `references/audit-tools.md` for ecosystem detection, audit commands, and OSV installation options.

## Phase 1: Dry-Run Analysis

In phase 1, never write files and never run commands that can change lockfiles, dependency folders, caches, manifests, or source files.

Forbidden before approval:

- `apply_patch` or any file write
- `npm install`, `npm update`, `npm audit fix`, `npm add`
- `pnpm install`, `pnpm update`, `pnpm audit --fix`, `pnpm add`
- `yarn install`, `yarn upgrade`, `yarn add`, `yarn audit --fix`
- `bun install`, `bun update`, `bun add`
- `pip install --upgrade`, `poetry update`, `pipenv update`
- `go get -u`, `cargo update`, `bundle update`
- deleting lockfiles, dependency directories, or caches

Allowed in dry-run:

- read project files
- inspect dependency trees with read-only commands
- run `osv-scanner scan source -r .` when installed
- run ecosystem-native audit commands from `references/audit-tools.md`
- run read-only outdated/version commands when needed for planning

If `osv-scanner` is missing, stop before the OSV scan and report it. Ask the user to choose:

1. install `osv-scanner` and then run OSV scan
2. skip OSV scan and continue with ecosystem-native audit tools only

If the user chooses installation, detect the OS and use the platform-appropriate method from `references/audit-tools.md`. After installation, continue phase 1 only; still do not fix vulnerabilities without `수정 승인` or `실제 변경 진행`.

## Phase 1 Report

Report in this shape:

- commands run
- tools missing or skipped
- vulnerability summary
- vulnerable package and current/fixed versions
- direct dependency vs transitive dependency
- likely parent package for transitive vulnerabilities
- minimum safe change candidate
- items likely fixable without `resolutions`/`overrides`
- items that may require `resolutions`/`overrides` and why
- expected fix risk
- exact commands planned for phase 2 verification
- explicit note that no files were changed

## Fix Planning Rules

Prefer the smallest change that removes the vulnerability:

1. Update a direct dependency to the minimum non-vulnerable version when that fixes the issue.
2. For transitive dependencies, first update the nearest parent dependency that brings in a fixed version.
3. Prefer patch updates over minor updates, and minor updates over major updates, when they remove the vulnerability.
4. Respect exact pins, constraints, `overrides`, and `resolutions`; treat changes to them as higher risk.
5. Use `resolutions`, `overrides`, constraints, or replacement rules only as a last resort, and explain why parent/direct updates are insufficient.
6. Do not change application behavior or make broad dependency refreshes unrelated to the vulnerability.

Resolution/override gate:

Before adding any `resolutions`, `overrides`, constraints, or replacement rules:

1. Apply the approved direct or nearest-parent dependency updates first.
2. Recompute the lockfile.
3. Re-run the audit.
4. Add a resolution only for vulnerabilities that still remain.
5. Add resolutions one at a time, re-running install and audit after each one.
6. Stop as soon as the audit is clean.

Forbidden: speculative, defensive, batch, or broad resolutions for packages not still reported vulnerable after direct/parent updates.

Risk labels:

- low: lockfile-only or patch-level change within an existing allowed range
- medium: minor update, parent dependency update, or package-manager resolution change with limited surface
- high: major update, framework/runtime update, peer dependency shift, or forced override/resolution

## Phase 2: Approved Fix

Start only when the user says exactly `수정 승인` or `실제 변경 진행`.

Apply the approved plan with the minimum file changes. If new scan results or dependency resolution conflicts require a materially different plan, stop and ask for a new approval instead of improvising.

After changes:

- rerun `osv-scanner scan source -r .` when available
- rerun ecosystem-native audit commands
- run existing lint/build/test commands when present
- do not create new tests unless the user explicitly asks
- report changed files, package/version changes, use of `resolutions`/`overrides`, scan results, lint/build/test results, and remaining compatibility risks
