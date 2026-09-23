---
type: note
created_by: user
authorship: mixed
---
<!-- Parent: ../AGENTS.md -->

# Repository Guidelines

## Project Overview
`30. Literature Notes/` stores thinking notes derived from external sources: research, reviews, and meetings. It is a user-only zone and inherits the vault-wide placement, metadata, provenance, and authorization rules from `../AGENTS.md`.

External originals stay in `../85. Raw/` regardless of who collected them. This directory holds interpretation and synthesis, not an alternate raw-capture route. A project- or area-owned record stays with its owning `15. Work/` folder.

## Architecture & Data Flow
The flow is source evidence → literature interpretation → (when the user refines it) a permanent note or publication. Keep one canonical home and preserve the distinction between source-grounded material and personal interpretation.

The three child directories are separate note families.

## Key Directories
| Directory | Role |
| --- | --- |
| `01 Researches/` | Research and paper-analysis notes (`type: research`) |
| `02 Reviews/` | Reviews with source-grounded synthesis and personal evaluation (`type: review`) |
| `03 Meetings/` | Meeting records (`type: meeting`); see its nested guide |

## Commands
No vault build or test command is defined for this note family. Use `qmd` for hybrid vault search and the `obsidian` CLI for authorized vault/link checks as described by `../AGENTS.md`; do not launch Obsidian implicitly. The parent guide owns any post-edit indexing or verification procedure.

## Code Conventions & Common Patterns
- Let `../90. Settings/01 Guideline/01. Folders and Placement.md` decide physical placement and `02. Properties.md` decide type and frontmatter; do not copy mutable type or field enumerations here.
- Before changing MOC relationships or membership, read `../90. Settings/01 Guideline/16. MOC.md`. The `16` filename is not a precedence tier.
- Preserve existing YAML provenance. Existing user-authored notes require exact-path or deterministic-manifest authorization; an authorized edit keeps `created_by: user` and records `authorship: mixed`.
- Use the canonical `source`/`up` links and type-specific fields from Properties. Meeting fields and section boundaries belong to `03 Meetings/AGENTS.md`.
- Treat any `## Thinking` section as user-only and preserve it verbatim. Do not create a competing provenance schema; conflicts with session instructions are reported to the owner.
- Use relative paths in shared guidance.

## Important Files
- `../AGENTS.md` — vault hierarchy, ownership, and authorization.
- `../90. Settings/01 Guideline/01. Folders and Placement.md` — physical placement.
- `../90. Settings/01 Guideline/02. Properties.md` — types, fields, and authorship SSOT.
- `../90. Settings/01 Guideline/16. MOC.md` — note-relationship policy, independent of folder placement.
- `../90. Settings/01 Guideline/03. Agent Permissions and Workflows.md` — agent zones and provenance.
- `../.oms/taxonomy.json` — machine-readable folder intent and agent-writable flags.

## Runtime/Tooling Preferences
`qmd` is the preferred hybrid search tool; `obsidian` is the vault CRUD/property/link-check surface. Policy documents under `../90. Settings/01 Guideline/` outrank this guide, and raw ingestion remains owned by the `../85. Raw/` pipeline.

## Testing & QA
Before handoff, check the note family and canonical home, source links, scalar type, authorization, and unchanged `## Thinking` content. Review the diff for frontmatter/provenance preservation and confirm that no raw-capture route was introduced. Parent-level verification covers the changed-path allowlist and any indexing or link checks.
