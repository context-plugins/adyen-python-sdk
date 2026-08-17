
# Payment Method Setup Info

## Structure

`PaymentMethodSetupInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accel` | [`AccelInfo1`](../../doc/models/accel-info-1.md) | Optional | Details to provide if `type` is **accel**. |
| `affirm` | [`AffirmInfo1`](../../doc/models/affirm-info-1.md) | Optional | Details to provide if `type` is **affirm**. |
| `afterpay_touch` | [`AfterpayTouchInfo1`](../../doc/models/afterpay-touch-info-1.md) | Optional | Details to provide if `type` is **afterpaytouch**. |
| `alipay_plus` | [`AlipayPlusInfo1`](../../doc/models/alipay-plus-info-1.md) | Optional | Details to provide if `type` is **alipay_plus**. |
| `amex` | [`AmexInfo1`](../../doc/models/amex-info-1.md) | Optional | Details to provide if `type` is **amex**.<br>For merchants operating in Australia, New Zealand & Canada, JCB and American Express are automatically requested together. |
| `apple_pay` | [`ApplePayInfo1`](../../doc/models/apple-pay-info-1.md) | Optional | Details to provide if `type` is **applepay**. |
| `bcmc` | [`BcmcInfo1`](../../doc/models/bcmc-info-1.md) | Optional | Details to provide if `type` is **bcmc** (Bancontact). |
| `business_line_id` | `str` | Optional | The unique identifier of the business line. Required if you are a [platform model](https://docs.adyen.com/platforms). |
| `carnet` | [`CarnetInfo1`](../../doc/models/carnet-info-1.md) | Optional | Details to provide if `type` is **carnet**. |
| `cartes_bancaires` | [`CartesBancairesInfo1`](../../doc/models/cartes-bancaires-info-1.md) | Optional | Details to provide if `type` is **cartebancaire**. |
| `clearpay` | [`ClearpayInfo1`](../../doc/models/clearpay-info-1.md) | Optional | Details to provide if `type` is **clearpay**. |
| `countries` | `List[str]` | Optional | The list of countries where a payment method is available. By default, all countries supported by the payment method. |
| `cup` | [`GenericPmWithTdiInfo1`](../../doc/models/generic-pm-with-tdi-info-1.md) | Optional | Details to provide if `type` is **cup** (China Union Pay). |
| `currencies` | `List[str]` | Optional | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. |
| `custom_routing_flags` | `List[str]` | Optional | The list of custom routing flags to route payment to the intended acquirer. |
| `diners` | [`DinersInfo1`](../../doc/models/diners-info-1.md) | Optional | Details to provide if `type` is **diners**.<br>For merchants operating in Japan, Diners payments are processed through the JCB network. This means that you must include [JCB-specific fields](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)#request-jcb) in this object. |
| `discover` | [`GenericPmWithTdiInfo2`](../../doc/models/generic-pm-with-tdi-info-2.md) | Optional | Details to provide if `type` is **discover**.<br>For merchants operating in Japan, request [Diners](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)#request-diners) payment method instead. Discover is automatically requested, together with Diners. |
| `eft_directdebit_ca` | [`GenericPmWithTdiInfo3`](../../doc/models/generic-pm-with-tdi-info-3.md) | Optional | Details to provide if `type` is **eft_directdebit_CA** (EFT PAD). |
| `eftpos_australia` | [`GenericPmWithTdiInfo4`](../../doc/models/generic-pm-with-tdi-info-4.md) | Optional | Details to provide if `type` is **eftpos_australia**. |
| `girocard` | [`GenericPmWithTdiInfo5`](../../doc/models/generic-pm-with-tdi-info-5.md) | Optional | Details to provide if `type` is **girocard**. |
| `givex` | [`GivexInfo1`](../../doc/models/givex-info-1.md) | Optional | Details to provide if `type` is **givex**. |
| `google_pay` | [`GooglePayInfo1`](../../doc/models/google-pay-info-1.md) | Optional | Details to provide if `type` is **googlepay**. |
| `ideal` | [`GenericPmWithTdiInfo6`](../../doc/models/generic-pm-with-tdi-info-6.md) | Optional | Details to provide if `type` is **ideal**. |
| `interac_card` | [`GenericPmWithTdiInfo7`](../../doc/models/generic-pm-with-tdi-info-7.md) | Optional | Details to provide if `type` is **interac_card**. |
| `jcb` | [`JCBInfo1`](../../doc/models/jcb-info-1.md) | Optional | Details to provide if `type` is **jcb**.<br>For merchants operating in Japan, `midNumber`, `reuseMidNumber`, and `serviceLevel` fields are required.<br>For merchants operating outside of Japan, these fields are not required.<br>For merchants operating in Australia, New Zealand & Canada, JCB and American Express are automatically requested together. |
| `klarna` | [`KlarnaInfo1`](../../doc/models/klarna-info-1.md) | Optional | Details to provide if `type` is **klarna** or its variant.<br><br>You can use the following payment method `type` values for Klarna:<br><br>* **klarna**: Klarna Pay Later<br>* **klarna_account**: Klarna Pay over time<br>* **klarna_paynow**: Klarna Pay now<br>* **klarna_b2b**: [Billie via Klarna](https://docs.adyen.com/payment-methods/klarna/billie) |
| `maestro` | [`GenericPmWithTdiInfo8`](../../doc/models/generic-pm-with-tdi-info-8.md) | Optional | Details to provide if `type` is **maestro**.<br>In the US, `maestro` is not supported; use `maestro_usa` instead. |
| `maestro_usa` | [`GenericPmWithTdiInfo9`](../../doc/models/generic-pm-with-tdi-info-9.md) | Optional | Details to provide if `type` is **maestro_usa**.<br>Only for Maestro USA, otherwise use `maestro`. |
| `mc` | [`GenericPmWithTdiInfo10`](../../doc/models/generic-pm-with-tdi-info-10.md) | Optional | Details to provide if `type` is **mc**. |
| `meal_voucher_fr` | [`MealVoucherFRInfo1`](../../doc/models/meal-voucher-fr-info-1.md) | Optional | Details to provide if `type` is **mealVoucher_FR**. |
| `nyce` | [`NyceInfo1`](../../doc/models/nyce-info-1.md) | Optional | Details to provide if `type` is **nyce**. |
| `paybybank_plaid` | [`PayByBankPlaidInfo1`](../../doc/models/pay-by-bank-plaid-info-1.md) | Optional | Details to provide if `type` is **paybybank_plaid**. |
| `payme` | [`PayMeInfo1`](../../doc/models/pay-me-info-1.md) | Optional | Details to provide if `type` is **payme**. |
| `paypal` | [`PayPalInfo1`](../../doc/models/pay-pal-info-1.md) | Optional | Details to provide if `type` is **paypal**. |
| `payto` | [`PayToInfo1`](../../doc/models/pay-to-info-1.md) | Optional | Details to provide if `type` is **payto**. |
| `pulse` | [`PulseInfo2`](../../doc/models/pulse-info-2.md) | Optional | Details to provide if `type` is **pulse**. |
| `reference` | `str` | Optional | Your reference for the payment method. Supported characters a-z, A-Z, 0-9.<br><br>**Constraints**: *Maximum Length*: `150` |
| `sepadirectdebit` | [`SepaDirectDebitInfo2`](../../doc/models/sepa-direct-debit-info-2.md) | Optional | Details to provide if `type` is **sepadirectdebit**. |
| `shopper_interaction` | [`ShopperInteraction1Enum`](../../doc/models/shopper-interaction-1-enum.md) | Optional | The sales channel. Required if:<br><br>- The merchant account does not have a sales channel.<br>- `type` is **alipay**.<br><br>When you provide this field, it overrides the default sales channel set on the merchant account.<br><br>Possible values: **eCommerce**, **pos**, **contAuth**, and **moto**. |
| `sodexo` | [`SodexoInfo2`](../../doc/models/sodexo-info-2.md) | Optional | Details to provide if `type` is **sodexo**. |
| `sofort` | [`SofortInfo2`](../../doc/models/sofort-info-2.md) | Optional | Sofort details. |
| `star` | [`StarInfo2`](../../doc/models/star-info-2.md) | Optional | Details to provide if `type` is **star**. |
| `store_ids` | `List[str]` | Optional | The unique identifier of the store for which to configure the payment method, if any. |
| `svs` | [`SvsInfo2`](../../doc/models/svs-info-2.md) | Optional | Details to provide if `type` is **svs**. |
| `swish` | [`SwishInfo2`](../../doc/models/swish-info-2.md) | Optional | Details to provide if `type` is **swish**.<br><br>- This field is required only if you have a contract with Swish. Swish handles settlement directly with you (not through Adyen).<br>- If not specified then it's assumed that you are using Adyen's contract with Swish.You don't have a direct relationship with Swish. |
| `ticket` | [`TicketInfo2`](../../doc/models/ticket-info-2.md) | Optional | Details to provide if `type` is **ticket** (Edenred Brazil). |
| `twint` | [`TwintInfo2`](../../doc/models/twint-info-2.md) | Optional | Details to provide if `type` is **twint**. |
| `mtype` | [`Type59Enum`](../../doc/models/type-59-enum.md) | Required | Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api). |
| `valuelink` | [`ValuelinkInfo2`](../../doc/models/valuelink-info-2.md) | Optional | Details to provide if `type` is **valuelink**. |
| `vipps` | [`VippsInfo2`](../../doc/models/vipps-info-2.md) | Optional | Details to provide if `type` is **vipps**. |
| `visa` | [`GenericPmWithTdiInfo11`](../../doc/models/generic-pm-with-tdi-info-11.md) | Optional | Details to provide if `type` is **visa**. |
| `wechatpay` | [`WeChatPayInfo2`](../../doc/models/we-chat-pay-info-2.md) | Optional | Details to provide if `type` is **wechatpay**. |
| `wechatpay_pos` | [`WeChatPayPosInfo2`](../../doc/models/we-chat-pay-pos-info-2.md) | Optional | Details to provide if `type` is **wechatpay_pos**. |

## Example

```python
from adyen.models.accel_info_1 import AccelInfo1
from adyen.models.affirm_info_1 import AffirmInfo1
from adyen.models.afterpay_touch_info_1 import AfterpayTouchInfo1
from adyen.models.alipay_plus_info_1 import AlipayPlusInfo1
from adyen.models.amex_info_1 import AmexInfo1
from adyen.models.payment_method_setup_info import PaymentMethodSetupInfo
from adyen.models.processing_type_enum import ProcessingTypeEnum
from adyen.models.service_level_enum import ServiceLevelEnum
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_59_enum import Type59Enum
from adyen.models.type_8_enum import Type8Enum

payment_method_setup_info = PaymentMethodSetupInfo(
    mtype=Type59Enum.VALE_REFEICAO,
    accel=AccelInfo1(
        processing_type=ProcessingTypeEnum.BILLPAY,
        transaction_description=TransactionDescriptionInfo1(
            doing_business_as_name='doingBusinessAsName0',
            mtype=Type8Enum.FIXED
        )
    ),
    affirm=AffirmInfo1(
        support_email='supportEmail2',
        price_plan='pricePlan8'
    ),
    afterpay_touch=AfterpayTouchInfo1(
        support_url='supportUrl4',
        support_email='supportEmail8'
    ),
    alipay_plus=AlipayPlusInfo1(
        settlement_currency_code='settlementCurrencyCode0'
    ),
    amex=AmexInfo1(
        service_level=ServiceLevelEnum.GATEWAYCONTRACT,
        mid_number='midNumber4',
        reuse_mid_number=False
    )
)
```

