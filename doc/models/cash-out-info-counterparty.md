
# Cash Out Info Counterparty

## Structure

`CashOutInfoCounterparty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the counterparty transfer instrument.<br><br>If you do not provide this field, the cashout funds remain in the instructing balance account after the cashout transfer is settled. |

## Example

```python
from adyen.models.cash_out_info_counterparty import CashOutInfoCounterparty

cash_out_info_counterparty = CashOutInfoCounterparty(
    transfer_instrument_id='transferInstrumentId6'
)
```

