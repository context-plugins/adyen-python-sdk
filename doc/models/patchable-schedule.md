
# Patchable Schedule

## Structure

`PatchableSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`ScheduleType1Enum`](../../doc/models/schedule-type-1-enum.md) | Optional | The type of schedule at which the top up is executed.<br><br>* **weekdays**: pull in funds Monday-Friday at 07:00 AM in the local timezone of the balance account.<br><br>* **weekly**: pull in funds every Monday at 07:00 AM in the local timezone of the balance account.<br><br>* **monthly**: pull in funds every first of the month at 07:00 AM in the local timezone of the balance account.<br><br>* **null** (default): continuous monitoring. |

## Example

```python
from adyen.models.patchable_schedule import PatchableSchedule
from adyen.models.schedule_type_1_enum import ScheduleType1Enum

patchable_schedule = PatchableSchedule(
    mtype=ScheduleType1Enum.MONTHLY
)
```

