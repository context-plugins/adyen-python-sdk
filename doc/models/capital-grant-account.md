
# Capital Grant Account

## Structure

`CapitalGrantAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balances` | [`List[CapitalBalance]`](../../doc/models/capital-balance.md) | Optional | The balances of the grant account. |
| `funding_balance_account_id` | `str` | Optional | The unique identifier of the balance account used to fund the grant. |
| `id` | `str` | Optional | The identifier of the grant account. |
| `limits` | [`List[GrantLimit]`](../../doc/models/grant-limit.md) | Optional | The limits of the grant account. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.capital_balance import CapitalBalance
from adyen.models.capital_grant_account import CapitalGrantAccount
from adyen.models.grant_limit import GrantLimit

capital_grant_account = CapitalGrantAccount(
    balances=[
        CapitalBalance(
            currency='currency0',
            fee=72,
            principal=110,
            total=150
        ),
        CapitalBalance(
            currency='currency0',
            fee=72,
            principal=110,
            total=150
        ),
        CapitalBalance(
            currency='currency0',
            fee=72,
            principal=110,
            total=150
        )
    ],
    funding_balance_account_id='fundingBalanceAccountId6',
    id='id6',
    limits=[
        GrantLimit(
            amount=Amount17(
                currency='currency2',
                value=110
            )
        ),
        GrantLimit(
            amount=Amount17(
                currency='currency2',
                value=110
            )
        ),
        GrantLimit(
            amount=Amount17(
                currency='currency2',
                value=110
            )
        )
    ]
)
```

