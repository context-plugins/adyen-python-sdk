
# Uninstall Android App Details

*This model accepts additional fields of type Any.*

## Structure

`UninstallAndroidAppDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `str` | Optional | The unique identifier of the app to be uninstalled. |
| `mtype` | [`Type73`](../../doc/models/type-73.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_73 import Type73
from adyen.models.uninstall_android_app_details import UninstallAndroidAppDetails

uninstall_android_app_details = UninstallAndroidAppDetails(
    app_id='appId2',
    mtype=Type73.UNINSTALLANDROIDAPP,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

