
# Patchable Trigger 2

The condition that triggers the top-up. This can be a recurring schedule or a minimum balance threshold.

## Structure

`PatchableTrigger2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schedule` | [PatchableSchedule](../../doc/models/patchable-schedule.md) \| None | Optional | This is a container for one-of cases. |
| `threshold` | [`PatchableAmountDTO1`](../../doc/models/patchable-amount-dto-1.md) | Optional | The balance threshold that triggers the top-up. If the balance falls below this amount, a top-up is initiated. |

## Example

```python
from adyen.models.patchable_amount_dto_1 import PatchableAmountDTO1
from adyen.models.patchable_schedule import PatchableSchedule
from adyen.models.patchable_trigger_2 import PatchableTrigger2
from adyen.models.schedule_type_1_enum import ScheduleType1Enum

patchable_trigger_2 = PatchableTrigger2(
    schedule=PatchableSchedule(
        mtype=ScheduleType1Enum.MONTHLY
    ),
    threshold=PatchableAmountDTO1(
        currency='currency8',
        value=32
    )
)
```

