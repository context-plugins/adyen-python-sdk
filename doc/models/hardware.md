
# Hardware

*This model accepts additional fields of type Any.*

## Structure

`Hardware`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_maximum_back_light` | `int` | Optional | The brightness of the display when the terminal is being used, expressed as a percentage. |
| `reset_totals_hour` | `int` | Optional | The hour of the day when the terminal is set to reset the Totals report. By default, the reset hour is at 6:00 AM in the timezone of the terminal. Minimum value: 0, maximum value: 23. |
| `restart_hour` | `int` | Optional | The hour of the day when the terminal is set to reboot to apply the configuration and software updates. By default, the restart hour is at 6:00 AM in the timezone of the terminal. Minimum value: 0, maximum value: 23. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.hardware import Hardware

hardware = Hardware(
    display_maximum_back_light=142,
    reset_totals_hour=132,
    restart_hour=110,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

