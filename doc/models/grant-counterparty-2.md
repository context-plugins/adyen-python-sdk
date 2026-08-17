
# Grant Counterparty 2

An object containing the details of the receiving party of the grant.

## Structure

`GrantCounterparty2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Optional | The identifier of the receiving account holder. |
| `balance_account_id` | `str` | Optional | The identifier of the balance account that belongs to the receiving account holder. |
| `transfer_instrument_id` | `str` | Optional | The identifier of the transfer instrument that belongs to the legal entity of the account holder. |

## Example

```python
from adyen.models.grant_counterparty_2 import GrantCounterparty2

grant_counterparty_2 = GrantCounterparty2(
    account_holder_id='accountHolderId6',
    balance_account_id='balanceAccountId6',
    transfer_instrument_id='transferInstrumentId2'
)
```

