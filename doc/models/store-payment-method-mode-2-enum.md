
# Store Payment Method Mode 2 Enum

Indicates if the details of the payment method will be stored for the shopper. Possible values:

* **disabled** – No details will be stored (default).
* **askForConsent** – If the `shopperReference` is provided, the Drop-in/Component shows a checkbox where the shopper can select to store their payment details for card payments.
* **enabled** – If the `shopperReference` is provided, the details will be stored without asking the shopper for consent.
  When set to **askForConsent** or **enabled**, you must also include the `recurringProcessingModel` parameter.

## Enumeration

`StorePaymentMethodMode2Enum`

## Fields

| Name |
|  --- |
| `ASKFORCONSENT` |
| `DISABLED` |
| `ENABLED` |

## Example

```python
from adyen.models.store_payment_method_mode_2_enum import StorePaymentMethodMode2Enum

store_payment_method_mode_2 = StorePaymentMethodMode2Enum.ASKFORCONSENT
```

