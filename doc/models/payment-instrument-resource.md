
# Payment Instrument Resource

## Structure

`PaymentInstrumentResource`

## Inherits From

[`Resource`](../../doc/models/resource.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_id` | `str` | Required | **Constraints**: *Minimum Length*: `1` |

## Example

```python
from adyen.models.resource import PaymentInstrumentResource

payment_instrument_resource = PaymentInstrumentResource(
    payment_instrument_id='paymentInstrumentId0',
    mtype='paymentInstrument'
)
```

