
# Payment Request 2

Request sent to terminal to initiate payment.
It conveys Information related to the Payment transaction to process.
Content of the `PaymentRequest` message.

*This model accepts additional fields of type Any.*

## Structure

`PaymentRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_data` | [`SaleData2`](../../doc/models/sale-data-2.md) | Required | - |
| `payment_transaction` | [`PaymentTransaction`](../../doc/models/payment-transaction.md) | Required | - |
| `payment_data` | [`PaymentData`](../../doc/models/payment-data.md) | Optional | - |
| `loyalty_data` | [`List[LoyaltyData]`](../../doc/models/loyalty-data.md) | Optional | Data related to a Loyalty program or account.<br>Loyalty cards used with the payment transaction and read by the Sale System. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amounts_req_1 import AmountsReq1
from adyen.models.card_acquisition_reference import CardAcquisitionReference
from adyen.models.entry_mode import EntryMode
from adyen.models.identification_support_1 import IdentificationSupport1
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.instalment import Instalment
from adyen.models.instalment_type import InstalmentType
from adyen.models.loyalty_account_id_3 import LoyaltyAccountId3
from adyen.models.loyalty_data import LoyaltyData
from adyen.models.loyalty_handling_1 import LoyaltyHandling1
from adyen.models.original_poi_transaction_3 import OriginalPoiTransaction3
from adyen.models.payment_data import PaymentData
from adyen.models.payment_request_2 import PaymentRequest2
from adyen.models.payment_transaction import PaymentTransaction
from adyen.models.payment_type_1 import PaymentType1
from adyen.models.period_unit_1 import PeriodUnit1
from adyen.models.poi_transaction_id import PoiTransactionId
from adyen.models.sale_data_2 import SaleData2
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.sale_transaction_id import SaleTransactionId
from adyen.models.transaction_conditions_1 import TransactionConditions1

payment_request_2 = PaymentRequest2(
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
    payment_transaction=PaymentTransaction(
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
    ),
    payment_data=PaymentData(
        payment_type=PaymentType1.NORMAL,
        split_payment_flag=False,
        requested_validity_date=dateutil.parser.parse('2016-03-13').date(),
        card_acquisition_reference=CardAcquisitionReference(
            transaction_id='TransactionID8',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        instalment=Instalment(
            instalment_type=InstalmentType.DEFERREDINSTALMENTS,
            sequence_number=106,
            plan_id='PlanID4',
            period=70,
            period_unit=PeriodUnit1.MONTHLY,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    loyalty_data=[
        LoyaltyData(
            card_acquisition_reference=CardAcquisitionReference(
                transaction_id='TransactionID8',
                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            loyalty_account_id=LoyaltyAccountId3(
                entry_mode=[
                    EntryMode.FILE
                ],
                identification_type=IdentificationType11.ISOTRACK2,
                loyalty_id='LoyaltyID4',
                identification_support=IdentificationSupport1.HYBRIDCARD,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        LoyaltyData(
            card_acquisition_reference=CardAcquisitionReference(
                transaction_id='TransactionID8',
                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            loyalty_account_id=LoyaltyAccountId3(
                entry_mode=[
                    EntryMode.FILE
                ],
                identification_type=IdentificationType11.ISOTRACK2,
                loyalty_id='LoyaltyID4',
                identification_support=IdentificationSupport1.HYBRIDCARD,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        LoyaltyData(
            card_acquisition_reference=CardAcquisitionReference(
                transaction_id='TransactionID8',
                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            loyalty_account_id=LoyaltyAccountId3(
                entry_mode=[
                    EntryMode.FILE
                ],
                identification_type=IdentificationType11.ISOTRACK2,
                loyalty_id='LoyaltyID4',
                identification_support=IdentificationSupport1.HYBRIDCARD,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
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

