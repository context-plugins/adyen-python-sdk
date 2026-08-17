
# Standalone Payment Cancel Request

## Structure

`StandalonePaymentCancelRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `application_info` | [`ApplicationInfo`](../../doc/models/application-info.md) | Optional | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `payment_reference` | `str` | Required | The [`reference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_reference) of the payment that you want to cancel. |
| `reference` | `str` | Optional | Your reference for the cancel request. Maximum length: 80 characters. |

## Example

```python
from adyen.models.application_info import ApplicationInfo
from adyen.models.common_field_1 import CommonField1
from adyen.models.common_field_2 import CommonField2
from adyen.models.common_field_4 import CommonField4
from adyen.models.external_platform import ExternalPlatform
from adyen.models.merchant_device import MerchantDevice
from adyen.models.standalone_payment_cancel_request import StandalonePaymentCancelRequest

standalone_payment_cancel_request = StandalonePaymentCancelRequest(
    merchant_account='merchantAccount6',
    payment_reference='paymentReference4',
    application_info=ApplicationInfo(
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
    ),
    reference='reference0'
)
```

