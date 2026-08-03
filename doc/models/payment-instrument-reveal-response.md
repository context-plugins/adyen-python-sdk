
# Payment Instrument Reveal Response

*This model accepts additional fields of type Any.*

## Structure

`PaymentInstrumentRevealResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `encrypted_data` | `str` | Required | The data encrypted using the `encryptedKey`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_instrument_reveal_response import PaymentInstrumentRevealResponse

payment_instrument_reveal_response = PaymentInstrumentRevealResponse(
    encrypted_data='encryptedData2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

