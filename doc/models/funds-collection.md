
# Funds Collection

*This model accepts additional fields of type Any.*

## Structure

`FundsCollection`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_identification` | [`BankAccountIdentification1`](../../doc/models/bank-account-identification-1.md) | Optional | - |
| `funds_collection_type` | [`FundsCollectionType2`](../../doc/models/funds-collection-type-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_account_identification_1 import BankAccountIdentification1
from adyen.models.funds_collection import FundsCollection
from adyen.models.funds_collection_type_2 import FundsCollectionType2

funds_collection = FundsCollection(
    account_identification=BankAccountIdentification1(
        mtype='BankAccountIdentification1',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    funds_collection_type=FundsCollectionType2.UNSCHEDULEDREPAYMENT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

