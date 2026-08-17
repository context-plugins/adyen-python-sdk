
# Uninstall Android App Details

## Structure

`UninstallAndroidAppDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `str` | Optional | The unique identifier of the app to be uninstalled. |
| `mtype` | [`Type71Enum`](../../doc/models/type-71-enum.md) | Optional | Type of terminal action: Uninstall an Android app.<br><br>**Default**: `"UninstallAndroidApp"` |

## Example

```python
from adyen.models.type_71_enum import Type71Enum
from adyen.models.uninstall_android_app_details import UninstallAndroidAppDetails

uninstall_android_app_details = UninstallAndroidAppDetails(
    app_id='appId2',
    mtype=Type71Enum.UNINSTALLANDROIDAPP
)
```

