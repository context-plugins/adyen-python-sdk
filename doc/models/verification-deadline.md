
# Verification Deadline

## Structure

`VerificationDeadline`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`List[CapabilityEnum]`](../../doc/models/capability-enum.md) | Required, Read-only | The names of the capabilities to be disallowed. |
| `entity_ids` | `List[str]` | Optional, Read-only | The unique identifiers of the bank account(s) that the deadline applies to |
| `expires_at` | `datetime` | Required, Read-only | The date that verification is due by before capabilities are disallowed. |

## Example

```python
import dateutil.parser

from adyen.models.verification_deadline import VerificationDeadline

verification_deadline = VerificationDeadline(
    capabilities=[],
    expires_at=dateutil.parser.parse(None)
)
```

