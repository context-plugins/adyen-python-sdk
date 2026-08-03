
# Payment Instrument 3

Contains information about the payment instrument used in the transfer.

*This model accepts additional fields of type Any.*

## Structure

`PaymentInstrument3`

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

from adyen.models.payment_instrument_3 import PaymentInstrument3

payment_instrument_3 = PaymentInstrument3(
    description='description8',
    id='id8',
    reference='reference6',
    token_type='tokenType4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

