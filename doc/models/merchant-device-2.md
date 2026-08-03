
# Merchant Device 2

*This model accepts additional fields of type Any.*

## Structure

`MerchantDevice2`

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

from adyen.models.merchant_device_2 import MerchantDevice2

merchant_device_2 = MerchantDevice2(
    os='os4',
    os_version='osVersion6',
    reference='reference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

