
# Update Payout Schedule Request

## Structure

`UpdatePayoutScheduleRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`ActionEnum`](../../doc/models/action-enum.md) | Optional | Direction on how to handle any payouts that have already been scheduled.<br><br>Possible values:<br><br>* `CLOSE`: close the existing batch of payouts.<br>* `UPDATE`: reschedule the existing batch to the new schedule.<br>* `NOTHING` (**default**): allow the payout to proceed. |
| `reason` | `str` | Optional | The reason for the payout schedule update.<br><br>> This field is required when the `schedule` parameter is set to `HOLD`. |
| `schedule` | [`Schedule1Enum`](../../doc/models/schedule-1-enum.md) | Required | The new payout schedule for the account.<br><br>Possible values: `DEFAULT`, `DAILY`, `DAILY_US`, `DAILY_EU`, `DAILY_AU`, `DAILY_SG`, `WEEKLY`, `WEEKLY_ON_TUE_FRI_MIDNIGHT`, `BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT`, `MONTHLY`, `HOLD`.<br><br>> `HOLD` prevents scheduled payouts, but you can still initiate payouts manually. |

## Example

```python
from adyen.models.action_enum import ActionEnum
from adyen.models.schedule_1_enum import Schedule1Enum
from adyen.models.update_payout_schedule_request import UpdatePayoutScheduleRequest

update_payout_schedule_request = UpdatePayoutScheduleRequest(
    schedule=Schedule1Enum.DAILY,
    action=ActionEnum.CLOSE,
    reason='reason8'
)
```

