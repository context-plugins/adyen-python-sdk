
# Stored Value Result

For each stored value card loaded or reloaded, in the StoredValue response message.
Result of loading/reloading a stored value card.

*This model accepts additional fields of type Any.*

## Structure

`StoredValueResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stored_value_transaction_type` | [`StoredValueTransactionType2`](../../doc/models/stored-value-transaction-type-2.md) | Required | - |
| `product_code` | `int` | Optional | Product code of item purchased with the transaction.<br>Copy.<br><br>**Constraints**: `>= 1`, `<= 20` |
| `ean_upc` | `int` | Optional | Standard product code of item purchased with the transaction.<br>Copy. |
| `item_amount` | `float` | Optional | Total amount of the item line.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `currency` | `str` | Optional | Currency of a monetary amount.<br>Copy.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |
| `stored_value_account_status` | [`StoredValueAccountStatus`](../../doc/models/stored-value-account-status.md) | Optional | - |
| `host_transaction_id` | [`HostTransactionId`](../../doc/models/host-transaction-id.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.entry_mode import EntryMode
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_status import StoredValueAccountStatus
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1
from adyen.models.stored_value_result import StoredValueResult
from adyen.models.stored_value_transaction_type_2 import StoredValueTransactionType2

stored_value_result = StoredValueResult(
    stored_value_transaction_type=StoredValueTransactionType2.REVERSE,
    product_code=20,
    ean_upc=214,
    item_amount=81.44,
    currency='Currency8',
    stored_value_account_status=StoredValueAccountStatus(
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
        current_balance=45.56,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

