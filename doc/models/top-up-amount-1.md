
# Top Up Amount 1

The currency and value to be added to the balance account, specified in minor units. This can be a fixed amount or a target amount.

*This model accepts additional fields of type Any.*

## Structure

`TopUpAmount1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fixed` | [`Fixed`](../../doc/models/fixed.md) | Optional | - |
| `target` | [`Target5`](../../doc/models/target-5.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.fixed import Fixed
from adyen.models.target_5 import Target5
from adyen.models.top_up_amount_1 import TopUpAmount1

top_up_amount_1 = TopUpAmount1(
    fixed=Fixed(
        currency='currency0',
        value=164,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    target=Target5(
        currency='currency2',
        value=188,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

