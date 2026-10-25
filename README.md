# hermes-context-persistence

Hermes Agent plugin that re-injects context after compaction using the
`post_compaction` hook.

## Problem

Long Hermes sessions compact older conversation into a summary. Project
rules and memory can be dropped, causing the agent to forget mandates.

## Solution

This plugin uses the `post_compaction` hook to re-inject `AGENTS.md` and
relevant memory after compaction.

## Installation

```bash
hermes plugins install alfonsodg/hermes-context-persistence
hermes plugins enable hermes-context-persistence
```

## License

MIT
