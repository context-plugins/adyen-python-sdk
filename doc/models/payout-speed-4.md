
# Payout Speed 4

Speed at which payouts for this account are processed.

Possible values: `STANDARD`, `SAME_DAY`.

## Enumeration

`PayoutSpeed4`

## Fields

| Name |
|  --- |
| `INSTANT` |
| `SAME_DAY` |
| `STANDARD` |

## Example

```python
from adyen.models.payout_speed_4 import PayoutSpeed4

payout_speed_4 = PayoutSpeed4.INSTANT
```

