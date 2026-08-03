
# Condition

*This model accepts additional fields of type Any.*

## Structure

`Condition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_type` | [`BalanceType`](../../doc/models/balance-type.md) | Required | - |
| `condition_type` | [`ConditionType`](../../doc/models/condition-type.md) | Required | - |
| `value` | `int` | Required | The value limit in the specified balance type and currency, in minor units. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.balance_type import BalanceType
from adyen.models.condition import Condition
from adyen.models.condition_type import ConditionType

condition = Condition(
    balance_type=BalanceType.BALANCE,
    condition_type=ConditionType.LESSTHAN,
    value=194,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

