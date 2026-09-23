---
type: note
created_by: agent
authorship: agent
---
<!-- Parent: ../AGENTS.md -->

# Repository Guidelines

## Project Overview

`15. Work/` is the active-work root. It separates finite Projects, ongoing Areas, inactive material, and project-less Tasks while keeping project-linked work beside its owner.

- `01 Project/` contains finite outcomes and one same-name hub per project.
- `02 Area/` contains ongoing responsibilities and one same-name hub per area.
- `03 Archive/` contains inactive Project/Area material preserved by year or context.
- `04 Tasks/` is the fallback for project-less notes with `type: task`; linked tasks stay in their owning Project or Area folder.

## Architecture & Data Flow

Project and Area hubs use `<folder>/<folder>.md`. Dated activity records use `YYYY-MM-DD <name>.md`; use `type: meeting` for meetings and `type: log` for other activity. The nearest nested `AGENTS.md` adds local architecture and sensitivity rules; it does not replace this contract.

A Task is discovered by `type: task`, not by folder. A `project` relation keeps it in its Project or Area folder; only project-less tasks fall back to `04 Tasks/`. Completion is recorded through `done`/`gtd` fields in place and never by moving the file to `03 Archive/`.

The external-original route is `../85. Raw/`, regardless of which collector produced the capture. Source-based engineering material belongs in `../30. Literature Notes/`, self-contained engineering knowledge in `../40. Permanent Notes/`, and decisions in the owning Work folder or `../90. Settings/01 Guideline/`.

## Key Directories

| Relative path | Contract |
|---|---|
| `01 Project/<name>/` | Active project hub, dated records, specifications, research, and project-local contracts. |
| `02 Area/<name>/` | Active area hub, operating records, and area-local policies or precedents. |
| `03 Archive/` | Governed archive destination for inactive Project/Area material; do not use it for completed Tasks. |
| `04 Tasks/` | Flat fallback only for tasks without a project relation. |

## Commands

- Use `qmd` for Korean/English vault search and `obsidian` CLI when a wikilink or vault property needs verification.
- Inspect placement and changed paths with `git status -- <relative-path>` before reporting work.
- Commit and push at the end of every task that changes a file, staging only the paths you touched (`git add -- "<path>"`). Never `git add -A`/`git add .`/`git commit -a` — unrelated user edits in the tree stay uncommitted. See [[04. Applications and Integrations#Git and GitHub]] for the full contract.
- Complete a Task by updating its `done`/`gtd` fields in place; do not move it to `03 Archive/`.

## Code Conventions & Common Patterns

- A Project/Area hub uses `type: project` and omits `status`; folder placement denotes active state.
- Discover Tasks by `type: task`, not by folder. `project` relations determine whether a task belongs to a Project/Area or falls back to `04 Tasks/`.
- `agentWritable` grants zone and new-file authority, never ownership of an existing note. Editing a user-authored note requires exact-path or deterministic-manifest authorization.
- Preserve existing YAML provenance and protected `## Thinking` sections. Follow the authoritative metadata/agent policy and current session instructions for new-note provenance; this guide does not define a competing schema.
- Before changing MOC relationships or membership, read `../90. Settings/01 Guideline/16. MOC.md`. Folders owns physical placement; Properties owns metadata serialization including tags. The `16` filename is not a precedence tier.

## Important Files

- `../AGENTS.md` — vault-wide taxonomy, metadata, zone, and writing rules.
- `../90. Settings/01 Guideline/01. Folders and Placement.md` — physical placement.
- `../90. Settings/01 Guideline/02. Properties.md` — frontmatter and authorship policy.
- `../90. Settings/01 Guideline/16. MOC.md` — note-relationship policy, independent of folder placement.
- `../90. Settings/01 Guideline/03. Agent Permissions and Workflows.md` — agent routing and writable-zone policy.
- `01 Project/AGENTS.md` and `02 Area/AGENTS.md` — child contracts for the two active Work branches.

## Runtime/Tooling Preferences

This directory is a vault knowledge structure, not one executable codebase. Prefer `qmd` for retrieval and the `obsidian` CLI for authorized link or property checks. Do not launch Obsidian implicitly. Project-specific build, test, or deployment commands belong in the relevant nested project guide and its source repository.

## Testing & QA

QA is structural: confirm the target folder and nearest contract, inspect frontmatter and task fields, verify links with vault tooling, and preserve user-owned content and protected `## Thinking`. There is no application test suite at this Work root.
