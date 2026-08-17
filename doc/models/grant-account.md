
# Grant Account

## Structure

`GrantAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balances` | [`List[CapitalBalance]`](../../doc/models/capital-balance.md) | Optional | Contains the sum of the balances of all grants tracked by this grant account. The balances are separated by currency. |
| `funding_balance_account_id` | `str` | Optional | The unique identifier of the balance account used to fund the grant. |
| `id` | `str` | Optional | The unique identifier of the grant account. |
| `limits` | [`List[GrantLimit1]`](../../doc/models/grant-limit-1.md) | Optional | Contains the maximum amount of funds that you can disburse for grants. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.capital_balance import CapitalBalance
from adyen.models.grant_account import GrantAccount
from adyen.models.grant_limit_1 import GrantLimit1

grant_account = GrantAccount(
    balances=[
        CapitalBalance(
            currency='currency0',
            fee=72,
            principal=110,
            total=150
        )
    ],
    funding_balance_account_id='fundingBalanceAccountId8',
    id='id4',
    limits=[
        GrantLimit1(
            amount=Amount17(
                currency='currency2',
                value=110
            )
        )
    ]
)
```

