
# Update Payment Method Info

## Structure

`UpdatePaymentMethodInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accel` | [`AccelUpdateInfo1`](../../doc/models/accel-update-info-1.md) | Optional | Details to provide if `type` is **accel**. |
| `affirm` | [`AffirmUpdateInfo1`](../../doc/models/affirm-update-info-1.md) | Optional | Details to provide if `type` is **affirm**. |
| `bcmc` | [`BcmcUpdateInfo1`](../../doc/models/bcmc-update-info-1.md) | Optional | Details to provide if `type` is **bcmc** (Bancontact). |
| `carnet` | [`GenericPmWithTdiUpdateInfo1`](../../doc/models/generic-pm-with-tdi-update-info-1.md) | Optional | Details to provide if `type` is **carnet**. |
| `cartes_bancaires` | [`CartesBancairesUpdateInfo1`](../../doc/models/cartes-bancaires-update-info-1.md) | Optional | Details to provide if `type` is **cartebancaire**. |
| `cashapp` | [`CashAppUpdateInfo1`](../../doc/models/cash-app-update-info-1.md) | Optional | Details to provide if `type` is **cashapp**. |
| `countries` | `List[str]` | Optional | The list of countries where a payment method is available. By default, all countries supported by the payment method. |
| `cup` | [`GenericPmWithTdiUpdateInfo2`](../../doc/models/generic-pm-with-tdi-update-info-2.md) | Optional | Details to provide if `type` is **cup** (China Union Pay). |
| `currencies` | `List[str]` | Optional | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. |
| `custom_routing_flags` | `List[str]` | Optional | Custom routing flags for acquirer routing. |
| `diners` | [`GenericPmWithTdiUpdateInfo3`](../../doc/models/generic-pm-with-tdi-update-info-3.md) | Optional | Details to provide if `type` is **diners**.<br>For merchants operating in Japan, Diners payments are processed through the JCB network. This means that you must include [JCB-specific fields](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)#request-jcb) in this object. |
| `discover` | [`GenericPmWithTdiUpdateInfo4`](../../doc/models/generic-pm-with-tdi-update-info-4.md) | Optional | Details to provide if `type` is **discover**.<br>For merchants operating in Japan, request [Diners](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)#request-diners) payment method instead. Discover is automatically requested, together with Diners. |
| `eft_directdebit_ca` | [`GenericPmWithTdiUpdateInfo5`](../../doc/models/generic-pm-with-tdi-update-info-5.md) | Optional | Details to provide if `type` is **eft_directdebit_CA** (EFT PAD). |
| `eftpos_australia` | [`GenericPmWithTdiUpdateInfo6`](../../doc/models/generic-pm-with-tdi-update-info-6.md) | Optional | Details to provide if `type` is **eftpos_australia**. |
| `enabled` | `bool` | Optional | Indicates whether the payment method is enabled (**true**) or disabled (**false**). |
| `girocard` | [`GenericPmWithTdiUpdateInfo7`](../../doc/models/generic-pm-with-tdi-update-info-7.md) | Optional | Details to provide if `type` is **girocard**. |
| `ideal` | [`GenericPmWithTdiUpdateInfo8`](../../doc/models/generic-pm-with-tdi-update-info-8.md) | Optional | Details to provide if `type` is **ideal**. |
| `interac_card` | [`GenericPmWithTdiUpdateInfo9`](../../doc/models/generic-pm-with-tdi-update-info-9.md) | Optional | Details to provide if `type` is **interac_card**. |
| `jcb` | [`GenericPmWithTdiUpdateInfo10`](../../doc/models/generic-pm-with-tdi-update-info-10.md) | Optional | Details to provide if `type` is **jcb**.<br>For merchants operating in Japan, `midNumber`, `reuseMidNumber`, and `serviceLevel` fields are required.<br>For merchants operating outside of Japan, these fields are not required. |
| `maestro` | [`GenericPmWithTdiUpdateInfo11`](../../doc/models/generic-pm-with-tdi-update-info-11.md) | Optional | Details to provide if `type` is **maestro**.<br>In the US, `maestro` is not supported; use `maestro_usa` instead. |
| `maestro_usa` | [`GenericPmWithTdiUpdateInfo12`](../../doc/models/generic-pm-with-tdi-update-info-12.md) | Optional | Details to provide if `type` is **maestro_usa**.<br>Only for Maestro USA, otherwise use `maestro`. |
| `mc` | [`GenericPmWithTdiUpdateInfo13`](../../doc/models/generic-pm-with-tdi-update-info-13.md) | Optional | Details to provide if `type` is **mc**. |
| `nyce` | [`NyceUpdateInfo1`](../../doc/models/nyce-update-info-1.md) | Optional | Details to provide if `type` is **nyce**. |
| `paybybank_plaid` | [`PayByBankPlaidUpdateInfo1`](../../doc/models/pay-by-bank-plaid-update-info-1.md) | Optional | Details to provide if `type` is **paybybank_plaid**. |
| `pulse` | [`PulseUpdateInfo1`](../../doc/models/pulse-update-info-1.md) | Optional | Details to provide if `type` is **pulse**. |
| `sepadirectdebit` | [`SepaDirectDebitUpdateInfo1`](../../doc/models/sepa-direct-debit-update-info-1.md) | Optional | Details to provide if `type` is **sepadirectdebit**. |
| `star` | [`StarUpdateInfo1`](../../doc/models/star-update-info-1.md) | Optional | Details to provide if `type` is **star**. |
| `store_id` | `str` | Optional | The store for this payment method |
| `store_ids` | `List[str]` | Optional | The list of stores for this payment method |
| `visa` | [`GenericPmWithTdiUpdateInfo14`](../../doc/models/generic-pm-with-tdi-update-info-14.md) | Optional | Details to provide if `type` is **visa**. |

## Example

```python
from adyen.models.accel_update_info_1 import AccelUpdateInfo1
from adyen.models.affirm_update_info_1 import AffirmUpdateInfo1
from adyen.models.bcmc_update_info_1 import BcmcUpdateInfo1
from adyen.models.cartes_bancaires_update_info_1 import CartesBancairesUpdateInfo1
from adyen.models.generic_pm_with_tdi_update_info_1 import GenericPmWithTdiUpdateInfo1
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum
from adyen.models.update_payment_method_info import UpdatePaymentMethodInfo

update_payment_method_info = UpdatePaymentMethodInfo(
    accel=AccelUpdateInfo1(
        transaction_description=TransactionDescriptionInfo1(
            doing_business_as_name='doingBusinessAsName0',
            mtype=Type8Enum.FIXED
        )
    ),
    affirm=AffirmUpdateInfo1(
        price_plan='pricePlan8'
    ),
    bcmc=BcmcUpdateInfo1(
        transaction_description=TransactionDescriptionInfo1(
            doing_business_as_name='doingBusinessAsName0',
            mtype=Type8Enum.FIXED
        )
    ),
    carnet=GenericPmWithTdiUpdateInfo1(
        transaction_description=TransactionDescriptionInfo1(
            doing_business_as_name='doingBusinessAsName0',
            mtype=Type8Enum.FIXED
        )
    ),
    cartes_bancaires=CartesBancairesUpdateInfo1(
        transaction_description=TransactionDescriptionInfo1(
            doing_business_as_name='doingBusinessAsName0',
            mtype=Type8Enum.FIXED
        )
    )
)
```

