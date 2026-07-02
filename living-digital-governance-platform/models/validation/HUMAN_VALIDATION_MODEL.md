# Human Validation Model

Human validation is mandatory when an output can influence operational, legal, institutional, ethical, or sensitive decisions.

```mermaid
flowchart TD
    A[AI Output or Critical Object] --> B{Sensitive or High Impact?}
    B -- Yes --> C[Human Validation Required]
    B -- No --> D[Standard Review]
    C --> E{Approved?}
    E -- Yes --> F[Controlled Use]
    E -- No --> G[Rejected or Revised]
    D --> H[Registered Use]
    F --> I[Traceability Log]
    G --> I
    H --> I
```

## Minimum Validation Evidence

- validated object
- validator
- validation date
- validation decision
- validation scope
- reason for rejection if rejected
- Traceability Log
