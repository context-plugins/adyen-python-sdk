
# Shopper Interaction Device

Shopper interaction device, such as terminal, mobile device or web browser, to initiate payment requests.

*This model accepts additional fields of type Any.*

## Structure

`ShopperInteractionDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `locale` | `str` | Optional | Locale on the shopper interaction device. |
| `os` | `str` | Optional | Operating system running on the shopper interaction device. |
| `os_version` | `str` | Optional | Version of the operating system on the shopper interaction device. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.shopper_interaction_device import ShopperInteractionDevice

shopper_interaction_device = ShopperInteractionDevice(
    locale='locale2',
    os='os2',
    os_version='osVersion4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

