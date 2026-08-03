
# Maestro Response Info 1

**maestro** details

*This model accepts additional fields of type Any.*

## Structure

`MaestroResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_description` | [`TransactionDescriptionInfo`](../../doc/models/transaction-description-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.maestro_response_info_1 import MaestroResponseInfo1
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33

maestro_response_info_1 = MaestroResponseInfo1(
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

