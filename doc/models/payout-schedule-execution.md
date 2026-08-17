
# Payout Schedule Execution

## Structure

`PayoutScheduleExecution`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the payout execution. |
| `result` | [`ExecutionResult1Enum`](../../doc/models/execution-result-1-enum.md) | Optional | The status of the payout execution.<br><br>Possible values:<br><br>- **succeeded**: The payout was sent successfully.<br>- **failed**: The payout could not be sent because an error occurred.<br>- **skipped**: The payout was not triggered as expected. |
| `result_details` | [`PayoutScheduleExecutionDetails2`](../../doc/models/payout-schedule-execution-details-2.md) | Optional | Contains information about the result of the payout execution. |
| `triggered_at` | `datetime` | Optional | The date and time when the payout execution was initiated. |

## Example

```python
import dateutil.parser

from adyen.models.execution_result_1_enum import ExecutionResult1Enum
from adyen.models.payout_schedule_execution import PayoutScheduleExecution
from adyen.models.payout_schedule_execution_details_2 import PayoutScheduleExecutionDetails2

payout_schedule_execution = PayoutScheduleExecution(
    id='id8',
    result=ExecutionResult1Enum.SKIPPED,
    result_details=PayoutScheduleExecutionDetails2(
        reason='reason8',
        reason_code='reasonCode0',
        transfer_id='transferId4'
    ),
    triggered_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

