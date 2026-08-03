
# Payment Instrument Resource

*This model accepts additional fields of type Any.*

## Structure

`PaymentInstrumentResource`

## Inherits From

[`Resource`](../../doc/models/resource.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_id` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.resource import PaymentInstrumentResource

payment_instrument_resource = PaymentInstrumentResource(
    payment_instrument_id='paymentInstrumentId0',
    mtype='paymentInstrument',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

