
# Generic Pm with Tdi Update Info 11

Details to provide if `type` is **maestro**.
In the US, `maestro` is not supported; use `maestro_usa` instead.

*This model accepts additional fields of type Any.*

## Structure

`GenericPmWithTdiUpdateInfo11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_description` | [`TransactionDescriptionInfo`](../../doc/models/transaction-description-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.generic_pm_with_tdi_update_info_11 import GenericPmWithTdiUpdateInfo11
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33

generic_pm_with_tdi_update_info_11 = GenericPmWithTdiUpdateInfo11(
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
)
```

