
# Capital Grant Info

## Structure

`CapitalGrantInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `counterparty` | [`GrantInfoCounterparty2`](../../doc/models/grant-info-counterparty-2.md) | Optional | An object containing the details of the receiving party of the grant. |
| `grant_account_id` | `str` | Required | The identifier of the grant account used for the grant. |
| `grant_offer_id` | `str` | Required | The identifier of the grant offer that has been selected and from which the grant details will be used. |

## Example

```python
from adyen.models.capital_grant_info import CapitalGrantInfo
from adyen.models.grant_info_counterparty_2 import GrantInfoCounterparty2

capital_grant_info = CapitalGrantInfo(
    grant_account_id='grantAccountId6',
    grant_offer_id='grantOfferId6',
    counterparty=GrantInfoCounterparty2(
        balance_account_id='balanceAccountId0',
        transfer_instrument_id='transferInstrumentId4'
    )
)
```

