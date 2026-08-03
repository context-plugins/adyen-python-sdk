
# Payout Schedule Execution

*This model accepts additional fields of type Any.*

## Structure

`PayoutScheduleExecution`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the payout execution. |
| `result` | [`ExecutionResult1`](../../doc/models/execution-result-1.md) | Optional | - |
| `result_details` | [`PayoutScheduleExecutionDetails`](../../doc/models/payout-schedule-execution-details.md) | Optional | - |
| `triggered_at` | `datetime` | Optional | The date and time when the payout execution was initiated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.execution_result_1 import ExecutionResult1
from adyen.models.payout_schedule_execution import PayoutScheduleExecution
from adyen.models.payout_schedule_execution_details import PayoutScheduleExecutionDetails

payout_schedule_execution = PayoutScheduleExecution(
    id='id8',
    result=ExecutionResult1.SKIPPED,
    result_details=PayoutScheduleExecutionDetails(
        reason='reason8',
        reason_code='reasonCode0',
        transfer_id='transferId4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    triggered_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

