
# Common Field

Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc.

*This model accepts additional fields of type Any.*

## Structure

`CommonField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the field. For example, Name of External Platform. |
| `version` | `str` | Optional | Version of the field. For example, Version of External Platform. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.common_field import CommonField

common_field = CommonField(
    name='name4',
    version='version0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

