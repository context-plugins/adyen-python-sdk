
# Repeated Message Response

## Structure

`RepeatedMessageResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_header` | [`MessageHeader`](../../doc/models/message-header.md) | Required | Message header of the Sale to POI protocol message.<br>It conveys Information related to the Sale to POI protocol management. |
| `repeated_response_message_body` | [`RepeatedResponseMessageBody`](../../doc/models/repeated-response-message-body.md) | Required | - |

## Example

```python
import dateutil.parser

from adyen.models.amounts_resp_1 import AmountsResp1
from adyen.models.card_acquisition_response import CardAcquisitionResponse
from adyen.models.card_data_1 import CardData1
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.check_data_1 import CheckData1
from adyen.models.converted_amount_1 import ConvertedAmount1
from adyen.models.currency_conversion import CurrencyConversion
from adyen.models.document_qualifier_1_enum import DocumentQualifier1Enum
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.instalment_1 import Instalment1
from adyen.models.instalment_type_enum import InstalmentTypeEnum
from adyen.models.loyalty_account import LoyaltyAccount
from adyen.models.loyalty_account_1 import LoyaltyAccount1
from adyen.models.loyalty_account_id_2 import LoyaltyAccountID2
from adyen.models.loyalty_acquirer_data_1 import LoyaltyAcquirerData1
from adyen.models.loyalty_response import LoyaltyResponse
from adyen.models.loyalty_result import LoyaltyResult
from adyen.models.message_category_1_enum import MessageCategory1Enum
from adyen.models.message_class_1_enum import MessageClass1Enum
from adyen.models.message_header import MessageHeader
from adyen.models.message_type_1_enum import MessageType1Enum
from adyen.models.mobile_data_1 import MobileData1
from adyen.models.original_poi_transaction import OriginalPOITransaction
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_text import OutputText
from adyen.models.payment_instrument_data import PaymentInstrumentData
from adyen.models.payment_instrument_data_1 import PaymentInstrumentData1
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.payment_response_4 import PaymentResponse4
from adyen.models.payment_result_11 import PaymentResult11
from adyen.models.payment_type_1_enum import PaymentType1Enum
from adyen.models.period_unit_1_enum import PeriodUnit1Enum
from adyen.models.poi_data_1 import POIData1
from adyen.models.poi_data_4 import POIData4
from adyen.models.predefined_content_1 import PredefinedContent1
from adyen.models.repeated_message_response import RepeatedMessageResponse
from adyen.models.repeated_response_message_body import RepeatedResponseMessageBody
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum
from adyen.models.reversal_response import ReversalResponse
from adyen.models.sale_data_1 import SaleData1
from adyen.models.sale_data_6 import SaleData6
from adyen.models.sale_terminal_data_1 import SaleTerminalData1
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_status_1 import StoredValueAccountStatus1
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.stored_value_response import StoredValueResponse
from adyen.models.stored_value_result import StoredValueResult
from adyen.models.stored_value_transaction_type_2_enum import StoredValueTransactionType2Enum
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum
from adyen.models.transaction_id_type import TransactionIDType
from adyen.models.transaction_id_type_1 import TransactionIDType1
from adyen.models.transaction_id_type_2 import TransactionIDType2
from adyen.models.transaction_id_type_4 import TransactionIDType4
from adyen.models.utm_coordinates import UTMCoordinates

repeated_message_response = RepeatedMessageResponse(
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
    repeated_response_message_body=RepeatedResponseMessageBody(
        loyalty_response=LoyaltyResponse(
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
                )
            ],
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
        ),
        payment_response=PaymentResponse4(
            response=Response11(
                result=Result11Enum.PARTIAL,
                error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
                additional_response='AdditionalResponse8'
            ),
            sale_data=SaleData6(
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
            payment_result=PaymentResult11(
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
        reversal_response=ReversalResponse(
            response=Response11(
                result=Result11Enum.PARTIAL,
                error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
                additional_response='AdditionalResponse8'
            ),
            poi_data=POIData4(
                poi_transaction_id=TransactionIDType2(
                    transaction_id='TransactionID2',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                poi_reconciliation_id=52
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
            reversed_amount=90.36,
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
        ),
        stored_value_response=StoredValueResponse(
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
            stored_value_result=[
                StoredValueResult(
                    stored_value_transaction_type=StoredValueTransactionType2Enum.REVERSE,
                    product_code=20,
                    ean_upc=136,
                    item_amount=5.58,
                    currency='Currency2',
                    stored_value_account_status=StoredValueAccountStatus1(
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
                        ),
                        current_balance=45.56
                    )
                ),
                StoredValueResult(
                    stored_value_transaction_type=StoredValueTransactionType2Enum.REVERSE,
                    product_code=20,
                    ean_upc=136,
                    item_amount=5.58,
                    currency='Currency2',
                    stored_value_account_status=StoredValueAccountStatus1(
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
                        ),
                        current_balance=45.56
                    )
                ),
                StoredValueResult(
                    stored_value_transaction_type=StoredValueTransactionType2Enum.REVERSE,
                    product_code=20,
                    ean_upc=136,
                    item_amount=5.58,
                    currency='Currency2',
                    stored_value_account_status=StoredValueAccountStatus1(
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
                        ),
                        current_balance=45.56
                    )
                )
            ],
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
        card_acquisition_response=CardAcquisitionResponse(
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
        )
    )
)
```

