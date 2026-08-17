
# Name 21

## Structure

`Name21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `last_name` | `str` | Optional | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.name_21 import Name21

name_21 = Name21(
    first_name='firstName8',
    last_name='lastName0'
)
```

