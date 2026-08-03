
# Star Info 2

Details to provide if `type` is **star**.

*This model accepts additional fields of type Any.*

## Structure

`StarInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `processing_type` | [`ProcessingType`](../../doc/models/processing-type.md) | Required | - |
| `transaction_description` | [`TransactionDescriptionInfo`](../../doc/models/transaction-description-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.processing_type import ProcessingType
from adyen.models.star_info_2 import StarInfo2
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33

star_info_2 = StarInfo2(
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
)
```

