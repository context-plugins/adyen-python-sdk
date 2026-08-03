
# Permit Result

*This model accepts additional fields of type Any.*

## Structure

`PermitResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `result_key` | `str` | Optional | The key to link permit requests to permit results. |
| `token` | `str` | Optional | The permit token which is used to make payments by the partner company. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.permit_result import PermitResult

permit_result = PermitResult(
    result_key='resultKey8',
    token='token8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

