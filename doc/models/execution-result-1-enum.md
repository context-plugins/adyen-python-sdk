
# Execution Result 1 Enum

The status of the payout execution.

Possible values:

- **succeeded**: The payout was sent successfully.
- **failed**: The payout could not be sent because an error occurred.
- **skipped**: The payout was not triggered as expected.

## Enumeration

`ExecutionResult1Enum`

## Fields

| Name |
|  --- |
| `FAILED` |
| `SUCCEEDED` |
| `SKIPPED` |

## Example

```python
from adyen.models.execution_result_1_enum import ExecutionResult1Enum

execution_result_1 = ExecutionResult1Enum.SKIPPED
```

