
# Name 21

The individual's name.

*This model accepts additional fields of type Any.*

## Structure

`Name21`

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

from adyen.models.name_21 import Name21

name_21 = Name21(
    first_name='firstName8',
    last_name='lastName0',
    infix='infix0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

