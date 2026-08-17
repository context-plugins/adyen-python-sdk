
# Payout Speed Enum

Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.

## Enumeration

`PayoutSpeedEnum`

## Fields

| Name |
|  --- |
| `INSTANT` |
| `SAME_DAY` |
| `STANDARD` |

## Example

```python
from adyen.models.payout_speed_enum import PayoutSpeedEnum

payout_speed = PayoutSpeedEnum.INSTANT
```

