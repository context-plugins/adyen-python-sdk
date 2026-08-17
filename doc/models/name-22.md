
# Name 22

The user's full name.

## Structure

`Name22`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `last_name` | `str` | Optional | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.name_22 import Name22

name_22 = Name22(
    first_name='firstName8',
    last_name='lastName0'
)
```

