
# Shopper Name 1

The shopper's full name. This object is required for some payment methods such as AfterPay, Klarna, or if you're enrolled in the PayPal Seller Protection program.

## Structure

`ShopperName1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `last_name` | `str` | Required | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.shopper_name_1 import ShopperName1

shopper_name_1 = ShopperName1(
    first_name='firstName8',
    last_name='lastName0'
)
```

