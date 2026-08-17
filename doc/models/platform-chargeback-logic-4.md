
# Platform Chargeback Logic 4

Dictates the behavior of how a potential chargeback should be booked when using Adyen Platforms.

## Structure

`PlatformChargebackLogic4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `behavior` | [`BehaviorEnum`](../../doc/models/behavior-enum.md) | Optional | The method of handling the chargeback.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**. |
| `cost_allocation_account` | `str` | Optional | The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account. |
| `target_account` | `str` | Optional | The unique identifier of the balance account against which the disputed amount is booked.<br><br>Required if `behavior` is **deductFromOneBalanceAccount**. |

## Example

```python
from adyen.models.behavior_enum import BehaviorEnum
from adyen.models.platform_chargeback_logic_4 import PlatformChargebackLogic4

platform_chargeback_logic_4 = PlatformChargebackLogic4(
    behavior=BehaviorEnum.DEDUCTACCORDINGTOSPLITRATIO,
    cost_allocation_account='costAllocationAccount8',
    target_account='targetAccount6'
)
```

