
# Store Payment Method Mode Enum

Indicates if the details of the payment method will be stored for the shopper. Possible values:

* **disabled** – No details will be stored (default).
* **askForConsent** – If the `shopperReference` is provided, the Drop-in/Component shows a checkbox where the shopper can select to store their payment details for card payments.
* **enabled** – If the `shopperReference` is provided, the details will be stored without asking the shopper for consent.

## Enumeration

`StorePaymentMethodModeEnum`

## Fields

| Name |
|  --- |
| `ASKFORCONSENT` |
| `DISABLED` |
| `ENABLED` |

## Example

```python
from adyen.models.store_payment_method_mode_enum import StorePaymentMethodModeEnum

store_payment_method_mode = StorePaymentMethodModeEnum.DISABLED
```

