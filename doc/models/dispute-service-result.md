
# Dispute Service Result

## Structure

`DisputeServiceResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_message` | `str` | Optional | The general error message. |
| `success` | `bool` | Required | Indicates whether the request succeeded. |

## Example

```python
from adyen.models.dispute_service_result import DisputeServiceResult

dispute_service_result = DisputeServiceResult(
    success=False,
    error_message='errorMessage2'
)
```

