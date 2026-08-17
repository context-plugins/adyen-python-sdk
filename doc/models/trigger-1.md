
# Trigger 1

The condition that triggers the top-up. This can be a recurring schedule or a minimum balance threshold.

## Structure

`Trigger1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schedule` | [`Schedule21`](../../doc/models/schedule-21.md) | Optional | Contains the details about the schedule that determines when the top up is executed. |
| `threshold` | [`Amount17`](../../doc/models/amount-17.md) | Required | The balance threshold that triggers the top-up. If the balance falls below this amount, a top-up is initiated. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.schedule_21 import Schedule21
from adyen.models.schedule_type_1_enum import ScheduleType1Enum
from adyen.models.trigger_1 import Trigger1

trigger_1 = Trigger1(
    threshold=Amount17(
        currency='currency8',
        value=32
    ),
    schedule=Schedule21(
        mtype=ScheduleType1Enum.WEEKDAYS
    )
)
```

