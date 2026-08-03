
# Payment Instrument Reveal Info

*This model accepts additional fields of type Any.*

## Structure

`PaymentInstrumentRevealInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cvc` | `str` | Required | The CVC2 value of the card. |
| `expiration` | [`Expiry`](../../doc/models/expiry.md) | Required | - |
| `pan` | `str` | Required | The primary account number (PAN) of the card. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.expiry import Expiry
from adyen.models.payment_instrument_reveal_info import PaymentInstrumentRevealInfo

payment_instrument_reveal_info = PaymentInstrumentRevealInfo(
    cvc='cvc2',
    expiration=Expiry(
        month='month6',
        year='year8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    pan='pan0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

