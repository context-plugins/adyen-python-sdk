
# Nyce Update Info 1

Details to provide if `type` is **nyce**.

*This model accepts additional fields of type Any.*

## Structure

`NyceUpdateInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_description` | [`TransactionDescriptionInfo`](../../doc/models/transaction-description-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.nyce_update_info_1 import NyceUpdateInfo1
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33

nyce_update_info_1 = NyceUpdateInfo1(
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

