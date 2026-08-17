
# Application Info

Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions).

## Structure

`ApplicationInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adyen_library` | [`CommonField4`](../../doc/models/common-field-4.md) | Optional | Adyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example, Magento plugin, Java API library, etc. |
| `adyen_payment_source` | [`CommonField1`](../../doc/models/common-field-1.md) | Optional | Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc. |
| `external_platform` | [`ExternalPlatform`](../../doc/models/external-platform.md) | Optional | Third-party developed platform used to initiate payment requests. For example, Magento, Zuora, etc. |
| `merchant_application` | [`CommonField2`](../../doc/models/common-field-2.md) | Optional | Merchant developed software, such as cashier application, used to interact with the Adyen API. |
| `merchant_device` | [`MerchantDevice`](../../doc/models/merchant-device.md) | Optional | Merchant device information. |
| `shopper_interaction_device` | [`ShopperInteractionDevice`](../../doc/models/shopper-interaction-device.md) | Optional | Shopper interaction device, such as terminal, mobile device or web browser, to initiate payment requests. |

## Example

```python
from adyen.models.application_info import ApplicationInfo
from adyen.models.common_field_1 import CommonField1
from adyen.models.common_field_2 import CommonField2
from adyen.models.common_field_4 import CommonField4
from adyen.models.external_platform import ExternalPlatform
from adyen.models.merchant_device import MerchantDevice

application_info = ApplicationInfo(
    adyen_library=CommonField4(
        name='name8',
        version='version4'
    ),
    adyen_payment_source=CommonField1(
        name='name2',
        version='version8'
    ),
    external_platform=ExternalPlatform(
        integrator='integrator0',
        name='name4',
        version='version0'
    ),
    merchant_application=CommonField2(
        name='name2',
        version='version8'
    ),
    merchant_device=MerchantDevice(
        os='os4',
        os_version='osVersion6',
        reference='reference8'
    )
)
```

