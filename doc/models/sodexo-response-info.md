
# Sodexo Response Info

*This model accepts additional fields of type Any.*

## Structure

`SodexoResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_contact_phone` | `str` | Optional | Sodexo merchantContactPhone |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sodexo_response_info import SodexoResponseInfo

sodexo_response_info = SodexoResponseInfo(
    merchant_contact_phone='merchantContactPhone0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

