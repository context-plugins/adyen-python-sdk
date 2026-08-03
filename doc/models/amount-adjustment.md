
# Amount Adjustment

*This model accepts additional fields of type Any.*

## Structure

`AmountAdjustment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Optional | - |
| `amount_adjustment_type` | [`AmountAdjustmentType`](../../doc/models/amount-adjustment-type.md) | Optional | - |
| `basepoints` | `int` | Optional | The basepoints associated with the applied markup. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.amount_adjustment import AmountAdjustment
from adyen.models.amount_adjustment_type import AmountAdjustmentType

amount_adjustment = AmountAdjustment(
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    amount_adjustment_type=AmountAdjustmentType.ATMMARKUP,
    basepoints=162,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

