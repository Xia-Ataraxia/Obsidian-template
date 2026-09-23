---
type: note
created_by: agent
authorship: agent
---
<!-- Parent: ../AGENTS.md -->

# Repository Guidelines

## Project Overview

`01 Project/` contains finite active outcomes. Each project owns a semantic-name folder and a same-name hub; project-local notes keep the product or delivery context together.

## Architecture & Data Flow

The project folder is the active boundary. A hub is `<project>/<project>.md`; dated logs stay at `<project>/YYYY-MM-DD <project>.md`. Meetings use `type: meeting`; other activity uses `type: log`. Supporting specifications, research, credentials, and nested contracts remain with their owner.

Project completion follows the governed archive workflow. A Task is completed by its fields in place and never moved to `03 Archive/`. External originals stay in `../../85. Raw/` regardless of collector; summarize or link them rather than creating a second source copy.

## Key Directories

| Relative path | Contract |
|---|---|
| `<project>/<project>.md` | Hub and navigation entry for one active project. |
| `<project>/YYYY-MM-DD <project>.md` | Dated project log; meetings use `type: meeting`, other activity uses `type: log`. |
| `<project>/` supporting notes | Specifications, research, credentials, and project evidence stay with their owner. |
| Nested `AGENTS.md` | Project-specific architecture, directory, sensitivity, and QA rules. |

## Commands

- Search the vault with `qmd`; use `obsidian` CLI to verify wikilinks and properties when a change depends on them.
- Read the nearest nested guide before touching a project with one.
- Use the project’s source-repository README or local build guide for executable commands; this vault folder is not a code checkout.
- End every file-changing task in a project folder with a commit and a push, staging only the paths you touched (`git add -- "<path>"`). Never stage the whole tree. See [[04. Applications and Integrations#Git and GitHub]] for the full contract.

## Code Conventions & Common Patterns

- A hub uses `type: project` and omits `status`; placement in `01 Project/` denotes active state.
- Dated logs use `YYYY-MM-DD <project>.md` and remain immutable evidence. Create a new log instead of rewriting a dated record to reflect later understanding.
- Existing user-authored hubs and support notes require exact-path or deterministic-manifest authorization. Preserve their YAML provenance and protected `## Thinking` sections.
- Follow the authoritative metadata/agent policy and current session instructions for new-note provenance. This shared guide does not introduce another `created_by`, `authorship`, or agent-identity schema.

## Important Files

- `../AGENTS.md` — Work-level project/area/task routing and task-state rules.
- `../../AGENTS.md` — vault taxonomy, metadata, writable zones, and protected-note rules.
- `../../90. Settings/01 Guideline/01. Folders and Placement.md`, `02. Properties.md`, and `03. Agent Permissions and Workflows.md` — authoritative placement, provenance, and agent policy.

## Runtime/Tooling Preferences

Prefer `qmd` for retrieval and the `obsidian` CLI for authorized link or property checks. Do not launch Obsidian implicitly. Executable tooling belongs to each project's source repository or nested `_build/` guide rather than this shared Project root.

## Testing & QA

QA for this branch is path- and contract-oriented: confirm the project folder and hub, inspect note type and project relation, verify links with vault tooling, and keep dated evidence in place. Build, test, deployment, or credential checks are project-specific and must follow the nested guide and the source repository’s current instructions; do not infer commands from another project.
