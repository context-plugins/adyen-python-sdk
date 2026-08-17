
# Payment Amount Update Request

## Structure

`PaymentAmountUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adjust_auth_type` | [`AdjustAuthTypeEnum`](../../doc/models/adjust-auth-type-enum.md) | Optional | The type of adjustment. Possible values:<br><br>* **cardholderInitiatedTransaction**<br><br>* **merchantInitiatedTransaction** |
| `adjust_authorisation_data` | `str` | Optional | The required data to make a [synchronous authorization adjustment](https://docs.adyen.com/online-payments/adjust-authorisation). Pass the corresponding value from the `/payments` response or webhook message. |
| `amount` | [`Amount29`](../../doc/models/amount-29.md) | Required | The updated amount. The `currency` must match the currency used in authorisation. |
| `application_info` | [`ApplicationInfo`](../../doc/models/application-info.md) | Optional | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). |
| `industry_usage` | [`IndustryUsage1Enum`](../../doc/models/industry-usage-1-enum.md) | Optional | The reason for the amount update. Possible values:<br><br>* **delayedCharge**<br>* **noShow**<br>* **installment** |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).<br><br>> This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `mpi_data` | [`ThreeDSecureData3`](../../doc/models/three-d-secure-data-3.md) | Optional | Authentication data from a [merchant plug-in (MPI)](https://en.wikipedia.org/wiki/Merchant_plug-in) like Mastercard SecureCode, Visa Secure, or Cartes Bancaires. Required for cardholder-initiated transaction (CIT) adjustments. |
| `reference` | `str` | Optional | Your reference for the amount update request. Maximum length: 80 characters. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/process-payments) or [platforms](https://docs.adyen.com/platforms/process-payments). |

## Example

```python
from adyen.models.adjust_auth_type_enum import AdjustAuthTypeEnum
from adyen.models.amount_29 import Amount29
from adyen.models.application_info import ApplicationInfo
from adyen.models.common_field_1 import CommonField1
from adyen.models.common_field_2 import CommonField2
from adyen.models.common_field_4 import CommonField4
from adyen.models.external_platform import ExternalPlatform
from adyen.models.industry_usage_1_enum import IndustryUsage1Enum
from adyen.models.line_item import LineItem
from adyen.models.merchant_device import MerchantDevice
from adyen.models.payment_amount_update_request import PaymentAmountUpdateRequest

payment_amount_update_request = PaymentAmountUpdateRequest(
    amount=Amount29(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount8',
    adjust_auth_type=AdjustAuthTypeEnum.CARDHOLDERINITIATEDTRANSACTION,
    adjust_authorisation_data='adjustAuthorisationData4',
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
    industry_usage=IndustryUsage1Enum.DELAYEDCHARGE,
    line_items=[
        LineItem(
            amount_excluding_tax=38,
            amount_including_tax=148,
            brand='brand6',
            color='color6',
            description='description2'
        )
    ]
)
```

