
# Stored Value Data

It contains: - the identification of the stored value accounts or the stored value cards, if provided by the Sale System, and - the associated products sold by the Sale System.
Data related to the stored value card.

*This model accepts additional fields of type Any.*

## Structure

`StoredValueData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stored_value_provider` | `str` | Optional | Identification of the provider of the stored value account load/reload.<br>If more than one provider to manage on the POI, and StoredValueAccountID absent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `stored_value_transaction_type` | [`StoredValueTransactionType1`](../../doc/models/stored-value-transaction-type-1.md) | Required | - |
| `stored_value_account_id` | [`StoredValueAccountId2`](../../doc/models/stored-value-account-id-2.md) | Optional | - |
| `original_poi_transaction` | [`OriginalPoiTransaction3`](../../doc/models/original-poi-transaction-3.md) | Optional | - |
| `product_code` | `int` | Optional | Product code of item purchased with the transaction.<br><br>**Constraints**: `>= 1`, `<= 20` |
| `ean_upc` | `int` | Optional | Standard product code of item purchased with the transaction. |
| `item_amount` | `float` | Optional | Total amount of the item line.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `currency` | `str` | Optional | Currency of a monetary amount.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.entry_mode import EntryMode
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.original_poi_transaction_3 import OriginalPoiTransaction3
from adyen.models.poi_transaction_id import PoiTransactionId
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1
from adyen.models.stored_value_data import StoredValueData
from adyen.models.stored_value_transaction_type_1 import StoredValueTransactionType1

stored_value_data = StoredValueData(
    stored_value_transaction_type=StoredValueTransactionType1.LOAD,
    stored_value_provider='StoredValueProvider0',
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
    original_poi_transaction=OriginalPoiTransaction3(
        sale_id='SaleID6',
        poiid='POIID0',
        poi_transaction_id=PoiTransactionId(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        reuse_card_data_flag=False,
        approval_code='ApprovalCode0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    product_code=20,
    ean_upc=196,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

