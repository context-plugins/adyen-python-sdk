
# Grant Counterparty

Contains the details of the party that receives the grant.

## Structure

`GrantCounterparty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Optional | The identifier of the receiving account holder. |
| `balance_account_id` | `str` | Optional | The identifier of the balance account that belongs to the receiving account holder. |
| `transfer_instrument_id` | `str` | Optional | The identifier of the transfer instrument that belongs to the legal entity of the account holder. |

## Example

```python
from adyen.models.grant_counterparty import GrantCounterparty

grant_counterparty = GrantCounterparty(
    account_holder_id='accountHolderId4',
    balance_account_id='balanceAccountId4',
    transfer_instrument_id='transferInstrumentId0'
)
```

