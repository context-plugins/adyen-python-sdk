
# Payment Request 21

Content of the Payment Request message.

## Structure

`PaymentRequest21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_data` | [`SaleData1`](../../doc/models/sale-data-1.md) | Required | Data related to the Sale System. |
| `payment_transaction` | [`PaymentTransaction1`](../../doc/models/payment-transaction-1.md) | Required | Data related to the payment and loyalty transaction. |
| `payment_data` | [`PaymentData1`](../../doc/models/payment-data-1.md) | Optional | Data related to the payment transaction.<br>If one data element is present. |
| `loyalty_data` | [`List[LoyaltyData]`](../../doc/models/loyalty-data.md) | Optional | Data related to a Loyalty program or account.<br>Loyalty cards used with the payment transaction and read by the Sale System. |

## Example

```python
import dateutil.parser

from adyen.models.amounts_req import AmountsReq
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.instalment_1 import Instalment1
from adyen.models.instalment_type_enum import InstalmentTypeEnum
from adyen.models.loyalty_account_id_1 import LoyaltyAccountID1
from adyen.models.loyalty_data import LoyaltyData
from adyen.models.loyalty_handling_1_enum import LoyaltyHandling1Enum
from adyen.models.original_poi_transaction import OriginalPOITransaction
from adyen.models.payment_data_1 import PaymentData1
from adyen.models.payment_request_21 import PaymentRequest21
from adyen.models.payment_transaction_1 import PaymentTransaction1
from adyen.models.payment_type_1_enum import PaymentType1Enum
from adyen.models.period_unit_1_enum import PeriodUnit1Enum
from adyen.models.sale_data_1 import SaleData1
from adyen.models.sale_terminal_data_1 import SaleTerminalData1
from adyen.models.transaction_conditions import TransactionConditions
from adyen.models.transaction_id_type import TransactionIDType
from adyen.models.transaction_id_type_1 import TransactionIDType1
from adyen.models.transaction_id_type_3 import TransactionIDType3
from adyen.models.transaction_id_type_4 import TransactionIDType4

payment_request_21 = PaymentRequest21(
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
    payment_transaction=PaymentTransaction1(
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
    ),
    payment_data=PaymentData1(
        payment_type=PaymentType1Enum.NORMAL,
        split_payment_flag=False,
        requested_validity_date=dateutil.parser.parse('2016-03-13').date(),
        card_acquisition_reference=TransactionIDType(
            transaction_id='TransactionID8',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        instalment=Instalment1(
            instalment_type=InstalmentTypeEnum.DEFERREDINSTALMENTS,
            sequence_number=106,
            plan_id='PlanID4',
            period=70,
            period_unit=PeriodUnit1Enum.MONTHLY
        )
    ),
    loyalty_data=[
        LoyaltyData(
            card_acquisition_reference=TransactionIDType3(
                transaction_id='TransactionID8',
                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
            ),
            loyalty_account_id=LoyaltyAccountID1(
                entry_mode=[
                    EntryModeEnum.FILE
                ],
                identification_type=IdentificationType11Enum.ISOTRACK2,
                loyalty_id='LoyaltyID4',
                identification_support=IdentificationSupport1Enum.HYBRIDCARD
            )
        )
    ]
)
```

