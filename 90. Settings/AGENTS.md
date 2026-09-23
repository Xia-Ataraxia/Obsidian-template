---
type: note
created_by: agent
authorship: agent
---
<!-- Parent: ../AGENTS.md -->

# Repository Guidelines

## Project Overview
`90. Settings/` is the user-only vault infrastructure layer: policy documents, templates, home and index pages, Bases views, operational guidelines, and the canonical Excalidraw drawing/asset root. Changes can affect the whole vault, so exact-path authorization and the policy precedence in `01 Guideline/` apply.

## Architecture & Data Flow
The canonical rule set is five documents across four precedence tiers: `01. Folders and Placement.md` → `02. Properties.md` → `03. Agent Permissions and Workflows.md` → peer `04. Applications and Integrations.md` and `15. Templates.md` at tier 4. The `15` filename is not a fifth precedence or a new priority. `16. MOC.md` is independent relationship policy (relationships created through notes); it is not part of that five-document operational subset, and the `16` filename is not a precedence tier or a new priority. `05. Writing Style.md` separately owns the user's prose and Markdown preferences; its number is not a policy precedence. Operational guidelines remain subordinate to the policy documents. The responsibility map in `01. Folders and Placement.md` assigns each rule to one current owner. Guides contain effective rules only; superseded definitions and migration narratives belong in Git history, with change rationale in commit messages. Do not require new ADR writing; historical decision records are preserved. Project decisions stay with the owning `15. Work/` project; vault/system decisions belong in `01 Guideline/`. Vault Git workflow is the current-branch commit and push; policy owner is [[04. Applications and Integrations#Git and GitHub]].

## Key Directories
| Directory | Role |
| --- | --- |
| `01 Guideline/` | Current rules: five policy documents across four precedence tiers and Writing Style; authority follows the Folders and Placement responsibility map. ADR writing is not a live procedure; historical decision records remain. |
| `02 Templates/` | Template root. Observed Templater `templates_folder` is `90. Settings/02 Templates`; folder templates are Daily / Weekly / Monthly / Quarterly / Yearly under `auto/` (no Dashboard folder template). Placement routes: `manual/`, `auto/`, `zotero/` (`zotero/` optional, ships empty). Observed extra dirs under the same root: `agent/`, `obsidian web clipper/` — contracts in `01 Guideline/15. Templates.md`; do not invent a Templater route or move files. |
| `03 Home/` | Home dashboards and landing pages |
| `04 Index/` | Index and navigation notes |
| `05 Bases/` | Obsidian Bases (`.base`) views |
| `07 Excalidraw/` | Canonical Excalidraw drawings and plugin assets. Not a Templater route and not a Collections catalog. |

## Commands
No Settings-specific build or test command exists. Use the vault-wide `qmd` search and authorized `obsidian` CLI surfaces from `../AGENTS.md`; do not launch Obsidian implicitly. Parent-level verification owns any indexing, link, or schema checks. Git: stay on this checkout's current branch, stage only task-owned paths, then commit and push the configured remote/branch per [[04. Applications and Integrations#Git and GitHub]]. Do not create branches or worktrees for Settings note edits; open a PR only when the user explicitly requests one for that task.

## Code Conventions & Common Patterns
- Read all applicable policy documents before changing structure, metadata, agent zones, plugins, templates, or application integrations. Lower precedence number wins on conflicts among tiers 1–4; `04. Applications and Integrations.md` and `15. Templates.md` are peers at tier 4, and the `15` filename does not add a fifth tier or a new priority.
- Before adding, splitting, merging, or renaming a guideline, apply `01 Guideline/01. Folders and Placement.md` → `Guideline 유지 원칙 — MECE`; keep its responsibility map and live references consistent.
- Read `01 Guideline/05. Writing Style.md` before editing authored prose. Keep source quotations, interpretation, and the author's own speech distinct; the detailed style rules live only in that document.
- Before changing MOC relationships or membership, read `01 Guideline/16. MOC.md`. Folders owns physical placement; Properties owns metadata serialization including tags. The `16` filename is not a precedence tier.
- Every existing user-authored file requires exact-path or deterministic-manifest authorization. Preserve YAML provenance; an authorized edit keeps `created_by: user` and sets `authorship: mixed`.
- Guidelines use imperative style and record enforcement gaps. Templates preserve their current engine syntax; Bases remain `.base` files. Do not duplicate mutable metadata enums or add a competing provenance schema.
- Treat any `## Thinking` section as user-only. Excalidraw drawings and plugin assets live in `07 Excalidraw/`; do not hand-edit raw `.excalidraw.md` content.

## Important Files
- `01 Guideline/00. Guideline Authoring.md` — guide and AGENTS authoring.
- `01 Guideline/01. Folders and Placement.md` — physical placement.
- `01 Guideline/02. Properties.md` — frontmatter, types, and authorship SSOT.
- `01 Guideline/03. Agent Permissions and Workflows.md` — zones, authorization, and provenance.
- `01 Guideline/04. Applications and Integrations.md` — application roles, interfaces, and integration policy.
- `01 Guideline/05. Writing Style.md` — the user's note-writing and Markdown presentation preferences, subordinate to policy and template contracts.
- `01 Guideline/06. Knowledge Compile Guideline.md` — knowledge compile.
- `01 Guideline/12. DEVONthink Guideline.md` — DEVONthink.
- `01 Guideline/15. Templates.md` — template categories, routes, and engine.
- `01 Guideline/16. MOC.md` — note-relationship policy, independent of folder placement.
- `01 Guideline/17. Research Evidence.md` — research evidence.
- `02 Templates/AGENTS.md` — template-root contract.
- `../.oms/taxonomy.json` — machine-readable routing intent.
- `../.obsidian/plugins/` — live plugin configuration; inspect path references before taxonomy changes. `community-plugins.json` is configured IDs, not install proof.

## Applications and Runtime References
Application roles, interfaces, and integration policy for Templater, ZotLit, Linter, Dataview, and other plugins follow `01 Guideline/04. Applications and Integrations.md`. OMS reuses the Obsidian template routes in `01 Guideline/15. Templates.md`; there is no separate OMS template folder. Periodic Notes is not installed; leftover core Daily Notes config and `periodic-notes:*` hotkeys are not install evidence. Plugin-managed properties and `.obsidian` settings are not hand-edited through this guide; template categories, routes, and engine syntax follow `01 Guideline/15. Templates.md`.

## Testing & QA
Check policy precedence, exact authorization, frontmatter/provenance preservation, template syntax, `.base` validity, and path references in plugin settings. Confirm extra template directories were documented rather than promoted into new Templater routes, no credentials were copied, and only the assigned guide changed. Parent-level verification covers link/index checks and the final changed-path allowlist.

<!-- MANUAL: -->
