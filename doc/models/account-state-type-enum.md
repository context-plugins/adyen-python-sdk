
# Account State Type Enum

The state required for the account holder.

> Permitted values: `Processing`, `Payout`.

## Enumeration

`AccountStateTypeEnum`

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
from adyen.models.account_state_type_enum import AccountStateTypeEnum

account_state_type = AccountStateTypeEnum.PAYOUT
```

