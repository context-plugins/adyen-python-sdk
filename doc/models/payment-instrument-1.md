
# Payment Instrument 1

Sets the allowed payment instrument for Pay at table transactions.  Can be: **cash** or **card**. If not set, the terminal presents both options.

## Enumeration

`PaymentInstrument1`

## Fields

| Name |
|  --- |
| `CASH` |
| `CARD` |

## Example

```python
from adyen.models.payment_instrument_1 import PaymentInstrument1

payment_instrument_1 = PaymentInstrument1.CASH
```

