
# Pin Change Request

## Structure

`PinChangeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encrypted_key` | `str` | Required | The symmetric session key that you encrypted with the [public key](https://docs.adyen.com/api-explorer/balanceplatform/2/get/publicKey) that you received from Adyen. |
| `encrypted_pin_block` | `str` | Required | The encrypted [PIN block](https://www.pcisecuritystandards.org/glossary/pin-block). |
| `payment_instrument_id` | `str` | Required | The unique identifier of the payment instrument, which is the card for which you are managing the PIN. |
| `token` | `str` | Required | The 16-digit token that you used to generate the `encryptedPinBlock`. |

## Example

```python
from adyen.models.pin_change_request import PinChangeRequest

pin_change_request = PinChangeRequest(
    encrypted_key='encryptedKey6',
    encrypted_pin_block='encryptedPinBlock8',
    payment_instrument_id='paymentInstrumentId0',
    token='token8'
)
```

