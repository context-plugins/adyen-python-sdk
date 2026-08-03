
# Payment Cancel Request

*This model accepts additional fields of type Any.*

## Structure

`PaymentCancelRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `application_info` | [`ApplicationInfo1`](../../doc/models/application-info-1.md) | Optional | - |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `reference` | `str` | Optional | Your reference for the cancel request. Maximum length: 80 characters. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.adyen_library import AdyenLibrary
from adyen.models.adyen_payment_source import AdyenPaymentSource
from adyen.models.application_info_1 import ApplicationInfo1
from adyen.models.external_platform_2 import ExternalPlatform2
from adyen.models.merchant_application import MerchantApplication
from adyen.models.merchant_device_2 import MerchantDevice2
from adyen.models.payment_cancel_request import PaymentCancelRequest

payment_cancel_request = PaymentCancelRequest(
    merchant_account='merchantAccount0',
    application_info=ApplicationInfo1(
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
    ),
    reference='reference6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

