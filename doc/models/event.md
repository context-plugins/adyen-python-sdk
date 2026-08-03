
# Event

The event.

> Permitted values: `InactivateAccount`, `RefundNotPaidOutTransfers`.
> For more information, refer to [Verification checks](https://docs.adyen.com/classic-platforms/verification-process).

## Enumeration

`Event`

## Fields

| Name |
|  --- |
| `INACTIVATEACCOUNT` |
| `REFUNDNOTPAIDOUTTRANSFERS` |

## Example

```python
from adyen.models.event import Event

event = Event.INACTIVATEACCOUNT
```

