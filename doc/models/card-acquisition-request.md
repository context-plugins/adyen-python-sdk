
# Card Acquisition Request

It conveys Information related to the payment and loyalty cards to read and analyse. This message pair is usually followed by a message pair (e.g. payment or loyalty) which refers to this Card Acquisition message pair.
Content of the Card Acquisition Request message.

## Structure

`CardAcquisitionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_data` | [`SaleData1`](../../doc/models/sale-data-1.md) | Required | Data related to the Sale System. |
| `card_acquisition_transaction` | [`CardAcquisitionTransaction1`](../../doc/models/card-acquisition-transaction-1.md) | Required | Data related to the payment and loyalty card acquisition. |

## Example

```python
import dateutil.parser

from adyen.models.card_acquisition_request import CardAcquisitionRequest
from adyen.models.card_acquisition_transaction_1 import CardAcquisitionTransaction1
from adyen.models.force_entry_mode_enum import ForceEntryModeEnum
from adyen.models.loyalty_handling_2_enum import LoyaltyHandling2Enum
from adyen.models.sale_data_1 import SaleData1
from adyen.models.sale_terminal_data_1 import SaleTerminalData1
from adyen.models.transaction_id_type_1 import TransactionIDType1

card_acquisition_request = CardAcquisitionRequest(
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
    card_acquisition_transaction=CardAcquisitionTransaction1(
        allowed_payment_brand=[
            'AllowedPaymentBrand6',
            'AllowedPaymentBrand7'
        ],
        allowed_loyalty_brand=[
            'AllowedLoyaltyBrand4'
        ],
        loyalty_handling=LoyaltyHandling2Enum.PROCESSED,
        customer_language='CustomerLanguage8',
        force_entry_mode=[
            ForceEntryModeEnum.ICC
        ]
    )
)
```

