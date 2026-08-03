
# Device Render Options

Display options for the 3D Secure 2 SDK.
Optional and only for `deviceChannel` **app**.

*This model accepts additional fields of type Any.*

## Structure

`DeviceRenderOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_interface` | [`SdkInterface`](../../doc/models/sdk-interface.md) | Optional | - |
| `sdk_ui_type` | [`List[SdkUiType]`](../../doc/models/sdk-ui-type.md) | Optional | UI types supported for displaying specific challenges.<br>Allowed values:<br><br>* text<br>* singleSelect<br>* outOfBand<br>* otherHtml<br>* multiSelect |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device_render_options import DeviceRenderOptions
from adyen.models.sdk_interface import SdkInterface
from adyen.models.sdk_ui_type import SdkUiType

device_render_options = DeviceRenderOptions(
    sdk_interface=SdkInterface.NATIVE,
    sdk_ui_type=[
        SdkUiType.SINGLESELECT,
        SdkUiType.TEXT,
        SdkUiType.MULTISELECT
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

