
# Payment Instrument 2

## Structure

`PaymentInstrument2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `reference` | `str` | Optional | The reference for the resource. |
| `token_type` | `str` | Optional | The type of wallet that the network token is associated with. |

## Example

```python
from adyen.models.payment_instrument_2 import PaymentInstrument2

payment_instrument_2 = PaymentInstrument2(
    description='description0',
    id='id0',
    reference='reference4',
    token_type='tokenType4'
)
```

