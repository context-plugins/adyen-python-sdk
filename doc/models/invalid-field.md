
# Invalid Field

## Structure

`InvalidField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The field that has an invalid value. |
| `value` | `str` | Required | The invalid value. |
| `message` | `str` | Required | Description of the validation error. |

## Example

```python
from adyen.models.invalid_field import InvalidField

invalid_field = InvalidField(
    name='name4',
    value='value6',
    message='message4'
)
```

