---
type: note
created_by: agent
authorship: agent
---
<!-- Parent: ../AGENTS.md -->

# Repository Guidelines

## Project Overview
`03 Meetings/` contains meeting records derived from conversations, interviews, seminars, and working sessions. It inherits the user-only boundary of `../AGENTS.md`; this file is a hierarchy contract, not a meeting record.

## Architecture & Data Flow
Keep recorded source facts and participant statements distinct from later interpretation. Existing meeting notes use the established section flow:

1. `## Thinking` — user-only reflection; agents never write here.
2. `## Discussed` — recorded discussion and, when authorized, agent analysis.
3. `## Next Steps` — follow-up actions or questions.
4. `## References` — supporting links and notes.

Meetings owned by a project or area stay in that owning `../../15. Work/` folder. External originals remain under `../../85. Raw/`; this directory is for the meeting record and its interpretation.

## Key Directories
Meeting notes are a flat corpus in this directory. `AGENTS.md` is exempt from meeting filename and `type: meeting` rules and retains its hierarchy-document metadata.

## Commands
No meeting-specific build or test command exists. Use `qmd` for search and the `obsidian` CLI for authorized link/property checks under `../../AGENTS.md`; do not launch Obsidian implicitly. Parent-level verification owns indexing and final checks.

## Code Conventions & Common Patterns
- New meeting records use scalar `type: meeting`; use `date_meet`, `speaker`, and `participants` only when supported by the record.
- Use a descriptive filename ending in `.meeting.md`; preserve established date prefixes. Link People names only when the corresponding note is verified.
- Existing user-authored notes require exact-path or deterministic-manifest authorization. Preserve `created_by: user`, set `authorship: mixed` after an authorized edit, and preserve all existing YAML provenance.
- Preserve `## Thinking` verbatim. Do not add alternate provenance fields; follow `../../90. Settings/01 Guideline/02. Properties.md` and `03. Agent Permissions and Workflows.md` when instructions conflict.
- Use relative paths and retain the distinction between source record, discussion, and interpretation.

## Important Files
- `../AGENTS.md` — Literature Notes scope and note-family rules.
- `../../AGENTS.md` — vault ownership and authorization.
- `../../90. Settings/01 Guideline/01. Folders and Placement.md` — placement SSOT.
- `../../90. Settings/01 Guideline/02. Properties.md` — meeting type and fields.
- `../../90. Settings/01 Guideline/03. Agent Permissions and Workflows.md` — user-only zone and provenance.
- `../../70. Collections/01 People/` — verified People-note destination.

## Runtime/Tooling Preferences
Use the vault-wide `qmd` search and authorized `obsidian` CLI surfaces from the parent guides. The four Policy documents under `../../90. Settings/01 Guideline/` are the SSOT; this guide does not duplicate their mutable metadata enums.

## Testing & QA
Check filename suffix/date prefix, scalar meeting type, evidence-backed participants, source-vs-interpretation separation, People links, and unchanged `## Thinking`. Confirm authorization and frontmatter preservation, and ensure no project-owned or raw route was introduced. Parent-level verification covers the changed-path allowlist and link checks.
