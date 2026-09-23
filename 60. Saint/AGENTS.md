---
type: note
created_by: user
authorship: user
---
<!-- Parent: ../AGENTS.md -->

# Repository Guidelines

## Project Overview

If the adopter keeps a faith root, `60. Saint/` is the vault's faith and spiritual-life area. It contains sermon
notes, Quiet Time (QT) reflections, prayers, Bible study, and worship records.
Treat this user-owned material with respect and preserve the writer's voice.

## Architecture & Data Flow

The area separates source and reflection by practice: sermon records capture
preaching, QT records capture daily devotion, prayer records capture requests
and gratitude, Bible records organize study by book or passage, and worship
records preserve praise and service material. Scripture and personal
reflection remain distinguishable inside each note.

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `01 Sermon/` | Sermon notes and reflections |
| `02 QT/` | Quiet Time daily devotionals |
| `03 Pray/` | Prayer requests and records |
| `04 Bible/` | Bible study and verse notes |
| `05 Worship/` | Worship and praise notes |

## Commands

- No build or test command is defined for this Markdown-only area.
- Use `qmd` for read-only bilingual search. Use the `obsidian` CLI only for
  an explicitly authorized move or rename that must preserve wikilinks.

## Code Conventions & Common Patterns

- Faith-specific properties include `church`, `pray`, `bible`, and `chapter`;
  preserve existing frontmatter and defer metadata rules to
  `../90. Settings/01 Guideline/02. Properties.md`.
- Bible verses use blockquotes with Korean and English text plus a book
  wikilink, for example:

  > [[Exodus 15]]:24
  > 백성이 모세에게...
  > And the people grumbled...

- Do not rewrite, summarize, or reinterpret spiritual reflections. Existing
  notes in this user-only area require exact-path or deterministic-manifest
  authorization before edits; an authorized agent contribution preserves
  `created_by: user` and sets `authorship: mixed`.
- A new agent-created note requires an explicit user request and the policy's
  literal `created_by: agent` and `authorship: agent` fields. Never add a
  competing provenance format.
- Keep `## Thinking` sections user-only.

## Important Files

- `../AGENTS.md` — vault-wide ownership and note-writing rules.
- `../90. Settings/01 Guideline/01. Folders and Placement.md` — Saint
  placement and directory taxonomy.
- `../90. Settings/01 Guideline/02. Properties.md` and
  `../90. Settings/01 Guideline/03. Agent Permissions and Workflows.md` — frontmatter and authorization.
- `../.oms/taxonomy.json` — machine routing metadata.

## Runtime/Tooling Preferences

Use `qmd` for retrieval and the `obsidian` CLI for authorized
wikilink-preserving moves. Do not launch Obsidian implicitly. Do not use an
automated summarizer or faith-specific content transformation in place of
the user's note.

## Testing & QA

- Review the changed path, frontmatter, verse blockquotes, wikilinks, and
  body for accidental voice or reflection changes.
- Verify any authorized move for collisions and links before finalizing it;
  this guide itself requires no build or test run.
- If machine routing metadata disagrees with this guide, follow
  `../AGENTS.md` and Folders and Placement (faith and spiritual life);
  reconcile the machine intent separately rather than inventing a local override.
