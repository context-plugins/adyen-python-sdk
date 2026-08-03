
# Sodexo Response Info 2

**sodexo** details

*This model accepts additional fields of type Any.*

## Structure

`SodexoResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_contact_phone` | `str` | Optional | Sodexo merchantContactPhone |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sodexo_response_info_2 import SodexoResponseInfo2

sodexo_response_info_2 = SodexoResponseInfo2(
    merchant_contact_phone='merchantContactPhone0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

