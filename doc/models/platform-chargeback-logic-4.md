
# Platform Chargeback Logic 4

Dictates the behavior of how a potential chargeback should be booked when using Adyen Platforms.

*This model accepts additional fields of type Any.*

## Structure

`PlatformChargebackLogic4`

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
from adyen.models.platform_chargeback_logic_4 import PlatformChargebackLogic4

platform_chargeback_logic_4 = PlatformChargebackLogic4(
    behavior=Behavior.DEDUCTACCORDINGTOSPLITRATIO,
    cost_allocation_account='costAllocationAccount8',
    target_account='targetAccount6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

