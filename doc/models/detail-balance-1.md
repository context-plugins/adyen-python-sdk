
# Detail Balance 1

The total balance of the account holder.

## Structure

`DetailBalance1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance` | [`List[Amount]`](../../doc/models/amount.md) | Optional | The list of balances held by the account. |
| `on_hold_balance` | [`List[Amount]`](../../doc/models/amount.md) | Optional | The list of on hold balances held by the account. |
| `pending_balance` | [`List[Amount]`](../../doc/models/amount.md) | Optional | The list of pending balances held by the account. |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.detail_balance_1 import DetailBalance1

detail_balance_1 = DetailBalance1(
    balance=[
        Amount(
            currency='currency4',
            value=128
        ),
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
        )
    ]
)
```

