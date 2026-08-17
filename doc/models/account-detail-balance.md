
# Account Detail Balance

## Structure

`AccountDetailBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Optional | The code of the account that holds the balance. |
| `detail_balance` | [`DetailBalance3`](../../doc/models/detail-balance-3.md) | Optional | Details of the balance held by the account. |

## Example

```python
from adyen.models.account_detail_balance import AccountDetailBalance
from adyen.models.amount import Amount
from adyen.models.detail_balance_3 import DetailBalance3

account_detail_balance = AccountDetailBalance(
    account_code='accountCode0',
    detail_balance=DetailBalance3(
        balance=[
            Amount(
                currency='currency4',
                value=128
            ),
            Amount(
                currency='currency4',
                value=128
            )
        ],
        on_hold_balance=[
            Amount(
                currency='currency8',
                value=72
            ),
            Amount(
                currency='currency8',
                value=72
            ),
            Amount(
                currency='currency8',
                value=72
            )
        ],
        pending_balance=[
            Amount(
                currency='currency2',
                value=254
            )
        ]
    )
)
```

