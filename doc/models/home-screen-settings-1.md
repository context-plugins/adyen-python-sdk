
# Home Screen Settings 1

Settings for the home screen.

*This model accepts additional fields of type Any.*

## Structure

`HomeScreenSettings1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hide_navigation_bar` | `bool` | Optional | Hide/show the navigation bar. |
| `show_payments_menu` | `bool` | Optional | Show/hide the payments menu. |
| `show_settings_menu` | `bool` | Optional | Show/hide the settings menu. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.home_screen_settings_1 import HomeScreenSettings1

home_screen_settings_1 = HomeScreenSettings1(
    hide_navigation_bar=False,
    show_payments_menu=False,
    show_settings_menu=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

