
# Grant Info Counterparty

Contains the details of the party that receives the grant.

## Structure

`GrantInfoCounterparty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The identifier of the balance account that belongs to the receiving account holder. |
| `transfer_instrument_id` | `str` | Optional | The identifier of the transfer instrument that belongs to the legal entity of the account holder. |

## Example

```python
from adyen.models.grant_info_counterparty import GrantInfoCounterparty

grant_info_counterparty = GrantInfoCounterparty(
    balance_account_id='balanceAccountId2',
    transfer_instrument_id='transferInstrumentId6'
)
```

