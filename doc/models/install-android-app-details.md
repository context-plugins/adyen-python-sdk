
# Install Android App Details

## Structure

`InstallAndroidAppDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `str` | Optional | The unique identifier of the app to be installed. |
| `mtype` | [`Type32Enum`](../../doc/models/type-32-enum.md) | Optional | Type of terminal action: Install an Android app.<br><br>**Default**: `"InstallAndroidApp"` |

## Example

```python
from adyen.models.install_android_app_details import InstallAndroidAppDetails
from adyen.models.type_32_enum import Type32Enum

install_android_app_details = InstallAndroidAppDetails(
    app_id='appId2',
    mtype=Type32Enum.INSTALLANDROIDAPP
)
```

