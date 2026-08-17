
# Top Up Counterparty 1

The details about the counterparty that is funding the top-up.

## Structure

`TopUpCounterparty1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_instrument_id` | `str` | Required | The unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id) that is funding the top-up. |

## Example

```python
from adyen.models.top_up_counterparty_1 import TopUpCounterparty1

top_up_counterparty_1 = TopUpCounterparty1(
    transfer_instrument_id='transferInstrumentId2'
)
```

