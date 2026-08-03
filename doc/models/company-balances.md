
# Company Balances

*This model accepts additional fields of type Any.*

## Structure

`CompanyBalances`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_balances_overview` | [`List[MerchantBalance]`](../../doc/models/merchant-balance.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_3 import Amount3
from adyen.models.company_balances import CompanyBalances
from adyen.models.merchant_balance import MerchantBalance

company_balances = CompanyBalances(
    merchant_balances_overview=[
        MerchantBalance(
            available_fund=Amount3(
                currency='currency4',
                value=152,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            deposit=Amount3(
                currency='currency4',
                value=62,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            merchant_account='merchantAccount4',
            next_payout=Amount3(
                currency='currency4',
                value=240,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            pending_balance=Amount3(
                currency='currency2',
                value=254,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

