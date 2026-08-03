
# Platform Chargeback Logic

Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/adyen-for-platforms-model).

*This model accepts additional fields of type Any.*

## Structure

`PlatformChargebackLogic`

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
from adyen.models.platform_chargeback_logic import PlatformChargebackLogic

platform_chargeback_logic = PlatformChargebackLogic(
    behavior=Behavior.DEDUCTFROMLIABLEACCOUNT,
    cost_allocation_account='costAllocationAccount6',
    target_account='targetAccount4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

