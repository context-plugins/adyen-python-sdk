
# Device Render Options

Display options for the 3D Secure 2 SDK.
Optional and only for `deviceChannel` **app**.

## Structure

`DeviceRenderOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_interface` | [`SdkInterfaceEnum`](../../doc/models/sdk-interface-enum.md) | Optional | Supported SDK interface types.<br>Allowed values:<br><br>* native<br>* html<br>* both<br><br>**Default**: `"both"` |
| `sdk_ui_type` | [`List[SdkUiTypeEnum]`](../../doc/models/sdk-ui-type-enum.md) | Optional | UI types supported for displaying specific challenges.<br>Allowed values:<br><br>* text<br>* singleSelect<br>* outOfBand<br>* otherHtml<br>* multiSelect |

## Example

```python
from adyen.models.device_render_options import DeviceRenderOptions
from adyen.models.sdk_interface_enum import SdkInterfaceEnum
from adyen.models.sdk_ui_type_enum import SdkUiTypeEnum

device_render_options = DeviceRenderOptions(
    sdk_interface=SdkInterfaceEnum.BOTH,
    sdk_ui_type=[
        SdkUiTypeEnum.SINGLESELECT,
        SdkUiTypeEnum.TEXT,
        SdkUiTypeEnum.MULTISELECT
    ]
)
```

