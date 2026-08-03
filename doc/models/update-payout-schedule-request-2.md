
# Update Payout Schedule Request 2

The details of the payout schedule to which the account must be updated.

*This model accepts additional fields of type Any.*

## Structure

`UpdatePayoutScheduleRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`Action`](../../doc/models/action.md) | Optional | - |
| `reason` | `str` | Optional | The reason for the payout schedule update.<br><br>> This field is required when the `schedule` parameter is set to `HOLD`. |
| `schedule` | [`Schedule1`](../../doc/models/schedule-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.action import Action
from adyen.models.schedule_1 import Schedule1
from adyen.models.update_payout_schedule_request_2 import UpdatePayoutScheduleRequest2

update_payout_schedule_request_2 = UpdatePayoutScheduleRequest2(
    schedule=Schedule1.WEEKLY_MON_TO_FRI_US,
    action=Action.UPDATE,
    reason='reason8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

