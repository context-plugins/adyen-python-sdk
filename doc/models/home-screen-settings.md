
# Home Screen Settings

## Structure

`HomeScreenSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hide_navigation_bar` | `bool` | Optional | Hide/show the navigation bar. |
| `show_payments_menu` | `bool` | Optional | Show/hide the payments menu. |
| `show_settings_menu` | `bool` | Optional | Show/hide the settings menu. |

## Example

```python
from adyen.models.home_screen_settings import HomeScreenSettings

home_screen_settings = HomeScreenSettings(
    hide_navigation_bar=False,
    show_payments_menu=False,
    show_settings_menu=False
)
```

