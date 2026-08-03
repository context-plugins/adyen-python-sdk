
# Sodexo Info

*This model accepts additional fields of type Any.*

## Structure

`SodexoInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_contact_phone` | `str` | Required | Sodexo merchantContactPhone |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sodexo_info import SodexoInfo

sodexo_info = SodexoInfo(
    merchant_contact_phone='merchantContactPhone0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

