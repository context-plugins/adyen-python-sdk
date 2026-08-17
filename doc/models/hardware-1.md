
# Hardware 1

Settings for terminal hardware features.

## Structure

`Hardware1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_maximum_back_light` | `int` | Optional | The brightness of the display when the terminal is being used, expressed as a percentage. |
| `reset_totals_hour` | `int` | Optional | The hour of the day when the terminal is set to reset the Totals report. By default, the reset hour is at 6:00 AM in the timezone of the terminal. Minimum value: 0, maximum value: 23. |
| `restart_hour` | `int` | Optional | The hour of the day when the terminal is set to reboot to apply the configuration and software updates. By default, the restart hour is at 6:00 AM in the timezone of the terminal. Minimum value: 0, maximum value: 23. |

## Example

```python
from adyen.models.hardware_1 import Hardware1

hardware_1 = Hardware1(
    display_maximum_back_light=104,
    reset_totals_hour=114,
    restart_hour=136
)
```

