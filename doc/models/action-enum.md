
# Action Enum

Direction on how to handle any payouts that have already been scheduled.

Possible values:

* `CLOSE`: close the existing batch of payouts.
* `UPDATE`: reschedule the existing batch to the new schedule.
* `NOTHING` (**default**): allow the payout to proceed.

## Enumeration

`ActionEnum`

## Fields

| Name |
|  --- |
| `CLOSE` |
| `NOTHING` |
| `UPDATE` |

## Example

```python
from adyen.models.action_enum import ActionEnum

action = ActionEnum.CLOSE
```

