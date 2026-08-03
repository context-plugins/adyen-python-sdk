
# Merchant Device

Merchant device information.

*This model accepts additional fields of type Any.*

## Structure

`MerchantDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `os` | `str` | Optional | Operating system running on the merchant device. |
| `os_version` | `str` | Optional | Version of the operating system on the merchant device. |
| `reference` | `str` | Optional | Merchant device reference. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.merchant_device import MerchantDevice

merchant_device = MerchantDevice(
    os='os4',
    os_version='osVersion6',
    reference='reference8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

