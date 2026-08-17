
# Terminal API Response

The response payload of the Adyen Terminal API.

## Structure

`TerminalAPIResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_to_poi_response` | [`SaleToPOIResponse`](../../doc/models/sale-to-poi-response.md) | Required | The SaleToPOIResponse message pair is a container for the response message content. It contains a MessageHeader and a message body. |

## Example

```python
import dateutil.parser

from adyen.models.admin_response_2 import AdminResponse2
from adyen.models.balance_inquiry_response_2 import BalanceInquiryResponse2
from adyen.models.card_acquisition_response_2 import CardAcquisitionResponse2
from adyen.models.card_data_1 import CardData1
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.check_data_1 import CheckData1
from adyen.models.device_3_enum import Device3Enum
from adyen.models.diagnosis_response_2 import DiagnosisResponse2
from adyen.models.display_response_2 import DisplayResponse2
from adyen.models.document_qualifier_1_enum import DocumentQualifier1Enum
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.global_status_1_enum import GlobalStatus1Enum
from adyen.models.host_status import HostStatus
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.info_qualify_3_enum import InfoQualify3Enum
from adyen.models.loyalty_account import LoyaltyAccount
from adyen.models.loyalty_account_id_2 import LoyaltyAccountID2
from adyen.models.message_category_1_enum import MessageCategory1Enum
from adyen.models.message_class_1_enum import MessageClass1Enum
from adyen.models.message_header import MessageHeader
from adyen.models.message_type_1_enum import MessageType1Enum
from adyen.models.mobile_data_1 import MobileData1
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_result import OutputResult
from adyen.models.output_text import OutputText
from adyen.models.payment_account_status_2 import PaymentAccountStatus2
from adyen.models.payment_acquirer_data import PaymentAcquirerData
from adyen.models.payment_instrument_data import PaymentInstrumentData
from adyen.models.payment_instrument_data_1 import PaymentInstrumentData1
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.poi_data_1 import POIData1
from adyen.models.poi_status_1 import POIStatus1
from adyen.models.predefined_content_1 import PredefinedContent1
from adyen.models.printer_status_1_enum import PrinterStatus1Enum
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum
from adyen.models.sale_data_1 import SaleData1
from adyen.models.sale_terminal_data_1 import SaleTerminalData1
from adyen.models.sale_to_poi_response import SaleToPOIResponse
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.terminal_api_response import TerminalAPIResponse
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum
from adyen.models.transaction_id_type_1 import TransactionIDType1
from adyen.models.transaction_id_type_2 import TransactionIDType2
from adyen.models.transaction_id_type_6 import TransactionIDType6
from adyen.models.utm_coordinates import UTMCoordinates

terminal_api_response = TerminalAPIResponse(
    sale_to_poi_response=SaleToPOIResponse(
        message_header=MessageHeader(
            message_class=MessageClass1Enum.SERVICE,
            message_category=MessageCategory1Enum.STOREDVALUE,
            message_type=MessageType1Enum.NOTIFICATION,
            sale_id='SaleID4',
            poiid='POIID0',
            protocol_version='ProtocolVersion2',
            service_id='ServiceID2',
            device_id='DeviceID4'
        ),
        balance_inquiry_response=BalanceInquiryResponse2(
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
                )
            ]
        ),
        card_acquisition_response=CardAcquisitionResponse2(
            response=Response11(
                result=Result11Enum.PARTIAL,
                error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
                additional_response='AdditionalResponse8'
            ),
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
            poi_data=POIData1(
                poi_transaction_id=TransactionIDType2(
                    transaction_id='TransactionID2',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                poi_reconciliation_id=52
            ),
            payment_brand=[
                'PaymentBrand1',
                'PaymentBrand2',
                'PaymentBrand3'
            ],
            payment_instrument_data=PaymentInstrumentData1(
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
            loyalty_account=[
                LoyaltyAccount(
                    loyalty_account_id=LoyaltyAccountID2(
                        entry_mode=[
                            EntryModeEnum.FILE
                        ],
                        identification_type=IdentificationType11Enum.ISOTRACK2,
                        loyalty_id='LoyaltyID4',
                        identification_support=IdentificationSupport1Enum.HYBRIDCARD
                    ),
                    loyalty_brand='LoyaltyBrand0'
                )
            ]
        ),
        admin_response=AdminResponse2(
            response=Response11(
                result=Result11Enum.PARTIAL,
                error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
                additional_response='AdditionalResponse8'
            )
        ),
        diagnosis_response=DiagnosisResponse2(
            response=Response11(
                result=Result11Enum.PARTIAL,
                error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
                additional_response='AdditionalResponse8'
            ),
            poi_status=POIStatus1(
                global_status=GlobalStatus1Enum.MAINTENANCE,
                security_ok_flag=False,
                pedok_flag=False,
                card_reader_ok_flag=False,
                printer_status=PrinterStatus1Enum.PAPERLOW,
                communication_ok_flag=False
            ),
            host_status=[
                HostStatus(
                    acquirer_id=120,
                    is_reachable_flag=False
                ),
                HostStatus(
                    acquirer_id=120,
                    is_reachable_flag=False
                )
            ]
        ),
        display_response=DisplayResponse2(
            output_result=[
                OutputResult(
                    device=Device3Enum.CASHIERINPUT,
                    info_qualify=InfoQualify3Enum.DOCUMENT,
                    response=Response11(
                        result=Result11Enum.PARTIAL,
                        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
                        additional_response='AdditionalResponse8'
                    )
                ),
                OutputResult(
                    device=Device3Enum.CASHIERINPUT,
                    info_qualify=InfoQualify3Enum.DOCUMENT,
                    response=Response11(
                        result=Result11Enum.PARTIAL,
                        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
                        additional_response='AdditionalResponse8'
                    )
                ),
                OutputResult(
                    device=Device3Enum.CASHIERINPUT,
                    info_qualify=InfoQualify3Enum.DOCUMENT,
                    response=Response11(
                        result=Result11Enum.PARTIAL,
                        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
                        additional_response='AdditionalResponse8'
                    )
                )
            ]
        )
    )
)
```

