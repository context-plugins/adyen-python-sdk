
# Stored Value Request 2

Content of the Stored Value Request message.

## Structure

`StoredValueRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_data` | [`SaleData1`](../../doc/models/sale-data-1.md) | Required | Data related to the Sale System. |
| `stored_value_data` | [`List[StoredValueData]`](../../doc/models/stored-value-data.md) | Required | Data related to the stored value card. |

## Example

```python
import dateutil.parser

from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.original_poi_transaction_1 import OriginalPOITransaction1
from adyen.models.sale_data_1 import SaleData1
from adyen.models.sale_terminal_data_1 import SaleTerminalData1
from adyen.models.stored_value_account_id_1 import StoredValueAccountID1
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.stored_value_data import StoredValueData
from adyen.models.stored_value_request_2 import StoredValueRequest2
from adyen.models.stored_value_transaction_type_1_enum import StoredValueTransactionType1Enum
from adyen.models.transaction_id_type_1 import TransactionIDType1
from adyen.models.transaction_id_type_4 import TransactionIDType4

stored_value_request_2 = StoredValueRequest2(
    sale_data=SaleData1(
        sale_transaction_id=TransactionIDType1(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        operator_id='OperatorID8',
        operator_language='OperatorLanguage2',
        shift_number='ShiftNumber0',
        sale_reference_id='SaleReferenceID8',
        sale_terminal_data=SaleTerminalData1(
            totals_group_id='TotalsGroupID4'
        )
    ),
    stored_value_data=[
        StoredValueData(
            stored_value_transaction_type=StoredValueTransactionType1Enum.RESERVE,
            stored_value_provider='StoredValueProvider2',
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
            ean_upc=194
        )
    ]
)
```

