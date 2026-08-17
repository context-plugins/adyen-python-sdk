
# Shopper Name

## Structure

`ShopperName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `last_name` | `str` | Required | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.shopper_name import ShopperName

shopper_name = ShopperName(
    first_name='firstName6',
    last_name='lastName2'
)
```

