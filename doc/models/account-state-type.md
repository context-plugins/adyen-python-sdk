
# Account State Type

The state required for the account holder.

> Permitted values: `Processing`, `Payout`.

## Enumeration

`AccountStateType`

## Fields

| Name |
|  --- |
| `LIMITEDPAYOUT` |
| `LIMITEDPROCESSING` |
| `LIMITLESSPAYOUT` |
| `LIMITLESSPROCESSING` |
| `PAYOUT` |
| `PROCESSING` |

## Example

```python
from adyen.models.account_state_type import AccountStateType

account_state_type = AccountStateType.PAYOUT
```

