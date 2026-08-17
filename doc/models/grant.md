
# Grant

## Structure

`Grant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balances` | [`CapitalBalance`](../../doc/models/capital-balance.md) | Required | Contains information about the balances of the grant. |
| `counterparty` | [`GrantCounterparty`](../../doc/models/grant-counterparty.md) | Optional | Contains the details of the party that receives the grant. |
| `grant_account_id` | `str` | Required | The unique identifier of the grant account that tracks this grant. |
| `grant_offer_id` | `str` | Required | The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant. |
| `id` | `str` | Required | The unique identifier of the grant reference. |
| `status` | [`Status25`](../../doc/models/status-25.md) | Required | Contains the status of the grant. |

## Example

```python
from adyen.models.action_1 import Action1
from adyen.models.capital_balance import CapitalBalance
from adyen.models.code_enum import CodeEnum
from adyen.models.grant import Grant
from adyen.models.grant_counterparty import GrantCounterparty
from adyen.models.status_25 import Status25

grant = Grant(
    balances=CapitalBalance(
        currency='currency0',
        fee=72,
        principal=110,
        total=150
    ),
    grant_account_id='grantAccountId8',
    grant_offer_id='grantOfferId4',
    id='id2',
    status=Status25(
        code=CodeEnum.REJECTED,
        actions=[
            Action1(
                action_code='actionCode6',
                resolved=False
            )
        ]
    ),
    counterparty=GrantCounterparty(
        account_holder_id='accountHolderId0',
        balance_account_id='balanceAccountId0',
        transfer_instrument_id='transferInstrumentId4'
    )
)
```

