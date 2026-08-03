
# Sale to Poi Request 2

*This model accepts additional fields of type Any.*

## Structure

`SaleToPoiRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_header` | [`MessageHeader1`](../../doc/models/message-header-1.md) | Required | - |
| `abort_request` | [`AbortRequest3`](../../doc/models/abort-request-3.md) | Optional | - |
| `balance_inquiry_request` | [`BalanceInquiryRequest3`](../../doc/models/balance-inquiry-request-3.md) | Optional | - |
| `card_acquisition_request` | [`CardAcquisitionRequest3`](../../doc/models/card-acquisition-request-3.md) | Optional | - |
| `admin_request` | [`AdminRequest3`](../../doc/models/admin-request-3.md) | Optional | - |
| `diagnosis_request` | [`DiagnosisRequest3`](../../doc/models/diagnosis-request-3.md) | Optional | - |
| `display_request` | [`DisplayRequest3`](../../doc/models/display-request-3.md) | Optional | - |
| `enable_service_request` | [`EnableServiceRequest3`](../../doc/models/enable-service-request-3.md) | Optional | - |
| `event_notification` | [`EventNotification3`](../../doc/models/event-notification-3.md) | Optional | - |
| `get_totals_request` | [`GetTotalsRequest3`](../../doc/models/get-totals-request-3.md) | Optional | - |
| `input_request` | [`InputRequest3`](../../doc/models/input-request-3.md) | Optional | - |
| `input_update` | [`InputUpdate3`](../../doc/models/input-update-3.md) | Optional | - |
| `login_request` | [`LoginRequest3`](../../doc/models/login-request-3.md) | Optional | - |
| `logout_request` | [`LogoutRequest3`](../../doc/models/logout-request-3.md) | Optional | - |
| `payment_request` | [`PaymentRequest22`](../../doc/models/payment-request-22.md) | Optional | - |
| `print_request` | [`PrintRequest3`](../../doc/models/print-request-3.md) | Optional | - |
| `card_reader_apdu_request` | [`CardReaderApduRequest3`](../../doc/models/card-reader-apdu-request-3.md) | Optional | - |
| `reconciliation_request` | [`ReconciliationRequest3`](../../doc/models/reconciliation-request-3.md) | Optional | - |
| `reversal_request` | [`ReversalRequest3`](../../doc/models/reversal-request-3.md) | Optional | - |
| `stored_value_request` | [`StoredValueRequest3`](../../doc/models/stored-value-request-3.md) | Optional | - |
| `transaction_status_request` | [`TransactionStatusRequest3`](../../doc/models/transaction-status-request-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.abort_request_3 import AbortRequest3
from adyen.models.account_type_13 import AccountType13
from adyen.models.admin_request_3 import AdminRequest3
from adyen.models.balance_inquiry_request_3 import BalanceInquiryRequest3
from adyen.models.card_acquisition_reference import CardAcquisitionReference
from adyen.models.card_acquisition_request_3 import CardAcquisitionRequest3
from adyen.models.card_acquisition_transaction import CardAcquisitionTransaction
from adyen.models.card_data_2 import CardData2
from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.check_data_2 import CheckData2
from adyen.models.device_11 import Device11
from adyen.models.diagnosis_request_3 import DiagnosisRequest3
from adyen.models.display_output_3 import DisplayOutput3
from adyen.models.entry_mode import EntryMode
from adyen.models.force_entry_mode import ForceEntryMode
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation import Geolocation
from adyen.models.identification_support_1 import IdentificationSupport1
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.info_qualify_1 import InfoQualify1
from adyen.models.loyalty_account_id_3 import LoyaltyAccountId3
from adyen.models.loyalty_account_req import LoyaltyAccountReq
from adyen.models.loyalty_handling_2 import LoyaltyHandling2
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1 import MenuEntryTag1
from adyen.models.message_category_1 import MessageCategory1
from adyen.models.message_category_2 import MessageCategory2
from adyen.models.message_class_1 import MessageClass1
from adyen.models.message_header_1 import MessageHeader1
from adyen.models.message_reference_1 import MessageReference1
from adyen.models.message_type_1 import MessageType1
from adyen.models.mobile_data_2 import MobileData2
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_format_2 import OutputFormat2
from adyen.models.output_text import OutputText
from adyen.models.payment_account_req import PaymentAccountReq
from adyen.models.payment_instrument_data_2 import PaymentInstrumentData2
from adyen.models.payment_instrument_type_11 import PaymentInstrumentType11
from adyen.models.predefined_content_2 import PredefinedContent2
from adyen.models.sale_data_2 import SaleData2
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.sale_to_poi_request_2 import SaleToPoiRequest2
from adyen.models.sale_transaction_id import SaleTransactionId
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1
from adyen.models.track_data_2 import TrackData2
from adyen.models.track_format_1 import TrackFormat1
from adyen.models.utm_coordinates import UtmCoordinates

sale_to_poi_request_2 = SaleToPoiRequest2(
    message_header=MessageHeader1(
        message_class=MessageClass1.SERVICE,
        message_category=MessageCategory1.STOREDVALUE,
        message_type=MessageType1.NOTIFICATION,
        sale_id='SaleID4',
        poiid='POIID0',
        protocol_version='ProtocolVersion2',
        service_id='ServiceID2',
        device_id='DeviceID4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    abort_request=AbortRequest3(
        message_reference=MessageReference1(
            message_category=MessageCategory2.PAYMENT,
            service_id='ServiceID0',
            device_id='DeviceID2',
            sale_id='SaleID8',
            poiid='POIID2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        abort_reason='AbortReason6',
        display_output=DisplayOutput3(
            device=Device11.CASHIERDISPLAY,
            info_qualify=InfoQualify1.STATUS,
            output_content=OutputContent2(
                output_format=OutputFormat1.XHTML,
                predefined_content=PredefinedContent2(
                    reference_id='ReferenceID0',
                    language='Language2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                output_text=[
                    OutputText(
                        text='Text6',
                        character_set=194,
                        start_row=74,
                        start_column=220,
                        character_width=CharacterWidth1.SINGLEWIDTH,
                        character_height=CharacterHeight1.SINGLEHEIGHT,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                output_xhtml='OutputXHTML2',
                output_barcode=OutputBarcode(
                    barcode_value='BarcodeValue2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            response_required_flag=False,
            minimum_display_time=110,
            menu_entry=[
                MenuEntry(
                    output_format=OutputFormat2.XHTML,
                    menu_entry_tag=MenuEntryTag1.SUBMENU,
                    default_selected_flag=False,
                    predefined_content=PredefinedContent2(
                        reference_id='ReferenceID0',
                        language='Language2',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    output_text=[
                        OutputText(
                            text='Text6',
                            character_set=194,
                            start_row=74,
                            start_column=220,
                            character_width=CharacterWidth1.SINGLEWIDTH,
                            character_height=CharacterHeight1.SINGLEHEIGHT,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        OutputText(
                            text='Text6',
                            character_set=194,
                            start_row=74,
                            start_column=220,
                            character_width=CharacterWidth1.SINGLEWIDTH,
                            character_height=CharacterHeight1.SINGLEHEIGHT,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        )
                    ],
                    output_xhtml='OutputXHTML8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                MenuEntry(
                    output_format=OutputFormat2.XHTML,
                    menu_entry_tag=MenuEntryTag1.SUBMENU,
                    default_selected_flag=False,
                    predefined_content=PredefinedContent2(
                        reference_id='ReferenceID0',
                        language='Language2',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    output_text=[
                        OutputText(
                            text='Text6',
                            character_set=194,
                            start_row=74,
                            start_column=220,
                            character_width=CharacterWidth1.SINGLEWIDTH,
                            character_height=CharacterHeight1.SINGLEHEIGHT,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        OutputText(
                            text='Text6',
                            character_set=194,
                            start_row=74,
                            start_column=220,
                            character_width=CharacterWidth1.SINGLEWIDTH,
                            character_height=CharacterHeight1.SINGLEHEIGHT,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        )
                    ],
                    output_xhtml='OutputXHTML8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            output_signature='OutputSignature4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    balance_inquiry_request=BalanceInquiryRequest3(
        payment_account_req=PaymentAccountReq(
            account_type=AccountType13.CHECKING,
            card_acquisition_reference=CardAcquisitionReference(
                transaction_id='TransactionID8',
                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            payment_instrument_data=PaymentInstrumentData2(
                payment_instrument_type=PaymentInstrumentType11.CASH,
                protected_card_data='ProtectedCardData8',
                card_data=CardData2(
                    payment_brand='PaymentBrand0',
                    masked_pan='MaskedPan0',
                    payment_account_ref='PaymentAccountRef8',
                    entry_mode=[
                        EntryMode.MANUAL,
                        EntryMode.KEYED
                    ],
                    card_country_code=3,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                check_data=CheckData2(
                    bank_id='BankID0',
                    account_number='AccountNumber6',
                    check_number='CheckNumber2',
                    track_data=TrackData2(
                        track_value='TrackValue6',
                        track_numb=3,
                        track_format=TrackFormat1.JISII,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    check_card_number='CheckCardNumber6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                mobile_data=MobileData2(
                    mobile_country_code=3,
                    mobile_network_code=3,
                    masked_msisdn=22,
                    geolocation=Geolocation(
                        geographic_coordinates=GeographicCoordinates(
                            latitude='Latitude4',
                            longitude='Longitude2',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        utm_coordinates=UtmCoordinates(
                            utm_zone='UTMZone6',
                            utm_eastward='UTMEastward0',
                            utm_northward='UTMNorthward0',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    protected_mobile_data='ProtectedMobileData0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                stored_value_account_id=StoredValueAccountId2(
                    stored_value_account_type=StoredValueAccountType1.PHONECARD,
                    entry_mode=[
                        EntryMode.MAGSTRIPE,
                        EntryMode.SCANNED
                    ],
                    identification_type=IdentificationType11.PHONENUMBER,
                    stored_value_id='StoredValueID8',
                    stored_value_provider='StoredValueProvider4',
                    owner_name='OwnerName0',
                    expiry_date=4,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        loyalty_account_req=LoyaltyAccountReq(
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
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card_acquisition_request=CardAcquisitionRequest3(
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
    ),
    admin_request=AdminRequest3(
        service_identification='ServiceIdentification0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    diagnosis_request=DiagnosisRequest3(
        poiid='POIID2',
        host_diagnosis_flag=False,
        acquirer_id=[
            48,
            49,
            50
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

