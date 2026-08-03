
# Payment Instrument 21

Contains information about the payment instrument that was used for the transaction.

*This model accepts additional fields of type Any.*

## Structure

`PaymentInstrument21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `reference` | `str` | Optional | The reference for the resource. |
| `token_type` | `str` | Optional | The type of wallet that the network token is associated with. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_instrument_21 import PaymentInstrument21

payment_instrument_21 = PaymentInstrument21(
    description='description2',
    id='id2',
    reference='reference8',
    token_type='tokenType8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

