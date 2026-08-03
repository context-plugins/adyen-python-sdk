
# Device Render Options 2

*This model accepts additional fields of type Any.*

## Structure

`DeviceRenderOptions2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_interface` | [`SdkInterface`](../../doc/models/sdk-interface.md) | Optional | - |
| `sdk_ui_type` | [`List[SdkUiType]`](../../doc/models/sdk-ui-type.md) | Optional | UI types supported for displaying specific challenges.<br>Allowed values:<br><br>* text<br>* singleSelect<br>* outOfBand<br>* otherHtml<br>* multiSelect |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device_render_options_2 import DeviceRenderOptions2
from adyen.models.sdk_interface import SdkInterface
from adyen.models.sdk_ui_type import SdkUiType

device_render_options_2 = DeviceRenderOptions2(
    sdk_interface=SdkInterface.HTML,
    sdk_ui_type=[
        SdkUiType.MULTISELECT
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

