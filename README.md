# hermes-context-persistence

Hermes Agent plugin that re-injects AGENTS.md context before each LLM call
using the `pre_llm_call` hook.

## Problem

Hermes already loads `AGENTS.md` as a context file into the system prompt,
which compaction does not summarise away. However, in very long sessions the
compacted context can still lose fidelity on project-specific mandates. This
plugin ensures `AGENTS.md` is re-injected before each LLM call so the rules
remain visible even after compaction.

## Solution

This plugin uses the `post_compaction` hook to re-inject `AGENTS.md` and
relevant memory after compaction.

## Installation

```bash
hermes plugins install alfonsodg/hermes-context-persistence
hermes plugins enable hermes-context-persistence
```

## Author

Alfonso de la Guarda Reyes <alfonsodg@gmail.com>

## License

MIT
