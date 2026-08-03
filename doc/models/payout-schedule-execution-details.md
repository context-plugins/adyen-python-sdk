
# Payout Schedule Execution Details

*This model accepts additional fields of type Any.*

## Structure

`PayoutScheduleExecutionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Optional | Human readable reason for why execution was not successful if applicable. |
| `reason_code` | `str` | Optional | Reason Code for why execution was not successful if applicable. |
| `transfer_id` | `str` | Optional | The id of the transfer from executing the payout. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payout_schedule_execution_details import PayoutScheduleExecutionDetails

payout_schedule_execution_details = PayoutScheduleExecutionDetails(
    reason='reason2',
    reason_code='reasonCode4',
    transfer_id='transferId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

