
# Stored Value Account Status 1

Data related to the result of the stored value card transaction.

*This model accepts additional fields of type Any.*

## Structure

`StoredValueAccountStatus1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stored_value_account_id` | [`StoredValueAccountId2`](../../doc/models/stored-value-account-id-2.md) | Required | - |
| `current_balance` | `float` | Optional | If relevant and known.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.entry_mode import EntryMode
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_status_1 import StoredValueAccountStatus1
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1

stored_value_account_status_1 = StoredValueAccountStatus1(
    stored_value_account_id=StoredValueAccountId2(
        stored_value_account_type=StoredValueAccountType1.PHONECARD,
        entry_mode=[
            EntryMode.MAGSTRIPE,
            EntryMode.SCANNED
        ],
        identification_type=IdentificationType11.PHONENUMBER,
        stored_value_id='StoredValueID8',
        stored_value_provider='StoredValueProvider4',
        owner_name='OwnerName0',
        expiry_date=4,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    current_balance=186.86,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

