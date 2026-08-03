
# Reveal Pin Request

*This model accepts additional fields of type Any.*

## Structure

`RevealPinRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encrypted_key` | `str` | Required | The symmetric session key that you encrypted with the [public key](https://docs.adyen.com/api-explorer/balanceplatform/2/get/publicKey) that you received from Adyen. |
| `payment_instrument_id` | `str` | Required | The unique identifier of the payment instrument, which is the card for which you are managing the PIN. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.reveal_pin_request import RevealPinRequest

reveal_pin_request = RevealPinRequest(
    encrypted_key='encryptedKey0',
    payment_instrument_id='paymentInstrumentId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

