
# Common Field 2

Merchant developed software, such as cashier application, used to interact with the Adyen API.

*This model accepts additional fields of type Any.*

## Structure

`CommonField2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the field. For example, Name of External Platform. |
| `version` | `str` | Optional | Version of the field. For example, Version of External Platform. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.common_field_2 import CommonField2

common_field_2 = CommonField2(
    name='name6',
    version='version2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

