
# Name 1

The name of the person funding the money.

## Structure

`Name1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `last_name` | `str` | Required | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.name_1 import Name1

name_1 = Name1(
    first_name='firstName2',
    last_name='lastName6'
)
```

