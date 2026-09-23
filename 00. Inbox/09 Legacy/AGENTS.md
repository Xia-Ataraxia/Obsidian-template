---
type: note
created_by: agent
authorship: agent
---
<!-- Parent: ../../AGENTS.md -->

# Repository Guidelines

## Project Overview

`00. Inbox/09 Legacy/` is the pre-taxonomy capture buffer for historical and
uncategorized Markdown notes. It is a landing zone for notes awaiting triage;
it is not an active project queue.

## Architecture & Data Flow

The vault flow is capture → triage → one canonical home. Use the current
Folders and Placement guideline to classify a legacy note by its `type` and content before
moving it. Captured external originals belong in `85. Raw/`, irrespective of
which agent or collector found them; `09 Legacy/` is not a substitute for Raw.

## Key Directories

- Notes sit at this directory root unless a nested content directory is added.
- The buffer may contain mixed historical captures awaiting classification.
- There is no source tree, generated output, or project-specific build
  artifact here.

## Commands

- Use `qmd` for read-only Korean/English search when available.
- Use the `obsidian` CLI only for an explicitly authorized move or rename so
  wikilinks are preserved.
- No build or test command is defined for this Markdown-only buffer.

## Code Conventions & Common Patterns

- Do not reorganize this buffer without explicit user instruction.
- Preserve each note's existing YAML provenance and defer metadata,
  authorship, and zone decisions to `../../90. Settings/01 Guideline/02. Properties.md`
  and `../../90. Settings/01 Guideline/03. Agent Permissions and Workflows.md`; do not introduce a competing provenance schema.
- Existing user-authored notes (including notes without `created_by`) require
  exact-path or deterministic-manifest authorization before edits. Preserve
  `created_by: user`, set `authorship: mixed` after an authorized contribution,
  and keep user-only `## Thinking` sections unchanged.
- A newly created agent note must use the policy's literal
  `created_by: agent` and `authorship: agent` fields.
- Search in both Korean and English. Move a note only after choosing its
  canonical destination and checking for collisions.

## Important Files

- `../../AGENTS.md` — vault-wide structure, ownership, and writing rules.
- `../../90. Settings/01 Guideline/01. Folders and Placement.md` — placement.
- `../../90. Settings/01 Guideline/02. Properties.md` and
  `../../90. Settings/01 Guideline/03. Agent Permissions and Workflows.md` — frontmatter and write authorization.
- `../../.oms/taxonomy.json` — machine-readable folder intent and zone
  routing.

## Runtime/Tooling Preferences

`qmd` is the preferred hybrid search tool; the `obsidian` CLI is the
wikilink-preserving move/rename tool when a move is authorized. Do not launch
Obsidian implicitly. Keep agent-ingest originals in `85. Raw/` and preserve
the existing note body when triaging.

## Testing & QA

- Before an authorized move, preflight destination collisions and verify
  wikilinks with the `obsidian` CLI.
- Check the note's frontmatter and body after any write; preserve existing
  provenance and `## Thinking`.
- Report unresolved classification or ownership conflicts instead of
  guessing. No automated build, test, or GUI check exists for this directory.
