
# Name 1

*This model accepts additional fields of type Any.*

## Structure

`Name1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The individual's first name. Must not be blank. |
| `infix` | `str` | Optional | The infix in the individual's name, if any. |
| `last_name` | `str` | Required | The individual's last name. Must not be blank. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.name_1 import Name1

name_1 = Name1(
    first_name='firstName2',
    last_name='lastName6',
    infix='infix6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

