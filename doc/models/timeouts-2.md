
# Timeouts 2

Settings for device [time-outs](https://docs.adyen.com/point-of-sale/pos-timeouts#device-time-out).

## Structure

`Timeouts2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_active_to_sleep` | `int` | Optional | Indicates the number of seconds of inactivity after which the terminal display goes into sleep mode. |

## Example

```python
from adyen.models.timeouts_2 import Timeouts2

timeouts_2 = Timeouts2(
    from_active_to_sleep=12
)
```

