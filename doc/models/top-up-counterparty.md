
# Top Up Counterparty

## Structure

`TopUpCounterparty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_instrument_id` | `str` | Required | The unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id) that is funding the top-up. |

## Example

```python
from adyen.models.top_up_counterparty import TopUpCounterparty

top_up_counterparty = TopUpCounterparty(
    transfer_instrument_id='transferInstrumentId2'
)
```

