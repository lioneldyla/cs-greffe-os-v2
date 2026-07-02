# State Transitions — LDGP

Generic LDGP lifecycle:

Draft → Registered → Reviewed → Approved → Active → Deprecated → Archived

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Registered
    Registered --> Reviewed
    Reviewed --> Approved
    Approved --> Active
    Active --> Deprecated
    Deprecated --> Archived
    Archived --> [*]
```

## Transition Rules

- Each transition requires documented validation.
- No object can skip the Approved state to become Active.
- Archived objects cannot be reactivated without a new Draft cycle.
