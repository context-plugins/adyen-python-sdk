
# Platform Chargeback Logic 1

*This model accepts additional fields of type Any.*

## Structure

`PlatformChargebackLogic1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `behavior` | [`Behavior`](../../doc/models/behavior.md) | Optional | - |
| `cost_allocation_account` | `str` | Optional | The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account. |
| `target_account` | `str` | Optional | The unique identifier of the balance account against which the disputed amount is booked.<br><br>Required if `behavior` is **deductFromOneBalanceAccount**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.behavior import Behavior
from adyen.models.platform_chargeback_logic_1 import PlatformChargebackLogic1

platform_chargeback_logic_1 = PlatformChargebackLogic1(
    behavior=Behavior.DEDUCTFROMLIABLEACCOUNT,
    cost_allocation_account='costAllocationAccount2',
    target_account='targetAccount0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

