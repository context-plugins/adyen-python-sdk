
# Payment Instrument Reveal Info

## Structure

`PaymentInstrumentRevealInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cvc` | `str` | Required | The CVC2 value of the card. |
| `expiration` | [`Expiry2`](../../doc/models/expiry-2.md) | Required | The expiration date of the card. |
| `pan` | `str` | Required | The primary account number (PAN) of the card. |

## Example

```python
from adyen.models.expiry_2 import Expiry2
from adyen.models.payment_instrument_reveal_info import PaymentInstrumentRevealInfo

payment_instrument_reveal_info = PaymentInstrumentRevealInfo(
    cvc='cvc2',
    expiration=Expiry2(
        month='month6',
        year='year8'
    ),
    pan='pan0'
)
```

