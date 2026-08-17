
# Company Balances

## Structure

`CompanyBalances`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_balances_overview` | [`List[MerchantBalance]`](../../doc/models/merchant-balance.md) | Optional | - |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.company_balances import CompanyBalances
from adyen.models.merchant_balance import MerchantBalance

company_balances = CompanyBalances(
    merchant_balances_overview=[
        MerchantBalance(
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
    ]
)
```

