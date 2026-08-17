
# Terminal API Request

The request payload of the Adyen Terminal API.

## Structure

`TerminalAPIRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sale_to_poi_request` | [`SaleToPOIRequest`](../../doc/models/sale-to-poi-request.md) | Required | The SaleToPOIRequest message pair is a container for the request message content. It contains a MessageHeader and a message body. |

## Example

```python
import dateutil.parser

from adyen.models.abort_request_2 import AbortRequest2
from adyen.models.account_type_12_enum import AccountType12Enum
from adyen.models.admin_request_2 import AdminRequest2
from adyen.models.balance_inquiry_request_2 import BalanceInquiryRequest2
from adyen.models.card_acquisition_request_2 import CardAcquisitionRequest2
from adyen.models.card_acquisition_transaction_1 import CardAcquisitionTransaction1
from adyen.models.card_data_1 import CardData1
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.check_data_1 import CheckData1
from adyen.models.device_11_enum import Device11Enum
from adyen.models.diagnosis_request_2 import DiagnosisRequest2
from adyen.models.display_output_1 import DisplayOutput1
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.force_entry_mode_enum import ForceEntryModeEnum
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.info_qualify_1_enum import InfoQualify1Enum
from adyen.models.loyalty_account_id import LoyaltyAccountID
from adyen.models.loyalty_account_req_2 import LoyaltyAccountReq2
from adyen.models.loyalty_handling_2_enum import LoyaltyHandling2Enum
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1_enum import MenuEntryTag1Enum
from adyen.models.message_category_1_enum import MessageCategory1Enum
from adyen.models.message_category_2_enum import MessageCategory2Enum
from adyen.models.message_class_1_enum import MessageClass1Enum
from adyen.models.message_header import MessageHeader
from adyen.models.message_reference_4 import MessageReference4
from adyen.models.message_type_1_enum import MessageType1Enum
from adyen.models.mobile_data_1 import MobileData1
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_format_2_enum import OutputFormat2Enum
from adyen.models.output_text import OutputText
from adyen.models.payment_account_req_2 import PaymentAccountReq2
from adyen.models.payment_instrument_data import PaymentInstrumentData
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.predefined_content import PredefinedContent
from adyen.models.predefined_content_1 import PredefinedContent1
from adyen.models.sale_data_1 import SaleData1
from adyen.models.sale_terminal_data_1 import SaleTerminalData1
from adyen.models.sale_to_poi_request import SaleToPOIRequest
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.terminal_api_request import TerminalAPIRequest
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum
from adyen.models.transaction_id_type import TransactionIDType
from adyen.models.transaction_id_type_1 import TransactionIDType1
from adyen.models.utm_coordinates import UTMCoordinates

terminal_api_request = TerminalAPIRequest(
    sale_to_poi_request=SaleToPOIRequest(
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
        abort_request=AbortRequest2(
            message_reference=MessageReference4(
                message_category=MessageCategory2Enum.PAYMENT,
                service_id='ServiceID0',
                device_id='DeviceID2',
                sale_id='SaleID8',
                poiid='POIID2'
            ),
            abort_reason='AbortReason6',
            display_output=DisplayOutput1(
                device=Device11Enum.CASHIERDISPLAY,
                info_qualify=InfoQualify1Enum.STATUS,
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
                response_required_flag=False,
                minimum_display_time=110,
                menu_entry=[
                    MenuEntry(
                        output_format=OutputFormat2Enum.XHTML,
                        menu_entry_tag=MenuEntryTag1Enum.SUBMENU,
                        default_selected_flag=False,
                        predefined_content=PredefinedContent(
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
                            ),
                            OutputText(
                                text='Text6',
                                character_set=194,
                                start_row=74,
                                start_column=220,
                                character_width=CharacterWidth1Enum.SINGLEWIDTH,
                                character_height=CharacterHeight1Enum.SINGLEHEIGHT
                            )
                        ],
                        output_xhtml='OutputXHTML8'
                    ),
                    MenuEntry(
                        output_format=OutputFormat2Enum.XHTML,
                        menu_entry_tag=MenuEntryTag1Enum.SUBMENU,
                        default_selected_flag=False,
                        predefined_content=PredefinedContent(
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
                            ),
                            OutputText(
                                text='Text6',
                                character_set=194,
                                start_row=74,
                                start_column=220,
                                character_width=CharacterWidth1Enum.SINGLEWIDTH,
                                character_height=CharacterHeight1Enum.SINGLEHEIGHT
                            )
                        ],
                        output_xhtml='OutputXHTML8'
                    )
                ],
                output_signature='OutputSignature4'
            )
        ),
        balance_inquiry_request=BalanceInquiryRequest2(
            payment_account_req=PaymentAccountReq2(
                account_type=AccountType12Enum.CHECKING,
                card_acquisition_reference=TransactionIDType(
                    transaction_id='TransactionID8',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
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
                )
            ),
            loyalty_account_req=LoyaltyAccountReq2(
                card_acquisition_reference=TransactionIDType(
                    transaction_id='TransactionID8',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                loyalty_account_id=LoyaltyAccountID(
                    entry_mode=[
                        EntryModeEnum.FILE
                    ],
                    identification_type=IdentificationType11Enum.ISOTRACK2,
                    loyalty_id='LoyaltyID4',
                    identification_support=IdentificationSupport1Enum.HYBRIDCARD
                )
            )
        ),
        card_acquisition_request=CardAcquisitionRequest2(
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
        ),
        admin_request=AdminRequest2(
            service_identification='ServiceIdentification0'
        ),
        diagnosis_request=DiagnosisRequest2(
            poiid='POIID2',
            host_diagnosis_flag=False,
            acquirer_id=[
                48,
                49,
                50
            ]
        )
    )
)
```

