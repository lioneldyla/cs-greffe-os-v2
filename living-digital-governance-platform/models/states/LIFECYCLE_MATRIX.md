# Lifecycle Matrix — LDGP

This matrix maps each governed object type to its applicable lifecycle states.

## Objects and Lifecycle States

| Object | Draft | Registered | Reviewed | Approved | Active | Deprecated | Archived |
|---|---|---|---|---|---|---|---|
| Dataset | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Document | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| AI Use Case | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| KPI | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Risk | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Decision | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Action | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Key Rules per Object

- **Dataset**: Requires owner at Registered. Human validation before Active.
- **Document**: Requires reviewer at Reviewed. Traceability Required.
- **AI Use Case**: Requires human validation before Active. AI outputs must be reviewed.
- **KPI**: Requires Accountable Authority approval.
- **Risk**: Must be reviewed before Approved.
- **Decision**: Requires human validation. Traceability Required.
- **Action**: Requires owner. Must be linked to a Decision or KPI.
