
# Payment Method Setup Info

*This model accepts additional fields of type Any.*

## Structure

`PaymentMethodSetupInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accel` | [`AccelInfo`](../../doc/models/accel-info.md) | Optional | - |
| `affirm` | [`AffirmInfo`](../../doc/models/affirm-info.md) | Optional | - |
| `afterpay_touch` | [`AfterpayTouchInfo`](../../doc/models/afterpay-touch-info.md) | Optional | - |
| `alipay_plus` | [`AlipayPlusInfo`](../../doc/models/alipay-plus-info.md) | Optional | - |
| `amex` | [`AmexInfo`](../../doc/models/amex-info.md) | Optional | - |
| `apple_pay` | [`ApplePayInfo`](../../doc/models/apple-pay-info.md) | Optional | - |
| `bcmc` | [`BcmcInfo`](../../doc/models/bcmc-info.md) | Optional | - |
| `business_line_id` | `str` | Optional | The unique identifier of the business line. Required if you are a [platform model](https://docs.adyen.com/platforms). |
| `carnet` | [`CarnetInfo`](../../doc/models/carnet-info.md) | Optional | - |
| `cartes_bancaires` | [`CartesBancairesInfo`](../../doc/models/cartes-bancaires-info.md) | Optional | - |
| `clearpay` | [`ClearpayInfo`](../../doc/models/clearpay-info.md) | Optional | - |
| `countries` | `List[str]` | Optional | The list of countries where a payment method is available. By default, all countries supported by the payment method. |
| `cup` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `currencies` | `List[str]` | Optional | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. |
| `custom_routing_flags` | `List[str]` | Optional | The list of custom routing flags to route payment to the intended acquirer. |
| `diners` | [`DinersInfo`](../../doc/models/diners-info.md) | Optional | - |
| `discover` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `eft_directdebit_ca` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `eftpos_australia` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `girocard` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `givex` | [`GivexInfo`](../../doc/models/givex-info.md) | Optional | - |
| `google_pay` | [`GooglePayInfo`](../../doc/models/google-pay-info.md) | Optional | - |
| `ideal` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `interac_card` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `jcb` | [`JcbInfo`](../../doc/models/jcb-info.md) | Optional | - |
| `klarna` | [`KlarnaInfo`](../../doc/models/klarna-info.md) | Optional | - |
| `maestro` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `maestro_usa` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `mc` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `meal_voucher_fr` | [`MealVoucherFrInfo`](../../doc/models/meal-voucher-fr-info.md) | Optional | - |
| `nyce` | [`AccelInfo`](../../doc/models/accel-info.md) | Optional | - |
| `paybybank_plaid` | [`PayByBankPlaidInfo`](../../doc/models/pay-by-bank-plaid-info.md) | Optional | - |
| `payme` | [`PayMeInfo`](../../doc/models/pay-me-info.md) | Optional | - |
| `paypal` | [`PayPalInfo`](../../doc/models/pay-pal-info.md) | Optional | - |
| `payto` | [`PayToInfo`](../../doc/models/pay-to-info.md) | Optional | - |
| `pulse` | [`AccelInfo`](../../doc/models/accel-info.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the payment method. Supported characters a-z, A-Z, 0-9.<br><br>**Constraints**: *Maximum Length*: `150` |
| `sepadirectdebit` | [`SepaDirectDebitInfo`](../../doc/models/sepa-direct-debit-info.md) | Optional | - |
| `shopper_interaction` | [`ShopperInteraction2`](../../doc/models/shopper-interaction-2.md) | Optional | - |
| `sodexo` | [`SodexoInfo`](../../doc/models/sodexo-info.md) | Optional | - |
| `sofort` | [`SofortInfo`](../../doc/models/sofort-info.md) | Optional | - |
| `star` | [`AccelInfo`](../../doc/models/accel-info.md) | Optional | - |
| `store_ids` | `List[str]` | Optional | The unique identifier of the store for which to configure the payment method, if any. |
| `svs` | [`SvsInfo`](../../doc/models/svs-info.md) | Optional | - |
| `swish` | [`SwishInfo`](../../doc/models/swish-info.md) | Optional | - |
| `ticket` | [`TicketInfo`](../../doc/models/ticket-info.md) | Optional | - |
| `twint` | [`TwintInfo`](../../doc/models/twint-info.md) | Optional | - |
| `mtype` | [`Type510`](../../doc/models/type-510.md) | Required | - |
| `valuelink` | [`ValuelinkInfo`](../../doc/models/valuelink-info.md) | Optional | - |
| `vipps` | [`VippsInfo`](../../doc/models/vipps-info.md) | Optional | - |
| `visa` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `wechatpay` | [`WeChatPayInfo`](../../doc/models/we-chat-pay-info.md) | Optional | - |
| `wechatpay_pos` | [`WeChatPayInfo`](../../doc/models/we-chat-pay-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.accel_info import AccelInfo
from adyen.models.affirm_info import AffirmInfo
from adyen.models.afterpay_touch_info import AfterpayTouchInfo
from adyen.models.alipay_plus_info import AlipayPlusInfo
from adyen.models.amex_info import AmexInfo
from adyen.models.payment_method_setup_info import PaymentMethodSetupInfo
from adyen.models.processing_type import ProcessingType
from adyen.models.service_level import ServiceLevel
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33
from adyen.models.type_510 import Type510

payment_method_setup_info = PaymentMethodSetupInfo(
    mtype=Type510.VALE_REFEICAO,
    accel=AccelInfo(
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
    affirm=AffirmInfo(
        support_email='supportEmail2',
        price_plan='pricePlan8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    afterpay_touch=AfterpayTouchInfo(
        support_url='supportUrl4',
        support_email='supportEmail8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    alipay_plus=AlipayPlusInfo(
        settlement_currency_code='settlementCurrencyCode0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    amex=AmexInfo(
        service_level=ServiceLevel.GATEWAYCONTRACT,
        mid_number='midNumber4',
        reuse_mid_number=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

