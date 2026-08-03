
# Payment Amount Update Request

*This model accepts additional fields of type Any.*

## Structure

`PaymentAmountUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adjust_auth_type` | [`AdjustAuthType`](../../doc/models/adjust-auth-type.md) | Optional | - |
| `adjust_authorisation_data` | `str` | Optional | The required data to make a [synchronous authorization adjustment](https://docs.adyen.com/online-payments/adjust-authorisation). Pass the corresponding value from the `/payments` response or webhook message. |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `application_info` | [`ApplicationInfo1`](../../doc/models/application-info-1.md) | Optional | - |
| `industry_usage` | [`IndustryUsage1`](../../doc/models/industry-usage-1.md) | Optional | - |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).<br><br>> This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `mpi_data` | [`MpiData`](../../doc/models/mpi-data.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the amount update request. Maximum length: 80 characters. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/process-payments) or [platforms](https://docs.adyen.com/platforms/process-payments). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.adjust_auth_type import AdjustAuthType
from adyen.models.adyen_library import AdyenLibrary
from adyen.models.adyen_payment_source import AdyenPaymentSource
from adyen.models.amount_16 import Amount16
from adyen.models.application_info_1 import ApplicationInfo1
from adyen.models.external_platform_2 import ExternalPlatform2
from adyen.models.industry_usage_1 import IndustryUsage1
from adyen.models.line_item import LineItem
from adyen.models.merchant_application import MerchantApplication
from adyen.models.merchant_device_2 import MerchantDevice2
from adyen.models.payment_amount_update_request import PaymentAmountUpdateRequest

payment_amount_update_request = PaymentAmountUpdateRequest(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_account='merchantAccount8',
    adjust_auth_type=AdjustAuthType.CARDHOLDERINITIATEDTRANSACTION,
    adjust_authorisation_data='adjustAuthorisationData4',
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
    industry_usage=IndustryUsage1.DELAYEDCHARGE,
    line_items=[
        LineItem(
            amount_excluding_tax=38,
            amount_including_tax=148,
            brand='brand6',
            color='color6',
            description='description2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

