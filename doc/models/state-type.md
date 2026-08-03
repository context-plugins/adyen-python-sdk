
# State Type

The state to be updated.

> Permitted values are: `Processing`, `Payout`

## Enumeration

`StateType`

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
from adyen.models.state_type import StateType

state_type = StateType.LIMITLESSPAYOUT
```

