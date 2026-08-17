
# Performed Transaction

## Structure

`PerformedTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response1`](../../doc/models/response-1.md) | Required | Result of a message request processing.<br>If Result is Success, `ErrorCondition` is absent or not used in the processing of the message. In the other cases, the `ErrorCondition` has to be present and can refine the processing of the message response. `AdditionalResponse` gives more information about the success or the failure of the message request processing, for logging without real time involvements. |
| `sale_data` | [`SaleData`](../../doc/models/sale-data.md) | Optional | Data associated with the Sale System, with a particular value during the processing of the payment by the POI, including the cards acquisition. |
| `poi_data` | [`POIData`](../../doc/models/poi-data.md) | Optional | Data related to the POI System.<br>In the Message Response, identification of the POI transaction. |
| `payment_result` | [`PaymentResult1`](../../doc/models/payment-result-1.md) | Optional | - |
| `loyalty_result` | [`List[LoyaltyResult]`](../../doc/models/loyalty-result.md) | Optional | - |
| `reversed_amount` | `float` | Optional | **Constraints**: `>= 0`, `<= 99999999.999999` |

## Example

```python
import dateutil.parser

from adyen.models.amounts_resp_1 import AmountsResp1
from adyen.models.card_data_1 import CardData1
from adyen.models.check_data_1 import CheckData1
from adyen.models.converted_amount_1 import ConvertedAmount1
from adyen.models.currency_conversion import CurrencyConversion
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.instalment_1 import Instalment1
from adyen.models.instalment_type_enum import InstalmentTypeEnum
from adyen.models.loyalty_account_1 import LoyaltyAccount1
from adyen.models.loyalty_account_id_2 import LoyaltyAccountID2
from adyen.models.loyalty_acquirer_data_1 import LoyaltyAcquirerData1
from adyen.models.loyalty_result import LoyaltyResult
from adyen.models.mobile_data_1 import MobileData1
from adyen.models.payment_instrument_data import PaymentInstrumentData
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.payment_result_1 import PaymentResult1
from adyen.models.payment_type_1_enum import PaymentType1Enum
from adyen.models.performed_transaction import PerformedTransaction
from adyen.models.period_unit_1_enum import PeriodUnit1Enum
from adyen.models.poi_data import POIData
from adyen.models.response_1 import Response1
from adyen.models.result_11_enum import Result11Enum
from adyen.models.sale_data import SaleData
from adyen.models.sale_terminal_data_1 import SaleTerminalData1
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum
from adyen.models.transaction_id_type import TransactionIDType
from adyen.models.transaction_id_type_1 import TransactionIDType1
from adyen.models.transaction_id_type_2 import TransactionIDType2
from adyen.models.utm_coordinates import UTMCoordinates

performed_transaction = PerformedTransaction(
    response=Response1(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    ),
    sale_data=SaleData(
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
    poi_data=POIData(
        poi_transaction_id=TransactionIDType2(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        poi_reconciliation_id=52
    ),
    payment_result=PaymentResult1(
        payment_type=PaymentType1Enum.ISSUERINSTALMENT,
        payment_instrument_data=PaymentInstrumentData(
            payment_instrument_type=PaymentInstrumentType11Enum.CASH,
            protected_card_data='ProtectedCardData8',
            card_data=CardData1(
                payment_brand='PaymentBrand0',
                masked_pan='MaskedPan0',
                payment_account_ref='PaymentAccountRef8',
                entry_mode=[
                    EntryModeEnum.MANUAL,
                    EntryModeEnum.KEYED
                ],
                card_country_code=3
            ),
            check_data=CheckData1(
                bank_id='BankID0',
                account_number='AccountNumber6',
                check_number='CheckNumber2',
                track_data=TrackData1(
                    track_value='TrackValue6',
                    track_numb=3,
                    track_format=TrackFormat1Enum.JISII
                ),
                check_card_number='CheckCardNumber6'
            ),
            mobile_data=MobileData1(
                mobile_country_code=3,
                mobile_network_code=3,
                masked_msisdn=22,
                geolocation=Geolocation1(
                    geographic_coordinates=GeographicCoordinates(
                        latitude='Latitude4',
                        longitude='Longitude2'
                    ),
                    utm_coordinates=UTMCoordinates(
                        utm_zone='UTMZone6',
                        utm_eastward='UTMEastward0',
                        utm_northward='UTMNorthward0'
                    )
                ),
                protected_mobile_data='ProtectedMobileData0'
            ),
            stored_value_account_id=StoredValueAccountID(
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
            )
        ),
        amounts_resp=AmountsResp1(
            authorized_amount=133.28,
            currency='Currency0',
            total_rebates_amount=120.04,
            total_fees_amount=181.08,
            cash_back_amount=206.58,
            tip_amount=86.96
        ),
        instalment=Instalment1(
            instalment_type=InstalmentTypeEnum.DEFERREDINSTALMENTS,
            sequence_number=106,
            plan_id='PlanID4',
            period=70,
            period_unit=PeriodUnit1Enum.MONTHLY
        ),
        currency_conversion=[
            CurrencyConversion(
                converted_amount=ConvertedAmount1(
                    amount_value=81.82,
                    currency='Currency0'
                ),
                customer_approved_flag=False,
                rate=175.8,
                markup=100.86,
                commission=197.78,
                declaration='Declaration4'
            ),
            CurrencyConversion(
                converted_amount=ConvertedAmount1(
                    amount_value=81.82,
                    currency='Currency0'
                ),
                customer_approved_flag=False,
                rate=175.8,
                markup=100.86,
                commission=197.78,
                declaration='Declaration4'
            )
        ]
    ),
    loyalty_result=[
        LoyaltyResult(
            loyalty_account=LoyaltyAccount1(
                loyalty_account_id=LoyaltyAccountID2(
                    entry_mode=[
                        EntryModeEnum.FILE
                    ],
                    identification_type=IdentificationType11Enum.ISOTRACK2,
                    loyalty_id='LoyaltyID4',
                    identification_support=IdentificationSupport1Enum.HYBRIDCARD
                ),
                loyalty_brand='LoyaltyBrand0'
            ),
            current_balance=171.12,
            loyalty_acquirer_data=LoyaltyAcquirerData1(
                loyalty_acquirer_id='LoyaltyAcquirerID4',
                approval_code='ApprovalCode4',
                loyalty_transaction_id=TransactionIDType(
                    transaction_id='TransactionID6',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                host_reconciliation_id='HostReconciliationID4'
            )
        ),
        LoyaltyResult(
            loyalty_account=LoyaltyAccount1(
                loyalty_account_id=LoyaltyAccountID2(
                    entry_mode=[
                        EntryModeEnum.FILE
                    ],
                    identification_type=IdentificationType11Enum.ISOTRACK2,
                    loyalty_id='LoyaltyID4',
                    identification_support=IdentificationSupport1Enum.HYBRIDCARD
                ),
                loyalty_brand='LoyaltyBrand0'
            ),
            current_balance=171.12,
            loyalty_acquirer_data=LoyaltyAcquirerData1(
                loyalty_acquirer_id='LoyaltyAcquirerID4',
                approval_code='ApprovalCode4',
                loyalty_transaction_id=TransactionIDType(
                    transaction_id='TransactionID6',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                host_reconciliation_id='HostReconciliationID4'
            )
        ),
        LoyaltyResult(
            loyalty_account=LoyaltyAccount1(
                loyalty_account_id=LoyaltyAccountID2(
                    entry_mode=[
                        EntryModeEnum.FILE
                    ],
                    identification_type=IdentificationType11Enum.ISOTRACK2,
                    loyalty_id='LoyaltyID4',
                    identification_support=IdentificationSupport1Enum.HYBRIDCARD
                ),
                loyalty_brand='LoyaltyBrand0'
            ),
            current_balance=171.12,
            loyalty_acquirer_data=LoyaltyAcquirerData1(
                loyalty_acquirer_id='LoyaltyAcquirerID4',
                approval_code='ApprovalCode4',
                loyalty_transaction_id=TransactionIDType(
                    transaction_id='TransactionID6',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                host_reconciliation_id='HostReconciliationID4'
            )
        )
    ],
    reversed_amount=85.76
)
```

