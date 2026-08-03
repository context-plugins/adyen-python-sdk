
# Payout Schedule Executions

*This model accepts additional fields of type Any.*

## Structure

`PayoutScheduleExecutions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payout_schedule_executions` | [`List[PayoutScheduleExecution]`](../../doc/models/payout-schedule-execution.md) | Required | Contains a list of executions of the payout schedule. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.execution_result_1 import ExecutionResult1
from adyen.models.payout_schedule_execution import PayoutScheduleExecution
from adyen.models.payout_schedule_execution_details import PayoutScheduleExecutionDetails
from adyen.models.payout_schedule_executions import PayoutScheduleExecutions

payout_schedule_executions = PayoutScheduleExecutions(
    payout_schedule_executions=[
        PayoutScheduleExecution(
            id='id2',
            result=ExecutionResult1.FAILED,
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

