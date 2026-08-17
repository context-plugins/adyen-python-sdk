
# Payment Instrument Reveal Request

## Structure

`PaymentInstrumentRevealRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encrypted_key` | `str` | Required | The symmetric session key that you encrypted with the [public key](https://docs.adyen.com/api-explorer/balanceplatform/2/get/publicKey) that you received from Adyen. |
| `payment_instrument_id` | `str` | Required | The unique identifier of the payment instrument, which is the card for which you are managing the PIN. |

## Example

```python
from adyen.models.payment_instrument_reveal_request import PaymentInstrumentRevealRequest

payment_instrument_reveal_request = PaymentInstrumentRevealRequest(
    encrypted_key='encryptedKey8',
    payment_instrument_id='paymentInstrumentId8'
)
```

