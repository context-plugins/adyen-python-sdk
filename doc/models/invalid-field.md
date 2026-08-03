
# Invalid Field

*This model accepts additional fields of type Any.*

## Structure

`InvalidField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Required | Description of the validation error. |
| `name` | `str` | Required | The field that has an invalid value. |
| `value` | `str` | Required | The invalid value. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.invalid_field import InvalidField

invalid_field = InvalidField(
    message='message4',
    name='name4',
    value='value6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

