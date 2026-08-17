
# Merchant Balance

## Structure

`MerchantBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `available_fund` | [`Amount17`](../../doc/models/amount-17.md) | Optional | - |
| `deposit` | [`Amount17`](../../doc/models/amount-17.md) | Optional | - |
| `merchant_account` | `str` | Optional | - |
| `next_payout` | [`Amount17`](../../doc/models/amount-17.md) | Optional | - |
| `pending_balance` | [`Amount17`](../../doc/models/amount-17.md) | Optional | - |
| `reserve` | [`Amount17`](../../doc/models/amount-17.md) | Optional | - |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.merchant_balance import MerchantBalance

merchant_balance = MerchantBalance(
    available_fund=Amount17(
        currency='currency4',
        value=152
    ),
    deposit=Amount17(
        currency='currency4',
        value=62
    ),
    merchant_account='merchantAccount4',
    next_payout=Amount17(
        currency='currency4',
        value=240
    ),
    pending_balance=Amount17(
        currency='currency2',
        value=254
    )
)
```

