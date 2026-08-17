
# Payout Schedule Execution Details

## Structure

`PayoutScheduleExecutionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Optional | Human readable reason for why execution was not successful if applicable. |
| `reason_code` | `str` | Optional | Reason Code for why execution was not successful if applicable. |
| `transfer_id` | `str` | Optional | The id of the transfer from executing the payout. |

## Example

```python
from adyen.models.payout_schedule_execution_details import PayoutScheduleExecutionDetails

payout_schedule_execution_details = PayoutScheduleExecutionDetails(
    reason='reason2',
    reason_code='reasonCode4',
    transfer_id='transferId0'
)
```

