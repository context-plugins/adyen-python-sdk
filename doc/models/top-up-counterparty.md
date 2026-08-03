
# Top Up Counterparty

*This model accepts additional fields of type Any.*

## Structure

`TopUpCounterparty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_instrument_id` | `str` | Required | The unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id) that is funding the top-up. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.top_up_counterparty import TopUpCounterparty

top_up_counterparty = TopUpCounterparty(
    transfer_instrument_id='transferInstrumentId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

