
# Detail Balance 1

The total balance of the account holder.

*This model accepts additional fields of type Any.*

## Structure

`DetailBalance1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance` | [`List[Amount2]`](../../doc/models/amount-2.md) | Optional | The list of balances held by the account. |
| `on_hold_balance` | [`List[Amount2]`](../../doc/models/amount-2.md) | Optional | The list of on hold balances held by the account. |
| `pending_balance` | [`List[Amount2]`](../../doc/models/amount-2.md) | Optional | The list of pending balances held by the account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_2 import Amount2
from adyen.models.detail_balance_1 import DetailBalance1

detail_balance_1 = DetailBalance1(
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
        )
    ],
    pending_balance=[
        Amount2(
            currency='currency2',
            value=254,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
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
)
```

