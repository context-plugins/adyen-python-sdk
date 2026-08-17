
# Payout Speed 4 Enum

Speed at which payouts for this account are processed.

Possible values: `STANDARD`, `SAME_DAY`.

## Enumeration

`PayoutSpeed4Enum`

## Fields

| Name |
|  --- |
| `INSTANT` |
| `SAME_DAY` |
| `STANDARD` |

## Example

```python
from adyen.models.payout_speed_4_enum import PayoutSpeed4Enum

payout_speed_4 = PayoutSpeed4Enum.INSTANT
```

