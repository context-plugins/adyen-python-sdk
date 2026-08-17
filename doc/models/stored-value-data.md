
# Stored Value Data

It contains: - the identification of the stored value accounts or the stored value cards, if provided by the Sale System, and - the associated products sold by the Sale System.
Data related to the stored value card.

## Structure

`StoredValueData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stored_value_provider` | `str` | Optional | Identification of the provider of the stored value account load/reload.<br>If more than one provider to manage on the POI, and StoredValueAccountID absent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `stored_value_transaction_type` | [`StoredValueTransactionType1Enum`](../../doc/models/stored-value-transaction-type-1-enum.md) | Required | Identification of operation to proceed on the stored value account or the stored value card.<br>Possible values:<br><br>* **Activate**<br>* **Duplicate**<br>* **Load**<br>* **Reserve**<br>* **Reverse**<br>* **Unload** |
| `stored_value_account_id` | [`StoredValueAccountID1`](../../doc/models/stored-value-account-id-1.md) | Optional | Identification of the stored value account or the stored value card.<br>If the identification of the Stored Value account or card has been made by the Sale System before the request. |
| `original_poi_transaction` | [`OriginalPOITransaction1`](../../doc/models/original-poi-transaction-1.md) | Optional | Identification of a previous POI transaction.<br>If StoredValueTransactionType is Reverse or Duplicate. |
| `product_code` | `int` | Optional | Product code of item purchased with the transaction.<br><br>**Constraints**: `>= 1`, `<= 20` |
| `ean_upc` | `int` | Optional | Standard product code of item purchased with the transaction. |
| `item_amount` | `float` | Optional | Total amount of the item line.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `currency` | `str` | Optional | Currency of a monetary amount.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |

## Example

```python
import dateutil.parser

from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.original_poi_transaction_1 import OriginalPOITransaction1
from adyen.models.stored_value_account_id_1 import StoredValueAccountID1
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.stored_value_data import StoredValueData
from adyen.models.stored_value_transaction_type_1_enum import StoredValueTransactionType1Enum
from adyen.models.transaction_id_type_4 import TransactionIDType4

stored_value_data = StoredValueData(
    stored_value_transaction_type=StoredValueTransactionType1Enum.LOAD,
    stored_value_provider='StoredValueProvider0',
    stored_value_account_id=StoredValueAccountID1(
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
    original_poi_transaction=OriginalPOITransaction1(
        sale_id='SaleID6',
        poiid='POIID0',
        poi_transaction_id=TransactionIDType4(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        reuse_card_data_flag=False,
        approval_code='ApprovalCode0'
    ),
    product_code=20,
    ean_upc=196
)
```

