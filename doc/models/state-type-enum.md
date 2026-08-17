
# State Type Enum

The state to be updated.

> Permitted values are: `Processing`, `Payout`

## Enumeration

`StateTypeEnum`

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
from adyen.models.state_type_enum import StateTypeEnum

state_type = StateTypeEnum.LIMITLESSPAYOUT
```

