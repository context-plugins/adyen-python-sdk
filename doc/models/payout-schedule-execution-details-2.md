
# Payout Schedule Execution Details 2

Contains information about the result of the payout execution.

## Structure

`PayoutScheduleExecutionDetails2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Optional | Human readable reason for why execution was not successful if applicable. |
| `reason_code` | `str` | Optional | Reason Code for why execution was not successful if applicable. |
| `transfer_id` | `str` | Optional | The id of the transfer from executing the payout. |

## Example

```python
from adyen.models.payout_schedule_execution_details_2 import PayoutScheduleExecutionDetails2

payout_schedule_execution_details_2 = PayoutScheduleExecutionDetails2(
    reason='reason8',
    reason_code='reasonCode6',
    transfer_id='transferId0'
)
```

