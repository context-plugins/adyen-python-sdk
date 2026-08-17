
# Payment Instrument Enum

Sets the allowed payment instrument for Pay at table transactions.  Can be: **cash** or **card**. If not set, the terminal presents both options.

## Enumeration

`PaymentInstrumentEnum`

## Fields

| Name |
|  --- |
| `CASH` |
| `CARD` |

## Example

```python
from adyen.models.payment_instrument_enum import PaymentInstrumentEnum

payment_instrument = PaymentInstrumentEnum.CASH
```

