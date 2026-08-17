
# Register SCA Final Response

## Structure

`RegisterSCAFinalResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `bool` | Optional | Specifies if the registration was initiated successfully. |

## Example

```python
from adyen.models.register_sca_final_response import RegisterSCAFinalResponse

register_sca_final_response = RegisterSCAFinalResponse(
    success=False
)
```

