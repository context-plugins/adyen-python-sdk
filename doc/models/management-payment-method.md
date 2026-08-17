
# Management Payment Method

## Structure

`ManagementPaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accel` | [`AccelResponseInfo1`](../../doc/models/accel-response-info-1.md) | Optional | **accel** details |
| `affirm` | [`AffirmResponseInfo1`](../../doc/models/affirm-response-info-1.md) | Optional | *affirm** details |
| `afterpay_touch` | [`AfterpayTouchResponseInfo1`](../../doc/models/afterpay-touch-response-info-1.md) | Optional | **afterpaytouch** details |
| `alipay_plus` | [`AlipayPlusResponseInfo1`](../../doc/models/alipay-plus-response-info-1.md) | Optional | **alipay_plus** details |
| `allowed` | `bool` | Optional | Indicates whether receiving payments is allowed. This value is set to **true** by Adyen after screening your merchant account. |
| `amex` | [`AmexResponseInfo1`](../../doc/models/amex-response-info-1.md) | Optional | **amex** details |
| `apple_pay` | [`ApplePayResponseInfo1`](../../doc/models/apple-pay-response-info-1.md) | Optional | **applepay** details |
| `associated_payment_methods` | [`List[AssociatedPaymentMethod]`](../../doc/models/associated-payment-method.md) | Optional | Payment methods that were also updated as part of an associated transition. |
| `bcmc` | [`BcmcResponseInfo1`](../../doc/models/bcmc-response-info-1.md) | Optional | **bcmc** (Bancontact) details |
| `business_line_id` | `str` | Optional | The unique identifier of the business line. Required if you are a [platform model](https://docs.adyen.com/platforms). |
| `carnet` | [`CarnetResponseInfo1`](../../doc/models/carnet-response-info-1.md) | Optional | **carnet** details |
| `cartes_bancaires` | [`CartesBancairesResponseInfo1`](../../doc/models/cartes-bancaires-response-info-1.md) | Optional | **cartesbancaire** details |
| `clearpay` | [`ClearpayResponseInfo1`](../../doc/models/clearpay-response-info-1.md) | Optional | **clearpay** details |
| `countries` | `List[str]` | Optional | The list of countries where a payment method is available. By default, all countries supported by the payment method. |
| `cup` | [`CupResponseInfo1`](../../doc/models/cup-response-info-1.md) | Optional | **cup** (China Union Pay) details |
| `currencies` | `List[str]` | Optional | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. |
| `custom_routing_flags` | `List[str]` | Optional | The list of custom routing flags to route payment to the intended acquirer. |
| `diners` | [`DinersResponseInfo1`](../../doc/models/diners-response-info-1.md) | Optional | **diners** details |
| `discover` | [`DiscoverResponseInfo1`](../../doc/models/discover-response-info-1.md) | Optional | **discover**. details |
| `eft_directdebit_ca` | [`EFTDirectDebitCAResponseInfo1`](../../doc/models/eft-direct-debit-ca-response-info-1.md) | Optional | **eft_directdebit_CA** (EFT PAD) details |
| `eftpos_australia` | [`EftPosAustraliaResponseInfo1`](../../doc/models/eft-pos-australia-response-info-1.md) | Optional | **eftpos_australia** details |
| `enabled` | `bool` | Optional | Indicates whether the payment method is enabled (**true**) or disabled (**false**). |
| `girocard` | [`GirocardResponseInfo1`](../../doc/models/girocard-response-info-1.md) | Optional | **girocard** details |
| `givex` | [`GivexResponseInfo1`](../../doc/models/givex-response-info-1.md) | Optional | **givex** details |
| `google_pay` | [`GooglePayResponseInfo1`](../../doc/models/google-pay-response-info-1.md) | Optional | **googlepay** details |
| `id` | `str` | Required | The identifier of the resource. |
| `ideal` | [`IdealResponseInfo1`](../../doc/models/ideal-response-info-1.md) | Optional | **ideal** details |
| `interac_card` | [`InteracCardResponseInfo1`](../../doc/models/interac-card-response-info-1.md) | Optional | **interac_card** details |
| `jcb` | [`JCBResponseInfo1`](../../doc/models/jcb-response-info-1.md) | Optional | **jcb** details |
| `klarna` | [`KlarnaResponseInfo1`](../../doc/models/klarna-response-info-1.md) | Optional | **klarna** or its variant details |
| `maestro` | [`MaestroResponseInfo1`](../../doc/models/maestro-response-info-1.md) | Optional | **maestro** details |
| `maestro_usa` | [`MaestroUSAResponseInfo1`](../../doc/models/maestro-usa-response-info-1.md) | Optional | Details to provide if `type` is **maestro_usa** details |
| `mc` | [`MCResponseInfo1`](../../doc/models/mc-response-info-1.md) | Optional | **mc** details |
| `meal_voucher_fr` | [`MealVoucherFRResponseInfo1`](../../doc/models/meal-voucher-fr-response-info-1.md) | Optional | **mealVoucher_FR** details |
| `nyce` | [`NyceResponseInfo1`](../../doc/models/nyce-response-info-1.md) | Optional | **nyce** details |
| `paybybank_plaid` | [`PayByBankPlaidResponseInfo1`](../../doc/models/pay-by-bank-plaid-response-info-1.md) | Optional | **paybybank_plaid** details |
| `payme` | [`PayMeResponseInfo1`](../../doc/models/pay-me-response-info-1.md) | Optional | **payme** details |
| `paypal` | [`PayPalResponseInfo1`](../../doc/models/pay-pal-response-info-1.md) | Optional | **paypal** details |
| `payto` | [`PayToResponseInfo1`](../../doc/models/pay-to-response-info-1.md) | Optional | **payto** details |
| `pulse` | [`PulseResponseInfo2`](../../doc/models/pulse-response-info-2.md) | Optional | **pulse** details |
| `reference` | `str` | Optional | Your reference for the payment method. Supported characters a-z, A-Z, 0-9.<br><br>**Constraints**: *Maximum Length*: `150` |
| `sepadirectdebit` | [`SepaDirectDebitResponseInfo2`](../../doc/models/sepa-direct-debit-response-info-2.md) | Optional | **sepadirectdebit** details |
| `shopper_interaction` | `str` | Optional | The sales channel. |
| `sodexo` | [`SodexoResponseInfo2`](../../doc/models/sodexo-response-info-2.md) | Optional | **sodexo** details |
| `sofort` | [`SofortResponseInfo2`](../../doc/models/sofort-response-info-2.md) | Optional | Sofort details. |
| `star` | [`StarResponseInfo2`](../../doc/models/star-response-info-2.md) | Optional | **star** details |
| `store_ids` | `List[str]` | Optional | The unique identifier of the store for which to configure the payment method, if any. |
| `svs` | [`SvsResponseInfo2`](../../doc/models/svs-response-info-2.md) | Optional | **svs** details |
| `swish` | [`SwishResponseInfo2`](../../doc/models/swish-response-info-2.md) | Optional | **swish** or its variant details |
| `ticket` | [`TicketResponseInfo2`](../../doc/models/ticket-response-info-2.md) | Optional | **ticket** (Edenred Brazil) details |
| `twint` | [`TwintResponseInfo2`](../../doc/models/twint-response-info-2.md) | Optional | **twint** details |
| `mtype` | `str` | Optional | Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api). |
| `valuelink` | [`ValuelinkResponseInfo2`](../../doc/models/valuelink-response-info-2.md) | Optional | **valuelink** details |
| `verification_status` | [`VerificationStatusEnum`](../../doc/models/verification-status-enum.md) | Optional | Payment method status. Possible values:<br><br>* **valid**<br>* **pending**<br>* **invalid**<br>* **rejected** |
| `vipps` | [`VippsResponseInfo2`](../../doc/models/vipps-response-info-2.md) | Optional | **vipps** details |
| `visa` | [`VisaResponseInfo2`](../../doc/models/visa-response-info-2.md) | Optional | **visa** details |
| `wechatpay` | [`WeChatPayResponseInfo2`](../../doc/models/we-chat-pay-response-info-2.md) | Optional | **wechatpay** details |
| `wechatpay_pos` | [`WeChatPayPosResponseInfo2`](../../doc/models/we-chat-pay-pos-response-info-2.md) | Optional | **wechatpay_pos** details |

## Example

```python
from adyen.models.accel_response_info_1 import AccelResponseInfo1
from adyen.models.affirm_response_info_1 import AffirmResponseInfo1
from adyen.models.afterpay_touch_response_info_1 import AfterpayTouchResponseInfo1
from adyen.models.alipay_plus_response_info_1 import AlipayPlusResponseInfo1
from adyen.models.management_payment_method import ManagementPaymentMethod
from adyen.models.processing_type_enum import ProcessingTypeEnum
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum

management_payment_method = ManagementPaymentMethod(
    id='id0',
    accel=AccelResponseInfo1(
        processing_type=ProcessingTypeEnum.BILLPAY,
        transaction_description=TransactionDescriptionResponseInfo1(
            doing_business_as_name='doingBusinessAsName0',
            mtype=Type8Enum.FIXED
        )
    ),
    affirm=AffirmResponseInfo1(
        public_api_key='publicApiKey4'
    ),
    afterpay_touch=AfterpayTouchResponseInfo1(
        support_email='supportEmail8',
        support_url='supportUrl4'
    ),
    alipay_plus=AlipayPlusResponseInfo1(
        settlement_currency_code='settlementCurrencyCode0'
    ),
    allowed=False
)
```

