
# Dispute Status

## Enumeration

`DisputeStatus`

## Fields

| Name |
|  --- |
| `DRAFT` |
| `SUBMITTED` |
| `CHARGEBACK` |
| `SECONDPRESENTMENT` |
| `WON` |
| `CLOSED` |

## Example

```python
from adyen.models.dispute_status import DisputeStatus

dispute_status = DisputeStatus.DRAFT
```

