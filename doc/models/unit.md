
# Unit

The unit of time. You can only use **minutes** and **hours** if the `interval.type` is **sliding**.

Possible values: **minutes**, **hours**, **days**, **weeks**, or **months**

## Enumeration

`Unit`

## Fields

| Name |
|  --- |
| `DAYS` |
| `HOURS` |
| `MINUTES` |
| `MONTHS` |
| `WEEKS` |

## Example

```python
from adyen.models.unit import Unit

unit = Unit.MONTHS
```

