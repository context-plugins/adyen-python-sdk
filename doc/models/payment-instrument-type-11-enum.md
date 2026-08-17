
# Payment Instrument Type 11 Enum

Type of payment instrument.
Possible values:

* **Card**
* **Cash**
* **Check**
* **Mobile**
* **StoredValue**

## Enumeration

`PaymentInstrumentType11Enum`

## Fields

| Name |
|  --- |
| `CARD` |
| `CHECK` |
| `MOBILE` |
| `STOREDVALUE` |
| `CASH` |

## Example

```python
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum

payment_instrument_type_11 = PaymentInstrumentType11Enum.CASH
```

