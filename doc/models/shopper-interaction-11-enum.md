
# Shopper Interaction 11 Enum

The sales channel condition that defines whether the split logic applies.

Possible values:

* **Ecommerce**: Online transactions where the cardholder is present.
* **ContAuth**: Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer).
* **Moto**: Mail-order and telephone-order transactions where the customer is in contact with the merchant via email or telephone.
* **POS**: Point-of-sale transactions where the customer is physically present to make a payment using a secure payment terminal.
* **ANY**: All sales channels.

## Enumeration

`ShopperInteraction11Enum`

## Fields

| Name |
|  --- |
| `ECOMMERCE` |
| `CONTAUTH` |
| `MOTO` |
| `POS` |
| `ANY` |

## Example

```python
from adyen.models.shopper_interaction_11_enum import ShopperInteraction11Enum

shopper_interaction_11 = ShopperInteraction11Enum.CONTAUTH
```

