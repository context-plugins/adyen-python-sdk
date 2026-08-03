
# Payout Schedule

The payout schedule for the account.

Possible values: `DEFAULT`, `DAILY`, `DAILY_US`, `DAILY_EU`, `DAILY_AU`, `DAILY_SG`, `WEEKLY`, `WEEKLY_ON_TUE_FRI_MIDNIGHT`, `BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT`, `MONTHLY`, `HOLD`.

> `HOLD` prevents scheduled payouts, but you can still initiate payouts manually.

## Enumeration

`PayoutSchedule`

## Fields

| Name |
|  --- |
| `BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT` |
| `DAILY` |
| `DAILY_AU` |
| `DAILY_EU` |
| `DAILY_SG` |
| `DAILY_US` |
| `HOLD` |
| `MONTHLY` |
| `WEEKLY` |
| `WEEKLY_MON_TO_FRI_AU` |
| `WEEKLY_MON_TO_FRI_EU` |
| `WEEKLY_MON_TO_FRI_US` |
| `WEEKLY_ON_TUE_FRI_MIDNIGHT` |
| `WEEKLY_SUN_TO_THU_AU` |
| `WEEKLY_SUN_TO_THU_US` |

## Example

```python
from adyen.models.payout_schedule import PayoutSchedule

payout_schedule = PayoutSchedule.WEEKLY_SUN_TO_THU_US
```

