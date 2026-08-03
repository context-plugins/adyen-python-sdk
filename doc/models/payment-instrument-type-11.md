
# Payment Instrument Type 11

Type of payment instrument.
Possible values:

* **Card**
* **Cash**
* **Check**
* **Mobile**
* **StoredValue**

## Enumeration

`PaymentInstrumentType11`

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
from adyen.models.payment_instrument_type_11 import PaymentInstrumentType11

payment_instrument_type_11 = PaymentInstrumentType11.CASH
```

