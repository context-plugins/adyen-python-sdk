
# Sodexo Info 2

Details to provide if `type` is **sodexo**.

*This model accepts additional fields of type Any.*

## Structure

`SodexoInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_contact_phone` | `str` | Required | Sodexo merchantContactPhone |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sodexo_info_2 import SodexoInfo2

sodexo_info_2 = SodexoInfo2(
    merchant_contact_phone='merchantContactPhone6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

