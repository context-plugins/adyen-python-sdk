
# Local Time

## Structure

`LocalTime`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hour` | `int` | Optional | - |
| `minute` | `int` | Optional | - |
| `nano` | `int` | Optional | - |
| `second` | `int` | Optional | - |

## Example

```python
from adyen.models.local_time import LocalTime

local_time = LocalTime(
    hour=180,
    minute=182,
    nano=206,
    second=244
)
```

