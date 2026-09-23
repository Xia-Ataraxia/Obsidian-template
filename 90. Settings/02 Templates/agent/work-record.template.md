---
type: idea
created_by: agent
authorship: agent
tags:
  - agent-session
date_created: {{date_created}}
date_modified: {{date_modified}}
---

# {{title}}

<!-- Optional identity keys are deliberately absent from baseline frontmatter. Add session_id as a quoted string only after verifying the parent runtime's ID. Add hermes_profile as a quoted string only for a verified active Hermes profile, following 02. Properties. Never add empty identity fields. Keep only the latest verified work-commit URL in Commit Evidence; replace rather than append older links or SHA lists. -->

<!-- Follow Agent Work Records in 90. Settings/01 Guideline/03. Agent Permissions and Workflows.md. This is one report per parent session, not one note per task. Update the existing session report as requests accumulate. Keep its initial filename stable. Fill session_id only from a verified parent runtime session identifier; omit that property when unavailable, following 02. Properties. Use English headings and the user's requested body language. Keep required ## sections; freely choose paragraphs, nested lists, and topic-specific ### or deeper headings within them. Follow 05. Writing Style for semantic grouping rather than forcing a single format. Sources are substantive evidence used to answer the user's questions or support results, not a list of instructions loaded. Include a guideline only when its content is itself evidence for the user's question. Repeat source bullets as needed and put the usage reason beneath each link. State accurately when no substantive sources were used; describe actual access limitations separately and omit them when none apply. Record only actual checks. Follow Git and GitHub in 04. Applications and Integrations for commit evidence; omit the Commit Evidence block for a session with no file changes, and never invent a commit or publication link. Resolve placeholders and remove these instructions before saving. -->

## Requests

{{requests_and_context}}

## Work Performed

{{work_performed}}

## Results

{{answers_deliverables_and_rationale}}

## Sources

- {{source_link}}
	- {{contribution_to_answer}}

{{source_limitations}}

## Verification

{{checks_outcomes_and_limits}}

### Commit Evidence

- Work commit
	- {{verified_work_commit_reference}}
- Origin
	- Machine
		- {{source_machine}}
	- Vault
		- {{source_vault}}
	- Worktree
		- {{source_worktree_path}}
	- Repository
		- {{source_repository}}
	- Branch
		- {{source_branch}}
- Publication
	- {{commit_and_publication_status}}

## Open Items

{{open_items}}
