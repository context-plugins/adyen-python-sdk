
# Balance Inquiry Response

Content of the Balance Inquiry Response message.
It conveys the balance and the identification of the associated payment, loyalty or stored value account.

## Structure

`BalanceInquiryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |
| `payment_account_status` | [`PaymentAccountStatus2`](../../doc/models/payment-account-status-2.md) | Optional | Data related to the result of a Balance Inquiry request.<br>If BalanceInquiryRequest. PaymentAccount present. |
| `payment_receipt` | [`List[PaymentReceipt]`](../../doc/models/payment-receipt.md) | Optional | - |

## Example

```python
import dateutil.parser

from adyen.models.balance_inquiry_response import BalanceInquiryResponse
from adyen.models.card_data_1 import CardData1
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.check_data_1 import CheckData1
from adyen.models.document_qualifier_1_enum import DocumentQualifier1Enum
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.mobile_data_1 import MobileData1
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_text import OutputText
from adyen.models.payment_account_status_2 import PaymentAccountStatus2
from adyen.models.payment_acquirer_data import PaymentAcquirerData
from adyen.models.payment_instrument_data import PaymentInstrumentData
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.predefined_content_1 import PredefinedContent1
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum
from adyen.models.transaction_id_type_6 import TransactionIDType6
from adyen.models.utm_coordinates import UTMCoordinates

balance_inquiry_response = BalanceInquiryResponse(
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    ),
    payment_account_status=PaymentAccountStatus2(
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
        current_balance=83.4,
        currency='Currency4',
        payment_acquirer_data=PaymentAcquirerData(
            merchant_id='MerchantID6',
            acquirer_poiid='AcquirerPOIID4',
            acquirer_id=238,
            acquirer_transaction_id=TransactionIDType6(
                transaction_id='TransactionID2',
                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
            ),
            approval_code='ApprovalCode8',
            host_reconciliation_id='HostReconciliationID8'
        )
    ),
    payment_receipt=[
        PaymentReceipt(
            document_qualifier=DocumentQualifier1Enum.CUSTOMERRECEIPT,
            output_content=OutputContent1(
                output_format=OutputFormat1Enum.XHTML,
                predefined_content=PredefinedContent1(
                    reference_id='ReferenceID0',
                    language='Language2'
                ),
                output_text=[
                    OutputText(
                        text='Text6',
                        character_set=194,
                        start_row=74,
                        start_column=220,
                        character_width=CharacterWidth1Enum.SINGLEWIDTH,
                        character_height=CharacterHeight1Enum.SINGLEHEIGHT
                    )
                ],
                output_xhtml='OutputXHTML2',
                output_barcode=OutputBarcode1(
                    barcode_value='BarcodeValue2'
                )
            ),
            integrated_print_flag=False,
            required_signature_flag=False
        ),
        PaymentReceipt(
            document_qualifier=DocumentQualifier1Enum.CUSTOMERRECEIPT,
            output_content=OutputContent1(
                output_format=OutputFormat1Enum.XHTML,
                predefined_content=PredefinedContent1(
                    reference_id='ReferenceID0',
                    language='Language2'
                ),
                output_text=[
                    OutputText(
                        text='Text6',
                        character_set=194,
                        start_row=74,
                        start_column=220,
                        character_width=CharacterWidth1Enum.SINGLEWIDTH,
                        character_height=CharacterHeight1Enum.SINGLEHEIGHT
                    )
                ],
                output_xhtml='OutputXHTML2',
                output_barcode=OutputBarcode1(
                    barcode_value='BarcodeValue2'
                )
            ),
            integrated_print_flag=False,
            required_signature_flag=False
        )
    ]
)
```

