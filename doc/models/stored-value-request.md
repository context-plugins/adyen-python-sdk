
# Stored Value Request

It conveys Information related to the Stored Value transaction to process.
Content of the Stored Value Request message.

*This model accepts additional fields of type Any.*

## Structure

`StoredValueRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_data` | [`SaleData2`](../../doc/models/sale-data-2.md) | Required | - |
| `stored_value_data` | [`List[StoredValueData]`](../../doc/models/stored-value-data.md) | Required | Data related to the stored value card. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.entry_mode import EntryMode
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.original_poi_transaction_3 import OriginalPoiTransaction3
from adyen.models.poi_transaction_id import PoiTransactionId
from adyen.models.sale_data_2 import SaleData2
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.sale_transaction_id import SaleTransactionId
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1
from adyen.models.stored_value_data import StoredValueData
from adyen.models.stored_value_request import StoredValueRequest
from adyen.models.stored_value_transaction_type_1 import StoredValueTransactionType1

stored_value_request = StoredValueRequest(
    sale_data=SaleData2(
        sale_transaction_id=SaleTransactionId(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        operator_id='OperatorID8',
        operator_language='OperatorLanguage2',
        shift_number='ShiftNumber0',
        sale_reference_id='SaleReferenceID8',
        sale_terminal_data=SaleTerminalData3(
            totals_group_id='TotalsGroupID4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    stored_value_data=[
        StoredValueData(
            stored_value_transaction_type=StoredValueTransactionType1.RESERVE,
            stored_value_provider='StoredValueProvider2',
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
            ean_upc=194,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

