
# Dispute Status 1 Enum

The current status of the dispute.

When you create a dispute, you can only set the `status` to **draft**. When you update a dispute, you can set the `status` to **submitted** or **closed**.

Possible values: **draft**, **submitted**, **closed**, **won**, **chargeback**, **secondPresentment**.

## Enumeration

`DisputeStatus1Enum`

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
from adyen.models.dispute_status_1_enum import DisputeStatus1Enum

dispute_status_1 = DisputeStatus1Enum.CHARGEBACK
```

