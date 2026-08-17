
# Name 23

The individual's name.

## Structure

`Name23`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The individual's first name. Must not be blank. |
| `infix` | `str` | Optional | The infix in the individual's name, if any. |
| `last_name` | `str` | Required | The individual's last name. Must not be blank. |

## Example

```python
from adyen.models.name_23 import Name23

name_23 = Name23(
    first_name='firstName8',
    last_name='lastName0',
    infix='infix0'
)
```

