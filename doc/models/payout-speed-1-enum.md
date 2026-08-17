
# Payout Speed 1 Enum

Speed at which payouts for this account are processed.

Possible values: `STANDARD` (default), `SAME_DAY`.

## Enumeration

`PayoutSpeed1Enum`

## Fields

| Name |
|  --- |
| `INSTANT` |
| `SAME_DAY` |
| `STANDARD` |

## Example

```python
from adyen.models.payout_speed_1_enum import PayoutSpeed1Enum

payout_speed_1 = PayoutSpeed1Enum.INSTANT
```

