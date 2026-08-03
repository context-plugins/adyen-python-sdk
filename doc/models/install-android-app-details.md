
# Install Android App Details

*This model accepts additional fields of type Any.*

## Structure

`InstallAndroidAppDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `str` | Optional | The unique identifier of the app to be installed. |
| `mtype` | [`Type310`](../../doc/models/type-310.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.install_android_app_details import InstallAndroidAppDetails
from adyen.models.type_310 import Type310

install_android_app_details = InstallAndroidAppDetails(
    app_id='appId2',
    mtype=Type310.INSTALLANDROIDAPP,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

