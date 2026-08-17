
# Payout Schedule Response 3

The details of the payout schedule to which the account is updated.

## Structure

`PayoutScheduleResponse3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next_scheduled_payout` | `datetime` | Optional | The date of the next scheduled payout. |
| `schedule` | [`ScheduleEnum`](../../doc/models/schedule-enum.md) | Optional | The payout schedule for the account.<br><br>Possible values: `DEFAULT`, `DAILY`, `DAILY_US`, `DAILY_EU`, `DAILY_AU`, `DAILY_SG`, `WEEKLY`, `WEEKLY_ON_TUE_FRI_MIDNIGHT`, `BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT`, `MONTHLY`, `HOLD`.<br><br>> `HOLD` prevents scheduled payouts, but you can still initiate payouts manually. |

## Example

```python
import dateutil.parser

from adyen.models.payout_schedule_response_3 import PayoutScheduleResponse3
from adyen.models.schedule_enum import ScheduleEnum

payout_schedule_response_3 = PayoutScheduleResponse3(
    next_scheduled_payout=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    schedule=ScheduleEnum.HOLD
)
```

