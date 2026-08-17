
# Name 7

The shopper's full name.

## Structure

`Name7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `last_name` | `str` | Required | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.name_7 import Name7

name_7 = Name7(
    first_name='firstName4',
    last_name='lastName2'
)
```

