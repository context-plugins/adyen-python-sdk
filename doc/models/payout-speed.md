
# Payout Speed

Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.

## Enumeration

`PayoutSpeed`

## Fields

| Name |
|  --- |
| `INSTANT` |
| `SAME_DAY` |
| `STANDARD` |

## Example

```python
from adyen.models.payout_speed import PayoutSpeed

payout_speed = PayoutSpeed.INSTANT
```

