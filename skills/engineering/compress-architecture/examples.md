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
Expected simplification: Medium
Risk: Low
Confidence: Medium
Evidence:
- src/api/user-service.ts: forwards calls to the repository without policy, validation, translation, or error handling.
- src/api/users/create-user.ts: already owns request validation before calling the service.
Reasoning: The module mostly forwards calls to the repository without adding policy, validation, or error handling. Collapsing it into the caller would reduce one layer without weakening a domain boundary.

Summary: 3 load-bearing, 2 candidates for compression (0 High / 1 Medium / 1 Low expected simplification).
```

## No Findings Output

```txt
No compression recommended in this scope.
Reasoning: The small adapters in this package isolate third-party APIs and keep tests independent of network behavior. The current boundaries appear load-bearing.
Summary: 5 load-bearing, 0 candidates for compression.
```
