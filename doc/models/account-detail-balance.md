
# Account Detail Balance

*This model accepts additional fields of type Any.*

## Structure

`AccountDetailBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Optional | The code of the account that holds the balance. |
| `detail_balance` | [`DetailBalance`](../../doc/models/detail-balance.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_detail_balance import AccountDetailBalance
from adyen.models.amount_2 import Amount2
from adyen.models.detail_balance import DetailBalance

account_detail_balance = AccountDetailBalance(
    account_code='accountCode0',
    detail_balance=DetailBalance(
        balance=[
            Amount2(
                currency='currency4',
                value=128,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            Amount2(
                currency='currency4',
                value=128,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        on_hold_balance=[
            Amount2(
                currency='currency8',
                value=72,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            Amount2(
                currency='currency8',
                value=72,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            Amount2(
                currency='currency8',
                value=72,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        pending_balance=[
            Amount2(
                currency='currency2',
                value=254,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

