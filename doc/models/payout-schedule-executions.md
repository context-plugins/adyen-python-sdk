
# Payout Schedule Executions

## Structure

`PayoutScheduleExecutions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payout_schedule_executions` | [`List[PayoutScheduleExecution]`](../../doc/models/payout-schedule-execution.md) | Required | Contains a list of executions of the payout schedule. |

## Example

```python
import dateutil.parser

from adyen.models.execution_result_1_enum import ExecutionResult1Enum
from adyen.models.payout_schedule_execution import PayoutScheduleExecution
from adyen.models.payout_schedule_execution_details_2 import PayoutScheduleExecutionDetails2
from adyen.models.payout_schedule_executions import PayoutScheduleExecutions

payout_schedule_executions = PayoutScheduleExecutions(
    payout_schedule_executions=[
        PayoutScheduleExecution(
            id='id2',
            result=ExecutionResult1Enum.FAILED,
            result_details=PayoutScheduleExecutionDetails2(
                reason='reason8',
                reason_code='reasonCode0',
                transfer_id='transferId4'
            ),
            triggered_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ]
)
```

