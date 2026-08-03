
# Shopper Interaction Device 2

*This model accepts additional fields of type Any.*

## Structure

`ShopperInteractionDevice2`

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

from adyen.models.shopper_interaction_device_2 import ShopperInteractionDevice2

shopper_interaction_device_2 = ShopperInteractionDevice2(
    locale='locale8',
    os='os8',
    os_version='osVersion0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

