
# Mandate Update

*This model accepts additional fields of type Any.*

## Structure

`MandateUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument linked to the mandate. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mandate_update import MandateUpdate

mandate_update = MandateUpdate(
    payment_instrument_id='paymentInstrumentId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

