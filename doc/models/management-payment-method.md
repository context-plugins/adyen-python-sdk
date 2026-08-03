
# Management Payment Method

*This model accepts additional fields of type Any.*

## Structure

`ManagementPaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accel` | [`AccelResponseInfo`](../../doc/models/accel-response-info.md) | Optional | - |
| `affirm` | [`AffirmResponseInfo`](../../doc/models/affirm-response-info.md) | Optional | - |
| `afterpay_touch` | [`AfterpayTouchResponseInfo`](../../doc/models/afterpay-touch-response-info.md) | Optional | - |
| `alipay_plus` | [`AlipayPlusResponseInfo`](../../doc/models/alipay-plus-response-info.md) | Optional | - |
| `allowed` | `bool` | Optional | Indicates whether receiving payments is allowed. This value is set to **true** by Adyen after screening your merchant account. |
| `amex` | [`AmexResponseInfo`](../../doc/models/amex-response-info.md) | Optional | - |
| `apple_pay` | [`ApplePayResponseInfo`](../../doc/models/apple-pay-response-info.md) | Optional | - |
| `associated_payment_methods` | [`List[AssociatedPaymentMethod]`](../../doc/models/associated-payment-method.md) | Optional | Payment methods that were also updated as part of an associated transition. |
| `bcmc` | [`BcmcResponseInfo`](../../doc/models/bcmc-response-info.md) | Optional | - |
| `business_line_id` | `str` | Optional | The unique identifier of the business line. Required if you are a [platform model](https://docs.adyen.com/platforms). |
| `carnet` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `cartes_bancaires` | [`CartesBancairesResponseInfo`](../../doc/models/cartes-bancaires-response-info.md) | Optional | - |
| `clearpay` | [`ClearpayResponseInfo`](../../doc/models/clearpay-response-info.md) | Optional | - |
| `countries` | `List[str]` | Optional | The list of countries where a payment method is available. By default, all countries supported by the payment method. |
| `cup` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `currencies` | `List[str]` | Optional | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. |
| `custom_routing_flags` | `List[str]` | Optional | The list of custom routing flags to route payment to the intended acquirer. |
| `diners` | [`DinersResponseInfo`](../../doc/models/diners-response-info.md) | Optional | - |
| `discover` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `eft_directdebit_ca` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `eftpos_australia` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `enabled` | `bool` | Optional | Indicates whether the payment method is enabled (**true**) or disabled (**false**). |
| `girocard` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `givex` | [`GivexResponseInfo`](../../doc/models/givex-response-info.md) | Optional | - |
| `google_pay` | [`GooglePayResponseInfo`](../../doc/models/google-pay-response-info.md) | Optional | - |
| `id` | `str` | Required | The identifier of the resource. |
| `ideal` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `interac_card` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `jcb` | [`JcbResponseInfo`](../../doc/models/jcb-response-info.md) | Optional | - |
| `klarna` | [`KlarnaResponseInfo`](../../doc/models/klarna-response-info.md) | Optional | - |
| `maestro` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `maestro_usa` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `mc` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `meal_voucher_fr` | [`MealVoucherFrResponseInfo`](../../doc/models/meal-voucher-fr-response-info.md) | Optional | - |
| `nyce` | [`AccelResponseInfo`](../../doc/models/accel-response-info.md) | Optional | - |
| `paybybank_plaid` | [`PayByBankPlaidResponseInfo`](../../doc/models/pay-by-bank-plaid-response-info.md) | Optional | - |
| `payme` | [`PayMeResponseInfo`](../../doc/models/pay-me-response-info.md) | Optional | - |
| `paypal` | [`PayPalResponseInfo`](../../doc/models/pay-pal-response-info.md) | Optional | - |
| `payto` | [`PayToResponseInfo`](../../doc/models/pay-to-response-info.md) | Optional | - |
| `pulse` | [`AccelResponseInfo`](../../doc/models/accel-response-info.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the payment method. Supported characters a-z, A-Z, 0-9.<br><br>**Constraints**: *Maximum Length*: `150` |
| `sepadirectdebit` | [`SepaDirectDebitInfo`](../../doc/models/sepa-direct-debit-info.md) | Optional | - |
| `shopper_interaction` | `str` | Optional | The sales channel. |
| `sodexo` | [`SodexoResponseInfo`](../../doc/models/sodexo-response-info.md) | Optional | - |
| `sofort` | [`SofortResponseInfo`](../../doc/models/sofort-response-info.md) | Optional | - |
| `star` | [`AccelResponseInfo`](../../doc/models/accel-response-info.md) | Optional | - |
| `store_ids` | `List[str]` | Optional | The unique identifier of the store for which to configure the payment method, if any. |
| `svs` | [`SvsResponseInfo`](../../doc/models/svs-response-info.md) | Optional | - |
| `swish` | [`SwishResponseInfo`](../../doc/models/swish-response-info.md) | Optional | - |
| `ticket` | [`TicketInfo`](../../doc/models/ticket-info.md) | Optional | - |
| `twint` | [`TwintResponseInfo`](../../doc/models/twint-response-info.md) | Optional | - |
| `mtype` | `str` | Optional | Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api). |
| `valuelink` | [`ValuelinkResponseInfo`](../../doc/models/valuelink-response-info.md) | Optional | - |
| `verification_status` | [`VerificationStatus`](../../doc/models/verification-status.md) | Optional | - |
| `vipps` | [`VippsResponseInfo`](../../doc/models/vipps-response-info.md) | Optional | - |
| `visa` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `wechatpay` | [`WeChatPayPosResponseInfo`](../../doc/models/we-chat-pay-pos-response-info.md) | Optional | - |
| `wechatpay_pos` | [`WeChatPayPosResponseInfo`](../../doc/models/we-chat-pay-pos-response-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.accel_response_info import AccelResponseInfo
from adyen.models.affirm_response_info import AffirmResponseInfo
from adyen.models.afterpay_touch_response_info import AfterpayTouchResponseInfo
from adyen.models.alipay_plus_response_info import AlipayPlusResponseInfo
from adyen.models.management_payment_method import ManagementPaymentMethod
from adyen.models.processing_type import ProcessingType
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33

management_payment_method = ManagementPaymentMethod(
    id='id0',
    accel=AccelResponseInfo(
        processing_type=ProcessingType.BILLPAY,
        transaction_description=TransactionDescriptionInfo(
            doing_business_as_name='doingBusinessAsName0',
            mtype=Type33.FIXED,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    affirm=AffirmResponseInfo(
        public_api_key='publicApiKey4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    afterpay_touch=AfterpayTouchResponseInfo(
        support_email='supportEmail8',
        support_url='supportUrl4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    alipay_plus=AlipayPlusResponseInfo(
        settlement_currency_code='settlementCurrencyCode0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    allowed=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

