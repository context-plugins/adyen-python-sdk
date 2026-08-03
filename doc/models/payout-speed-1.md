
# Payout Speed 1

Speed at which payouts for this account are processed.

Possible values: `STANDARD` (default), `SAME_DAY`.

## Enumeration

`PayoutSpeed1`

## Fields

| Name |
|  --- |
| `INSTANT` |
| `SAME_DAY` |
| `STANDARD` |

## Example

```python
from adyen.models.payout_speed_1 import PayoutSpeed1

payout_speed_1 = PayoutSpeed1.INSTANT
```

