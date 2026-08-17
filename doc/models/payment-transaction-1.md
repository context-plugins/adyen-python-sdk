
# Payment Transaction 1

Data related to the payment and loyalty transaction.

## Structure

`PaymentTransaction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amounts_req` | [`AmountsReq`](../../doc/models/amounts-req.md) | Required | Various amounts related to the payment request from the Sale System. |
| `original_poi_transaction` | [`OriginalPOITransaction`](../../doc/models/original-poi-transaction.md) | Optional | Identification of a previous POI transaction.<br>In the Payment Request message, it allows using the card of a previous CardAcquisition or Payment request. |
| `transaction_conditions` | [`TransactionConditions`](../../doc/models/transaction-conditions.md) | Optional | Conditions on which the transaction must be processed. |

## Example

```python
import dateutil.parser

from adyen.models.amounts_req import AmountsReq
from adyen.models.loyalty_handling_1_enum import LoyaltyHandling1Enum
from adyen.models.original_poi_transaction import OriginalPOITransaction
from adyen.models.payment_transaction_1 import PaymentTransaction1
from adyen.models.transaction_conditions import TransactionConditions
from adyen.models.transaction_id_type_4 import TransactionIDType4

payment_transaction_1 = PaymentTransaction1(
    amounts_req=AmountsReq(
        currency='Currency4',
        requested_amount=38.52,
        cash_back_amount=77.72,
        tip_amount=40.18,
        paid_amount=239.98,
        minimum_amount_to_deliver=73.38,
        maximum_cash_back_amount=36.82
    ),
    original_poi_transaction=OriginalPOITransaction(
        sale_id='SaleID6',
        poiid='POIID0',
        poi_transaction_id=TransactionIDType4(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        reuse_card_data_flag=False,
        approval_code='ApprovalCode0'
    ),
    transaction_conditions=TransactionConditions(
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
        loyalty_handling=LoyaltyHandling1Enum.FORBIDDEN
    )
)
```

