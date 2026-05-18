# Compress Architecture Examples

## Invocation

```txt
/compress-architecture
This codebase feels too complex. Audit the API layer first.
```

## Expected Behavior

The skill should inspect the requested scope, produce a ranked compression report, and wait for confirmation before editing files.

## Example Output Shape

```txt
### src/api/user-service.ts
Label: delegating
Proposed action: collapse
Complexity delta: Medium
Reasoning: The module mostly forwards calls to the repository without adding policy, validation, or error handling. Collapsing it into the caller would reduce one layer without weakening a domain boundary.

Summary: 3 load-bearing, 2 candidates for compression (0 High / 1 Medium / 1 Low impact).
```
