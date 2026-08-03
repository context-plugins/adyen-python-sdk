
# Application Info

Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions).

*This model accepts additional fields of type Any.*

## Structure

`ApplicationInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adyen_library` | [`AdyenLibrary`](../../doc/models/adyen-library.md) | Optional | - |
| `adyen_payment_source` | [`AdyenPaymentSource`](../../doc/models/adyen-payment-source.md) | Optional | - |
| `external_platform` | [`ExternalPlatform2`](../../doc/models/external-platform-2.md) | Optional | - |
| `merchant_application` | [`MerchantApplication`](../../doc/models/merchant-application.md) | Optional | - |
| `merchant_device` | [`MerchantDevice2`](../../doc/models/merchant-device-2.md) | Optional | - |
| `shopper_interaction_device` | [`ShopperInteractionDevice2`](../../doc/models/shopper-interaction-device-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.adyen_library import AdyenLibrary
from adyen.models.adyen_payment_source import AdyenPaymentSource
from adyen.models.application_info import ApplicationInfo
from adyen.models.external_platform_2 import ExternalPlatform2
from adyen.models.merchant_application import MerchantApplication
from adyen.models.merchant_device_2 import MerchantDevice2

application_info = ApplicationInfo(
    adyen_library=AdyenLibrary(
        name='name8',
        version='version4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    adyen_payment_source=AdyenPaymentSource(
        name='name2',
        version='version8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    external_platform=ExternalPlatform2(
        integrator='integrator0',
        name='name4',
        version='version0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_application=MerchantApplication(
        name='name2',
        version='version8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_device=MerchantDevice2(
        os='os4',
        os_version='osVersion6',
        reference='reference8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

