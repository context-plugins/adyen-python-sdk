
# Behavior Enum

The method of handling the chargeback.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**., Specifies how and from which balance account(s) to deduct the chargeback amount.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**., Specifies how and from which balance account(s) to deduct the refund amount.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**

## Enumeration

`BehaviorEnum`

## Fields

| Name |
|  --- |
| `DEDUCTFROMONEBALANCEACCOUNT` |
| `DEDUCTACCORDINGTOSPLITRATIO` |
| `DEDUCTFROMLIABLEACCOUNT` |

## Example

```python
from adyen.models.behavior_enum import BehaviorEnum

behavior = BehaviorEnum.DEDUCTFROMLIABLEACCOUNT
```

