
# Shopper Interaction 1 Enum

The sales channel. Required if:

- The merchant account does not have a sales channel.
- `type` is **alipay**.

When you provide this field, it overrides the default sales channel set on the merchant account.

Possible values: **eCommerce**, **pos**, **contAuth**, and **moto**.

## Enumeration

`ShopperInteraction1Enum`

## Fields

| Name |
|  --- |
| `ECOMMERCE` |
| `POS` |
| `MOTO` |
| `CONTAUTH` |

## Example

```python
from adyen.models.shopper_interaction_1_enum import ShopperInteraction1Enum

shopper_interaction_1 = ShopperInteraction1Enum.ECOMMERCE
```

