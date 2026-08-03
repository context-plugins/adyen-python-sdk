
# Payout Schedule Response 3

The details of the payout schedule to which the account is updated.

*This model accepts additional fields of type Any.*

## Structure

`PayoutScheduleResponse3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next_scheduled_payout` | `datetime` | Optional | The date of the next scheduled payout. |
| `schedule` | [`PayoutSchedule`](../../doc/models/payout-schedule.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.payout_schedule import PayoutSchedule
from adyen.models.payout_schedule_response_3 import PayoutScheduleResponse3

payout_schedule_response_3 = PayoutScheduleResponse3(
    next_scheduled_payout=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    schedule=PayoutSchedule.HOLD,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

