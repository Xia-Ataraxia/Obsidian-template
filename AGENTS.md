---
type: note
created_by: agent
authorship: agent
---
# Repository Guidelines

## Purpose

- This repository is a portable Obsidian vault template.
	- It ships the twelve-root system, nested `AGENTS.md` contracts, and operational guidelines.
	- Adopters run the same system in their own vault.
- This file is the routing entry point for vault work.
	- It names the required owner documents without copying their contracts.
- The twelve numbered roots ship as skeleton with a few public example notes.
- Guideline number `07` is intentionally absent because it is machine-specific.
- Guides other than the README pair, `08. Writing and AI`, and `09. Agent Skills` are single-language.
- `.oms/*.json` control files are produced by the OMS tool and are not shipped.
- Six community plugins ship pre-installed as binaries (`main.js`, `manifest.json`, `styles.css`) under `.obsidian/plugins/`: Templater, Homepage, Omnisearch, Excalidraw, Outliner, Linter.
- The vendored skill under `.agents/skills/obsidian/` is upstream content kept verbatim. Fix problems upstream and re-vendor, rather than editing the copy in place. The skill teaches generic Obsidian mechanics and never overrides this vault's own placement, writing, or permission guides.

## User Context

- Read @Me.md to understand who owns this vault.
- Root `Me.md` is a blank worksheet in this template.
	- Filled answers stay in the adopter's vault.
- Match the task to the routes below before loading guidelines.
	- Paths are lookup targets, not import directives.
	- Read only the matching owners and their required dependencies.
	- Reuse current context rather than rereading unchanged documents.
- Before editing, read the applicable nested `AGENTS.md` files along the target directory path.
- Human navigation: [[Me]], [[01. Folders and Placement]].

## Agent Identity

- Recognized agent names are configured by the adopter, for example Hermes profiles, GJC, Aside, Claude Code, Codex.
	- The shipped Inbox destinations exist for GJC, Aside, Claude Code, Codex, and web chat providers.
	- See `Agent Work Record Placement` in `90. Settings/01 Guideline/01. Folders and Placement.md`.
	- Use reliable runtime identity when selecting a name.
	- Do not use the underlying model as identity evidence.
	- Do not infer role specialization.
	- Recognition does not grant editing permissions.
- An unknown or uncertain identity asks the user for the agent name and record destination before creating a record.
	- A known identity with an unresolved destination asks the user before creating the record.
- Never auto-register an agent name or create a folder to resolve identity or placement.

## Task Routes

- When creating or editing an `AGENTS.md` contract, read `90. Settings/01 Guideline/00. Guideline Authoring.md`.
	- Follow its `AGENTS Authoring` section.
- When determining edit permissions or selecting a reusable workflow:
	- Read `90. Settings/01 Guideline/03. Agent Permissions and Workflows.md`.
	- Use `Routing Law` and `Zone Determination Table` for authorization.
	- Use `Skill Package` and `Workflow Selection` for craft-skills and the adopter's skill repositories.
	- Use `Context Discovery` for reference resolution and conditional reading.
- When changing structure, metadata, permissions, or application integrations:
	- Read the five policy owners in precedence order.
		- Tier 1: `90. Settings/01 Guideline/01. Folders and Placement.md`
		- Tier 2: `90. Settings/01 Guideline/02. Properties.md`
		- Tier 3: `90. Settings/01 Guideline/03. Agent Permissions and Workflows.md`
		- Tier 4: `90. Settings/01 Guideline/04. Applications and Integrations.md`
		- Tier 4 peer: `90. Settings/01 Guideline/15. Templates.md`
- When writing or editing note prose:
	- Read `90. Settings/01 Guideline/05. Writing Style.md`.
- When recording properties or dates:
	- Read `90. Settings/01 Guideline/02. Properties.md`.
- When editing note relationships or MOC membership:
	- Read `90. Settings/01 Guideline/16. MOC.md`.
- When writing or editing `AGENTS.md`:
	- Read `90. Settings/01 Guideline/00. Guideline Authoring.md`.
		- Follow `AGENTS Authoring` for independent investigation, synthesis, and review.
	- Read `90. Settings/02 Templates/agent/root-agents.template.md` for the root file.
	- Read `90. Settings/02 Templates/agent/nested-agents.template.md` for nested files.
- When writing or editing guidelines:
	- Read `90. Settings/01 Guideline/00. Guideline Authoring.md`.
	- Read `90. Settings/02 Templates/manual/guideline.template.md`.
- When choosing application interfaces or changing integrations:
	- Read `90. Settings/01 Guideline/04. Applications and Integrations.md`.
- When editing or running templates:
	- Read `90. Settings/01 Guideline/15. Templates.md`.
- When compiling knowledge from sources:
	- Read `90. Settings/01 Guideline/06. Knowledge Compile Guideline.md`.
- When working with DEVONthink:
	- Read `90. Settings/01 Guideline/12. DEVONthink Guideline.md`.
- When recording or grading research evidence:
	- Read `90. Settings/01 Guideline/17. Research Evidence.md`.
- When completing file changes or performing Git operations:
	- Read `Git and GitHub` in `90. Settings/01 Guideline/04. Applications and Integrations.md`.
- When onboarding or teaching the basics: read `90. Settings/01 Guideline/08. Writing and AI.md` (bilingual) and `09. Agent Skills.md` (bilingual).

## Work Records

- Before completing a substantive task, read `90. Settings/01 Guideline/03. Agent Permissions and Workflows.md`.
	- Follow `Agent Work Records` for the session-report obligation and content contract.
	- Read `Agent Work Record Placement` in `90. Settings/01 Guideline/01. Folders and Placement.md` for the destination.
	- Use the exact template `90. Settings/02 Templates/agent/work-record.template.md`.
