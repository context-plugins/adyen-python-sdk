
# Grant Info Counterparty 2

An object containing the details of the receiving party of the grant.

## Structure

`GrantInfoCounterparty2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The identifier of the balance account that belongs to the receiving account holder. |
| `transfer_instrument_id` | `str` | Optional | The identifier of the transfer instrument that belongs to the legal entity of the account holder. |

## Example

```python
from adyen.models.grant_info_counterparty_2 import GrantInfoCounterparty2

grant_info_counterparty_2 = GrantInfoCounterparty2(
    balance_account_id='balanceAccountId4',
    transfer_instrument_id='transferInstrumentId0'
)
```

