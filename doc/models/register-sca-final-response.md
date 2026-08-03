
# Register Sca Final Response

*This model accepts additional fields of type Any.*

## Structure

`RegisterScaFinalResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `bool` | Optional | Specifies if the registration was initiated successfully. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.register_sca_final_response import RegisterScaFinalResponse

register_sca_final_response = RegisterScaFinalResponse(
    success=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

