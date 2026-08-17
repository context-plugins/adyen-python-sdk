
# Event Enum

The event.

> Permitted values: `InactivateAccount`, `RefundNotPaidOutTransfers`.
> For more information, refer to [Verification checks](https://docs.adyen.com/classic-platforms/verification-process).

## Enumeration

`EventEnum`

## Fields

| Name |
|  --- |
| `INACTIVATEACCOUNT` |
| `REFUNDNOTPAIDOUTTRANSFERS` |

## Example

```python
from adyen.models.event_enum import EventEnum

event = EventEnum.INACTIVATEACCOUNT
```

