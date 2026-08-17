
# Mandate Update

## Structure

`MandateUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument linked to the mandate. |

## Example

```python
from adyen.models.mandate_update import MandateUpdate

mandate_update = MandateUpdate(
    payment_instrument_id='paymentInstrumentId8'
)
```

