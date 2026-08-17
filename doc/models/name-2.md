
# Name 2

The name of the shopper.

## Structure

`Name2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `last_name` | `str` | Required | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.name_2 import Name2

name_2 = Name2(
    first_name='firstName6',
    last_name='lastName2'
)
```

