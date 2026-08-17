
# Permit Result

## Structure

`PermitResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `result_key` | `str` | Optional | The key to link permit requests to permit results. |
| `token` | `str` | Optional | The permit token which is used to make payments by the partner company. |

## Example

```python
from adyen.models.permit_result import PermitResult

permit_result = PermitResult(
    result_key='resultKey8',
    token='token8'
)
```

