
# Payment Instrument Reveal Response

## Structure

`PaymentInstrumentRevealResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encrypted_data` | `str` | Required | The data encrypted using the `encryptedKey`. |

## Example

```python
from adyen.models.payment_instrument_reveal_response import PaymentInstrumentRevealResponse

payment_instrument_reveal_response = PaymentInstrumentRevealResponse(
    encrypted_data='encryptedData2'
)
```

