
# Merchant Device

Merchant device information.

## Structure

`MerchantDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `os` | `str` | Optional | Operating system running on the merchant device. |
| `os_version` | `str` | Optional | Version of the operating system on the merchant device. |
| `reference` | `str` | Optional | Merchant device reference. |

## Example

```python
from adyen.models.merchant_device import MerchantDevice

merchant_device = MerchantDevice(
    os='os4',
    os_version='osVersion6',
    reference='reference8'
)
```

