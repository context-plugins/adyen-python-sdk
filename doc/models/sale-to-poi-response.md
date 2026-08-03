
# Sale to Poi Response

The SaleToPOIResponse message pair is a container for the response message content. It contains a MessageHeader and a message body.

*This model accepts additional fields of type Any.*

## Structure

`SaleToPoiResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_header` | [`MessageHeader1`](../../doc/models/message-header-1.md) | Required | - |
| `balance_inquiry_response` | [`BalanceInquiryResponse3`](../../doc/models/balance-inquiry-response-3.md) | Optional | - |
| `card_acquisition_response` | [`CardAcquisitionResponse1`](../../doc/models/card-acquisition-response-1.md) | Optional | - |
| `admin_response` | [`AdminResponse3`](../../doc/models/admin-response-3.md) | Optional | - |
| `diagnosis_response` | [`DiagnosisResponse3`](../../doc/models/diagnosis-response-3.md) | Optional | - |
| `display_response` | [`DisplayResponse3`](../../doc/models/display-response-3.md) | Optional | - |
| `enable_service_response` | [`EnableServiceResponse3`](../../doc/models/enable-service-response-3.md) | Optional | - |
| `get_totals_response` | [`GetTotalsResponse3`](../../doc/models/get-totals-response-3.md) | Optional | - |
| `input_response` | [`InputResponse3`](../../doc/models/input-response-3.md) | Optional | - |
| `login_response` | [`LoginResponse3`](../../doc/models/login-response-3.md) | Optional | - |
| `logout_response` | [`LogoutResponse3`](../../doc/models/logout-response-3.md) | Optional | - |
| `loyalty_response` | [`LoyaltyResponse1`](../../doc/models/loyalty-response-1.md) | Optional | - |
| `payment_response` | [`PaymentResponse5`](../../doc/models/payment-response-5.md) | Optional | - |
| `print_response` | [`PrintResponse3`](../../doc/models/print-response-3.md) | Optional | - |
| `card_reader_apdu_response` | [`CardReaderApduResponse1`](../../doc/models/card-reader-apdu-response-1.md) | Optional | - |
| `reconciliation_response` | [`ReconciliationResponse3`](../../doc/models/reconciliation-response-3.md) | Optional | - |
| `reversal_response` | [`ReversalResponse1`](../../doc/models/reversal-response-1.md) | Optional | - |
| `stored_value_response` | [`StoredValueResponse1`](../../doc/models/stored-value-response-1.md) | Optional | - |
| `transaction_status_response` | [`TransactionStatusResponse3`](../../doc/models/transaction-status-response-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.acquirer_transaction_id import AcquirerTransactionId
from adyen.models.admin_response_3 import AdminResponse3
from adyen.models.balance_inquiry_response_3 import BalanceInquiryResponse3
from adyen.models.card_acquisition_response_1 import CardAcquisitionResponse1
from adyen.models.card_data_2 import CardData2
from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.check_data_2 import CheckData2
from adyen.models.device_3 import Device3
from adyen.models.diagnosis_response_3 import DiagnosisResponse3
from adyen.models.display_response_3 import DisplayResponse3
from adyen.models.document_qualifier_1 import DocumentQualifier1
from adyen.models.entry_mode import EntryMode
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation import Geolocation
from adyen.models.global_status_1 import GlobalStatus1
from adyen.models.host_status import HostStatus
from adyen.models.identification_support_1 import IdentificationSupport1
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.info_qualify_3 import InfoQualify3
from adyen.models.loyalty_account import LoyaltyAccount
from adyen.models.loyalty_account_id_3 import LoyaltyAccountId3
from adyen.models.message_category_1 import MessageCategory1
from adyen.models.message_class_1 import MessageClass1
from adyen.models.message_header_1 import MessageHeader1
from adyen.models.message_type_1 import MessageType1
from adyen.models.mobile_data_2 import MobileData2
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_result import OutputResult
from adyen.models.output_text import OutputText
from adyen.models.payment_account_status import PaymentAccountStatus
from adyen.models.payment_acquirer_data_1 import PaymentAcquirerData1
from adyen.models.payment_instrument_data_2 import PaymentInstrumentData2
from adyen.models.payment_instrument_type_11 import PaymentInstrumentType11
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.poi_data_2 import PoiData2
from adyen.models.poi_status_2 import PoiStatus2
from adyen.models.poi_transaction_id import PoiTransactionId
from adyen.models.predefined_content_2 import PredefinedContent2
from adyen.models.printer_status_1 import PrinterStatus1
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11
from adyen.models.sale_data_2 import SaleData2
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.sale_to_poi_response import SaleToPoiResponse
from adyen.models.sale_transaction_id import SaleTransactionId
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1
from adyen.models.track_data_2 import TrackData2
from adyen.models.track_format_1 import TrackFormat1
from adyen.models.utm_coordinates import UtmCoordinates

sale_to_poi_response = SaleToPoiResponse(
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
    balance_inquiry_response=BalanceInquiryResponse3(
        response=Response3(
            result=Result11.PARTIAL,
            error_condition=ErrorCondition1.PAYMENTRESTRICTION,
            additional_response='AdditionalResponse8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        payment_account_status=PaymentAccountStatus(
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
            current_balance=83.4,
            currency='Currency4',
            payment_acquirer_data=PaymentAcquirerData1(
                merchant_id='MerchantID6',
                acquirer_poiid='AcquirerPOIID4',
                acquirer_id=238,
                acquirer_transaction_id=AcquirerTransactionId(
                    transaction_id='TransactionID2',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                approval_code='ApprovalCode8',
                host_reconciliation_id='HostReconciliationID8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        payment_receipt=[
            PaymentReceipt(
                document_qualifier=DocumentQualifier1.CUSTOMERRECEIPT,
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
                integrated_print_flag=False,
                required_signature_flag=False,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card_acquisition_response=CardAcquisitionResponse1(
        response=Response3(
            result=Result11.PARTIAL,
            error_condition=ErrorCondition1.PAYMENTRESTRICTION,
            additional_response='AdditionalResponse8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
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
        poi_data=PoiData2(
            poi_transaction_id=PoiTransactionId(
                transaction_id='TransactionID2',
                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            poi_reconciliation_id=52,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        payment_brand=[
            'PaymentBrand1',
            'PaymentBrand2',
            'PaymentBrand3'
        ],
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
        loyalty_account=[
            LoyaltyAccount(
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
                loyalty_brand='LoyaltyBrand0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    admin_response=AdminResponse3(
        response=Response3(
            result=Result11.PARTIAL,
            error_condition=ErrorCondition1.PAYMENTRESTRICTION,
            additional_response='AdditionalResponse8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    diagnosis_response=DiagnosisResponse3(
        response=Response3(
            result=Result11.PARTIAL,
            error_condition=ErrorCondition1.PAYMENTRESTRICTION,
            additional_response='AdditionalResponse8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        poi_status=PoiStatus2(
            global_status=GlobalStatus1.MAINTENANCE,
            security_ok_flag=False,
            pedok_flag=False,
            card_reader_ok_flag=False,
            printer_status=PrinterStatus1.PAPERLOW,
            communication_ok_flag=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        host_status=[
            HostStatus(
                acquirer_id=120,
                is_reachable_flag=False,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            HostStatus(
                acquirer_id=120,
                is_reachable_flag=False,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    display_response=DisplayResponse3(
        output_result=[
            OutputResult(
                device=Device3.CASHIERINPUT,
                info_qualify=InfoQualify3.DOCUMENT,
                response=Response3(
                    result=Result11.PARTIAL,
                    error_condition=ErrorCondition1.PAYMENTRESTRICTION,
                    additional_response='AdditionalResponse8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            OutputResult(
                device=Device3.CASHIERINPUT,
                info_qualify=InfoQualify3.DOCUMENT,
                response=Response3(
                    result=Result11.PARTIAL,
                    error_condition=ErrorCondition1.PAYMENTRESTRICTION,
                    additional_response='AdditionalResponse8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            OutputResult(
                device=Device3.CASHIERINPUT,
                info_qualify=InfoQualify3.DOCUMENT,
                response=Response3(
                    result=Result11.PARTIAL,
                    error_condition=ErrorCondition1.PAYMENTRESTRICTION,
                    additional_response='AdditionalResponse8',
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

