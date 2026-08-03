
# Behavior

The method of handling the chargeback.

Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**.

## Enumeration

`Behavior`

## Fields

| Name |
|  --- |
| `DEDUCTFROMONEBALANCEACCOUNT` |
| `DEDUCTACCORDINGTOSPLITRATIO` |
| `DEDUCTFROMLIABLEACCOUNT` |

## Example

```python
from adyen.models.behavior import Behavior

behavior = Behavior.DEDUCTFROMLIABLEACCOUNT
```

