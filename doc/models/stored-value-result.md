
# Stored Value Result

For each stored value card loaded or reloaded, in the StoredValue response message.
Result of loading/reloading a stored value card.

## Structure

`StoredValueResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stored_value_transaction_type` | [`StoredValueTransactionType2Enum`](../../doc/models/stored-value-transaction-type-2-enum.md) | Required | Identification of operation to proceed on the stored value account or the stored value card.<br>Copy.<br>Possible values:<br><br>* **Activate**<br>* **Duplicate**<br>* **Load**<br>* **Reserve**<br>* **Reverse**<br>* **Unload** |
| `product_code` | `int` | Optional | Product code of item purchased with the transaction.<br>Copy.<br><br>**Constraints**: `>= 1`, `<= 20` |
| `ean_upc` | `int` | Optional | Standard product code of item purchased with the transaction.<br>Copy. |
| `item_amount` | `float` | Optional | Total amount of the item line.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `currency` | `str` | Optional | Currency of a monetary amount.<br>Copy.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |
| `stored_value_account_status` | [`StoredValueAccountStatus1`](../../doc/models/stored-value-account-status-1.md) | Optional | Data related to the result of the stored value card transaction. |
| `host_transaction_id` | [`TransactionIDType7`](../../doc/models/transaction-id-type-7.md) | Optional | Identification of the transaction by the host in charge of the stored value transaction.<br>If provided by the Host. |

## Example

```python
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_status_1 import StoredValueAccountStatus1
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.stored_value_result import StoredValueResult
from adyen.models.stored_value_transaction_type_2_enum import StoredValueTransactionType2Enum

stored_value_result = StoredValueResult(
    stored_value_transaction_type=StoredValueTransactionType2Enum.REVERSE,
    product_code=20,
    ean_upc=214,
    item_amount=81.44,
    currency='Currency8',
    stored_value_account_status=StoredValueAccountStatus1(
        stored_value_account_id=StoredValueAccountID(
            stored_value_account_type=StoredValueAccountType1Enum.PHONECARD,
            entry_mode=[
                EntryModeEnum.MAGSTRIPE,
                EntryModeEnum.SCANNED
            ],
            identification_type=IdentificationType11Enum.PHONENUMBER,
            stored_value_id='StoredValueID8',
            stored_value_provider='StoredValueProvider4',
            owner_name='OwnerName0',
            expiry_date=4
        ),
        current_balance=45.56
    )
)
```

