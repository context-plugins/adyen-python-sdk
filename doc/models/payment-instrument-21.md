
# Payment Instrument 21

Contains information about the payment instrument that was used for the transaction.

## Structure

`PaymentInstrument21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `reference` | `str` | Optional | The reference for the resource. |
| `token_type` | `str` | Optional | The type of wallet that the network token is associated with. |

## Example

```python
from adyen.models.payment_instrument_21 import PaymentInstrument21

payment_instrument_21 = PaymentInstrument21(
    description='description2',
    id='id2',
    reference='reference8',
    token_type='tokenType8'
)
```

