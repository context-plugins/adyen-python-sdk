
# Cash Out Info Counterparty

*This model accepts additional fields of type Any.*

## Structure

`CashOutInfoCounterparty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the counterparty transfer instrument.<br><br>If you do not provide this field, the cashout funds remain in the instructing balance account after the cashout transfer is settled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.cash_out_info_counterparty import CashOutInfoCounterparty

cash_out_info_counterparty = CashOutInfoCounterparty(
    transfer_instrument_id='transferInstrumentId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

