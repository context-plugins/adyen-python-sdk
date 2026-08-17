
# Grants

## Structure

`Grants`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grants` | [`List[Grant]`](../../doc/models/grant.md) | Required | Contains a list of the grants that the account holder has received. |

## Example

```python
from adyen.models.action_1 import Action1
from adyen.models.capital_balance import CapitalBalance
from adyen.models.code_enum import CodeEnum
from adyen.models.grant import Grant
from adyen.models.grant_counterparty import GrantCounterparty
from adyen.models.grants import Grants
from adyen.models.status_25 import Status25

grants = Grants(
    grants=[
        Grant(
            balances=CapitalBalance(
                currency='currency0',
                fee=72,
                principal=110,
                total=150
            ),
            grant_account_id='grantAccountId6',
            grant_offer_id='grantOfferId6',
            id='id0',
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
    ]
)
```

