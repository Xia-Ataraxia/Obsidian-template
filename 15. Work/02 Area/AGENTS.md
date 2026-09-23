---
type: note
created_by: agent
authorship: agent
---
<!-- Parent: ../AGENTS.md -->

# Repository Guidelines

## Project Overview

`02 Area/` contains ongoing responsibilities with no finite completion point. Each Area owns a semantic-name folder and a same-name hub; dated records, policies, and precedents stay with that responsibility.

## Architecture & Data Flow

An Area hub is `<area>/<area>.md`. Dated operating records use `YYYY-MM-DD <area>.md` with `type: log`, or `type: meeting` for a meeting. Policies and precedents belong to their owning Area. Cross-project source-based engineering material belongs in `../../30. Literature Notes/`; self-contained engineering knowledge belongs in `../../40. Permanent Notes/`. External originals remain in `../../85. Raw/` regardless of collector.

Complete Tasks through `done`/`gtd` fields in place. Area lifecycle is separate from Task completion and does not justify moving a task to an archive folder.

## Key Directories

| Relative path | Contract |
|---|---|
| `<area>/<area>.md` | Area hub and navigation entry. |
| `<area>/YYYY-MM-DD <area>.md` | Dated operating record; use `type: log`, or `type: meeting` for a meeting. |
| Nested `AGENTS.md` | Area-specific boundaries and sensitivity rules; follow the nearest one. |

## Commands

- Use `qmd` for vault search and `obsidian` CLI for wikilink or property verification.
- Inspect the nearest Area hub and nested contract before changing an operating record; do not turn a neighboring Area into a shared source of truth.
- Complete Tasks through `done`/`gtd` fields in place. Area lifecycle is separate from Task completion and does not justify moving a task to an archive folder.
- End every file-changing task in an area folder with a commit and a push, staging only the paths you touched (`git add -- "<path>"`). Never stage the whole tree. See [[04. Applications and Integrations#Git and GitHub]] for the full contract.

## Code Conventions & Common Patterns

- Hubs use `type: project` and omit `status`.
- Keep dated records as evidence. Update a current name note or create a new record instead of rewriting historical wording.
- Existing user-authored notes require exact-path or deterministic-manifest authorization. Preserve YAML provenance and protected `## Thinking` sections.
- Follow the authoritative metadata/agent policy and current session instructions for new-note provenance. This guide does not create a competing schema or override the nearest local contract.

## Important Files

- `../AGENTS.md` — Work-level routing, task state, and ownership rules.
- `../../AGENTS.md` — vault taxonomy, metadata, writable zones, and protected-note rules.
- `../../90. Settings/01 Guideline/01. Folders and Placement.md`, `02. Properties.md`, and `03. Agent Permissions and Workflows.md` — authoritative policy sources.

## Runtime/Tooling Preferences

Prefer `qmd` for retrieval and the `obsidian` CLI for authorized link or property checks. Do not launch Obsidian implicitly. Scheduled, plugin, company, and other operational tooling belongs to the owning Area contract or its source project.

## Testing & QA

QA is structural: verify the Area path, hub, note type, project relation where used, and links with vault tooling; keep user-authored content and dated evidence intact. Scheduled, plugin, company, and other operational checks belong to their own Area contracts and source projects rather than this shared guide.
