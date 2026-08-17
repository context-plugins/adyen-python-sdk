
# Dispute Service Result 1

The result of the dispute service.

## Structure

`DisputeServiceResult1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `str` | Optional | The general error message. |
| `success` | `bool` | Required | Indicates whether the request succeeded. |

## Example

```python
from adyen.models.dispute_service_result_1 import DisputeServiceResult1

dispute_service_result_1 = DisputeServiceResult1(
    success=False,
    error_message='errorMessage2'
)
```

