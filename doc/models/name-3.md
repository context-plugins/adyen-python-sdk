
# Name 3

## Structure

`Name3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The individual's first name. Must not be blank. |
| `infix` | `str` | Optional | The infix in the individual's name, if any. |
| `last_name` | `str` | Required | The individual's last name. Must not be blank. |

## Example

```python
from adyen.models.name_3 import Name3

name_3 = Name3(
    first_name='firstName0',
    last_name='lastName8',
    infix='infix8'
)
```

