
# Payment Transaction

*This model accepts additional fields of type Any.*

## Structure

`PaymentTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amounts_req` | [`AmountsReq1`](../../doc/models/amounts-req-1.md) | Required | - |
| `original_poi_transaction` | [`OriginalPoiTransaction3`](../../doc/models/original-poi-transaction-3.md) | Optional | - |
| `transaction_conditions` | [`TransactionConditions1`](../../doc/models/transaction-conditions-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amounts_req_1 import AmountsReq1
from adyen.models.loyalty_handling_1 import LoyaltyHandling1
from adyen.models.original_poi_transaction_3 import OriginalPoiTransaction3
from adyen.models.payment_transaction import PaymentTransaction
from adyen.models.poi_transaction_id import PoiTransactionId
from adyen.models.transaction_conditions_1 import TransactionConditions1

payment_transaction = PaymentTransaction(
    amounts_req=AmountsReq1(
        currency='Currency4',
        requested_amount=38.52,
        cash_back_amount=77.72,
        tip_amount=40.18,
        paid_amount=239.98,
        minimum_amount_to_deliver=73.38,
        maximum_cash_back_amount=36.82,
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
    transaction_conditions=TransactionConditions1(
        allowed_payment_brand=[
            'AllowedPaymentBrand0',
            'AllowedPaymentBrand1',
            'AllowedPaymentBrand2'
        ],
        acquirer_id=[
            56,
            57,
            58
        ],
        debit_preferred_flag=False,
        allowed_loyalty_brand=[
            'AllowedLoyaltyBrand8',
            'AllowedLoyaltyBrand9'
        ],
        loyalty_handling=LoyaltyHandling1.FORBIDDEN,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

