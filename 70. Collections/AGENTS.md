---
type: note
created_by: user
authorship: mixed
---
<!-- Parent: ../AGENTS.md -->

# Repository Guidelines

## Project Overview
`70. Collections/` is the user-curated catalog for reference objects and directory-like notes: people, prompts, MOCs, music, places, organizations, selected GitHub tools, and channels. It is user-only by default and inherits authorization and provenance rules from `../AGENTS.md`.

External originals remain in `../85. Raw/` regardless of collector. Terminology belongs to `../50. AI/02 Terminologies/`, not this collection; source interpretation belongs to `../30. Literature Notes/`.

## Architecture & Data Flow
Collections are canonical homes for selected entities and reusable objects, not an unattended capture sink. `08 Github/` and `09 Channel/` are explicit user-request exceptions described by `../90. Settings/01 Guideline/03. Agent Permissions and Workflows.md`; automated or unreviewed external capture uses `85. Raw/`.

## Key Directories
| Directory | Role |
| --- | --- |
| `01 People/` | People profiles (`type: people`) |
| `02 Prompt/` | LLM prompts; new prompt files use `.prompt.md` |
| `03 MoC/` | Numbered, flat Maps of Content |
| `04 Music/` | Music and playlist notes (`type: music`) |
| `05 Places/` | Place notes (`type: places`) |
| `07 Organization/` | Organization profiles (`type: organization`) |
| `08 Github/` | User-selected reusable software/tool objects (`type: tool`) with GitHub provenance |
| `09 Channel/` | Publishing-channel entities (`type: channel`), separate from people and organizations |
| `10 Flowers/` | Flower cards (`type: flower`) with `image` cover |

## Commands
No collection-specific build or test command exists. Use `qmd` for hybrid search and the authorized `obsidian` CLI for property/link checks under `../AGENTS.md`; do not launch Obsidian implicitly. Parent-level verification owns indexing and final checks.

## Code Conventions & Common Patterns
- Existing notes require exact-path or deterministic-manifest authorization. Preserve YAML provenance; authorized edits to user-created notes keep `created_by: user` and set `authorship: mixed`.
- Follow type and field serialization in `../90. Settings/01 Guideline/02. Properties.md` and physical placement in `01. Folders and Placement.md` rather than copying mutable enums here.
- People links use verified notes. MOC files stay flat and numbered under `03 MoC/` (Folders owns that physical home). Before changing MOC relationships or membership, read `../90. Settings/01 Guideline/16. MOC.md`; tier, axis, and dual-MOC rules belong there. The `16` filename is not a precedence tier.
- Do not route Excalidraw drawings or plugin assets here. Canonical root is `../90. Settings/07 Excalidraw`. GitHub notes use the current `tool` contract and source provenance; channel notes remain distinct from people and organizations.
- Raw external originals are never routed here merely because a collector produced them.
- Preserve any `## Thinking` section as user-only and report conflicts rather than introducing a competing provenance schema.

## Important Files
- `../AGENTS.md` — vault hierarchy, ownership, and authorization.
- `../90. Settings/01 Guideline/01. Folders and Placement.md` — collection placement.
- `../90. Settings/01 Guideline/02. Properties.md` — collection types and fields.
- `../90. Settings/01 Guideline/16. MOC.md` — MOC relationship policy, independent of folder placement.
- `../90. Settings/01 Guideline/03. Agent Permissions and Workflows.md` — user-only boundary and explicit exceptions.
- `../90. Settings/01 Guideline/04. Applications and Integrations.md` — application roles, interfaces, and integration policy boundaries.
- `../90. Settings/01 Guideline/15. Templates.md` — template categories, routes, and engine.
- `../.oms/taxonomy.json` — machine-readable routing intent.

## Applications and Runtime References
Use `qmd` for Korean/English hybrid search. Use `obsidian` only for authorized vault CRUD/property/link checks. Excalidraw, Bases, and other plugin-managed surfaces follow the application roles, interfaces, and integration policy in `04. Applications and Integrations.md`; this guide does not prescribe a parallel schema.

## Testing & QA
Confirm the note is a selected collection object, has one canonical home, uses the policy-defined type and provenance, and links only verified entities. Check raw-vs-curated routing, MOC placement, plugin-managed files, and unchanged user-only sections. Parent-level verification covers the changed-path allowlist and link/index checks.

<!-- MANUAL: -->
