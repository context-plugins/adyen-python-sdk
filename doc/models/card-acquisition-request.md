
# Card Acquisition Request

It conveys Information related to the payment and loyalty cards to read and analyse. This message pair is usually followed by a message pair (e.g. payment or loyalty) which refers to this Card Acquisition message pair.
Content of the Card Acquisition Request message.

*This model accepts additional fields of type Any.*

## Structure

`CardAcquisitionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_data` | [`SaleData2`](../../doc/models/sale-data-2.md) | Required | - |
| `card_acquisition_transaction` | [`CardAcquisitionTransaction`](../../doc/models/card-acquisition-transaction.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.card_acquisition_request import CardAcquisitionRequest
from adyen.models.card_acquisition_transaction import CardAcquisitionTransaction
from adyen.models.force_entry_mode import ForceEntryMode
from adyen.models.loyalty_handling_2 import LoyaltyHandling2
from adyen.models.sale_data_2 import SaleData2
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.sale_transaction_id import SaleTransactionId

card_acquisition_request = CardAcquisitionRequest(
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
    card_acquisition_transaction=CardAcquisitionTransaction(
        allowed_payment_brand=[
            'AllowedPaymentBrand6',
            'AllowedPaymentBrand7'
        ],
        allowed_loyalty_brand=[
            'AllowedLoyaltyBrand4'
        ],
        loyalty_handling=LoyaltyHandling2.PROCESSED,
        customer_language='CustomerLanguage8',
        force_entry_mode=[
            ForceEntryMode.ICC
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

