
# Local Time 2

The time when the payout funds are settled in your user's transfer instrument.

## Structure

`LocalTime2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hour` | `int` | Optional | - |
| `minute` | `int` | Optional | - |
| `nano` | `int` | Optional | - |
| `second` | `int` | Optional | - |

## Example

```python
from adyen.models.local_time_2 import LocalTime2

local_time_2 = LocalTime2(
    hour=48,
    minute=50,
    nano=74,
    second=144
)
```

