
# Kiosk Mode Settings

*This model accepts additional fields of type Any.*

## Structure

`KioskModeSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_apps_in_kiosk_mode` | `List[str]` | Optional | List of package names for apps allowed to run in kiosk mode. |
| `kiosk_app_on_startup` | `str` | Optional | The package name of the app to launch on startup. This must be one of the apps included in `allowedAppsInKioskMode`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.kiosk_mode_settings import KioskModeSettings

kiosk_mode_settings = KioskModeSettings(
    allowed_apps_in_kiosk_mode=[
        'allowedAppsInKioskMode0',
        'allowedAppsInKioskMode9',
        'allowedAppsInKioskMode8'
    ],
    kiosk_app_on_startup='kioskAppOnStartup4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

