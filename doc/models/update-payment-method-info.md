
# Update Payment Method Info

*This model accepts additional fields of type Any.*

## Structure

`UpdatePaymentMethodInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accel` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `affirm` | [`AffirmUpdateInfo`](../../doc/models/affirm-update-info.md) | Optional | - |
| `bcmc` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `carnet` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `cartes_bancaires` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `cashapp` | [`CashAppUpdateInfo`](../../doc/models/cash-app-update-info.md) | Optional | - |
| `countries` | `List[str]` | Optional | The list of countries where a payment method is available. By default, all countries supported by the payment method. |
| `cup` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `currencies` | `List[str]` | Optional | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. |
| `custom_routing_flags` | `List[str]` | Optional | Custom routing flags for acquirer routing. |
| `diners` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `discover` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `eft_directdebit_ca` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `eftpos_australia` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `enabled` | `bool` | Optional | Indicates whether the payment method is enabled (**true**) or disabled (**false**). |
| `girocard` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `ideal` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `interac_card` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `jcb` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `maestro` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `maestro_usa` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `mc` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `nyce` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `paybybank_plaid` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `pulse` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `sepadirectdebit` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `star` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `store_id` | `str` | Optional | The store for this payment method |
| `store_ids` | `List[str]` | Optional | The list of stores for this payment method |
| `visa` | [`AccelUpdateInfo`](../../doc/models/accel-update-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.accel_update_info import AccelUpdateInfo
from adyen.models.affirm_update_info import AffirmUpdateInfo
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33
from adyen.models.update_payment_method_info import UpdatePaymentMethodInfo

update_payment_method_info = UpdatePaymentMethodInfo(
    accel=AccelUpdateInfo(
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
    affirm=AffirmUpdateInfo(
        price_plan='pricePlan8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    bcmc=AccelUpdateInfo(
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
    carnet=AccelUpdateInfo(
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
    cartes_bancaires=AccelUpdateInfo(
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

