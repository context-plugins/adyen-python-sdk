
# Shopper Name 2

The shopper's full name.

## Structure

`ShopperName2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `last_name` | `str` | Required | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.shopper_name_2 import ShopperName2

shopper_name_2 = ShopperName2(
    first_name='firstName2',
    last_name='lastName6'
)
```

