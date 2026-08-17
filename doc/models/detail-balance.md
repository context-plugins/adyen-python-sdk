
# Detail Balance

## Structure

`DetailBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance` | [`List[Amount]`](../../doc/models/amount.md) | Optional | The list of balances held by the account. |
| `on_hold_balance` | [`List[Amount]`](../../doc/models/amount.md) | Optional | The list of on hold balances held by the account. |
| `pending_balance` | [`List[Amount]`](../../doc/models/amount.md) | Optional | The list of pending balances held by the account. |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.detail_balance import DetailBalance

detail_balance = DetailBalance(
    balance=[
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
        )
    ],
    pending_balance=[
        Amount(
            currency='currency2',
            value=254
        ),
        Amount(
            currency='currency2',
            value=254
        ),
        Amount(
            currency='currency2',
            value=254
        )
    ]
)
```

