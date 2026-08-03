
# Cash Out Transfer

*This model accepts additional fields of type Any.*

## Structure

`CashOutTransfer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `id` | `str` | Required | The reference of the cashout transfer. |
| `mtype` | [`Type122`](../../doc/models/type-122.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.cash_out_transfer import CashOutTransfer
from adyen.models.type_122 import Type122

cash_out_transfer = CashOutTransfer(
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    id='id6',
    mtype=Type122.CASHOUTREPAYMENT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

