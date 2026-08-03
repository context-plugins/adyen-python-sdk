
# Execution Result 1

The status of the payout execution.

Possible values:

- **succeeded**: The payout was sent successfully.
- **failed**: The payout could not be sent because an error occurred.
- **skipped**: The payout was not triggered as expected.

## Enumeration

`ExecutionResult1`

## Fields

| Name |
|  --- |
| `FAILED` |
| `SUCCEEDED` |
| `SKIPPED` |

## Example

```python
from adyen.models.execution_result_1 import ExecutionResult1

execution_result_1 = ExecutionResult1.SKIPPED
```

