
# Capital Grant Account

*This model accepts additional fields of type Any.*

## Structure

`CapitalGrantAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balances` | [`List[CapitalBalance]`](../../doc/models/capital-balance.md) | Optional | The balances of the grant account. |
| `funding_balance_account_id` | `str` | Optional | The unique identifier of the balance account used to fund the grant. |
| `id` | `str` | Optional | The identifier of the grant account. |
| `limits` | [`List[GrantLimit]`](../../doc/models/grant-limit.md) | Optional | The limits of the grant account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.capital_balance import CapitalBalance
from adyen.models.capital_grant_account import CapitalGrantAccount
from adyen.models.grant_limit import GrantLimit

capital_grant_account = CapitalGrantAccount(
    balances=[
        CapitalBalance(
            currency='currency0',
            fee=72,
            principal=110,
            total=150,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CapitalBalance(
            currency='currency0',
            fee=72,
            principal=110,
            total=150,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
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
    funding_balance_account_id='fundingBalanceAccountId6',
    id='id6',
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
        ),
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
        ),
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

