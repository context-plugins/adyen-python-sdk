
# Cash Out Info Counterparty 1

Contains information about the counterparty of the cashout transfer.

## Structure

`CashOutInfoCounterparty1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the counterparty transfer instrument.<br><br>If you do not provide this field, the cashout funds remain in the instructing balance account after the cashout transfer is settled. |

## Example

```python
from adyen.models.cash_out_info_counterparty_1 import CashOutInfoCounterparty1

cash_out_info_counterparty_1 = CashOutInfoCounterparty1(
    transfer_instrument_id='transferInstrumentId4'
)
```

