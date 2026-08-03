
# Grant Account

*This model accepts additional fields of type Any.*

## Structure

`GrantAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balances` | [`List[CapitalBalance]`](../../doc/models/capital-balance.md) | Optional | Contains the sum of the balances of all grants tracked by this grant account. The balances are separated by currency. |
| `funding_balance_account_id` | `str` | Optional | The unique identifier of the balance account used to fund the grant. |
| `id` | `str` | Optional | The unique identifier of the grant account. |
| `limits` | [`List[GrantLimit]`](../../doc/models/grant-limit.md) | Optional | Contains the maximum amount of funds that you can disburse for grants. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.capital_balance import CapitalBalance
from adyen.models.grant_account import GrantAccount
from adyen.models.grant_limit import GrantLimit

grant_account = GrantAccount(
    balances=[
        CapitalBalance(
            currency='currency0',
            fee=72,
            principal=110,
            total=150,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    funding_balance_account_id='fundingBalanceAccountId8',
    id='id4',
    limits=[
        GrantLimit(
            amount=Amount5(
                currency='currency2',
                value=110,
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

