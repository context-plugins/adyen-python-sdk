
# Platform Chargeback Logic

Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/adyen-for-platforms-model).

## Structure

`PlatformChargebackLogic`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `behavior` | [`BehaviorEnum`](../../doc/models/behavior-enum.md) | Optional | The method of handling the chargeback.<br><br>Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**. |
| `cost_allocation_account` | `str` | Optional | The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account. |
| `target_account` | `str` | Optional | The unique identifier of the balance account against which the disputed amount is booked.<br><br>Required if `behavior` is **deductFromOneBalanceAccount**. |

## Example

```python
from adyen.models.behavior_enum import BehaviorEnum
from adyen.models.platform_chargeback_logic import PlatformChargebackLogic

platform_chargeback_logic = PlatformChargebackLogic(
    behavior=BehaviorEnum.DEDUCTFROMLIABLEACCOUNT,
    cost_allocation_account='costAllocationAccount6',
    target_account='targetAccount4'
)
```

