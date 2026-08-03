
# Transaction Status Response 2

Content of the TransactionStatus Response message.

*This model accepts additional fields of type Any.*

## Structure

`TransactionStatusResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `message_reference` | [`MessageReference1`](../../doc/models/message-reference-1.md) | Optional | - |
| `repeated_message_response` | [`RepeatedMessageResponse`](../../doc/models/repeated-message-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amounts_resp import AmountsResp
from adyen.models.card_acquisition_response_1 import CardAcquisitionResponse1
from adyen.models.card_data_2 import CardData2
from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.check_data_2 import CheckData2
from adyen.models.converted_amount import ConvertedAmount
from adyen.models.currency_conversion import CurrencyConversion
from adyen.models.document_qualifier_1 import DocumentQualifier1
from adyen.models.entry_mode import EntryMode
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation import Geolocation
from adyen.models.identification_support_1 import IdentificationSupport1
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.instalment import Instalment
from adyen.models.instalment_type import InstalmentType
from adyen.models.loyalty_account import LoyaltyAccount
from adyen.models.loyalty_account_12 import LoyaltyAccount12
from adyen.models.loyalty_account_id_3 import LoyaltyAccountId3
from adyen.models.loyalty_acquirer_data import LoyaltyAcquirerData
from adyen.models.loyalty_response_1 import LoyaltyResponse1
from adyen.models.loyalty_result import LoyaltyResult
from adyen.models.loyalty_transaction_id import LoyaltyTransactionId
from adyen.models.message_category_1 import MessageCategory1
from adyen.models.message_category_2 import MessageCategory2
from adyen.models.message_class_1 import MessageClass1
from adyen.models.message_header_1 import MessageHeader1
from adyen.models.message_reference_1 import MessageReference1
from adyen.models.message_type_1 import MessageType1
from adyen.models.mobile_data_2 import MobileData2
from adyen.models.original_poi_transaction_3 import OriginalPoiTransaction3
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_text import OutputText
from adyen.models.payment_instrument_data_2 import PaymentInstrumentData2
from adyen.models.payment_instrument_type_11 import PaymentInstrumentType11
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.payment_response_5 import PaymentResponse5
from adyen.models.payment_result_1 import PaymentResult1
from adyen.models.payment_type_1 import PaymentType1
from adyen.models.period_unit_1 import PeriodUnit1
from adyen.models.poi_data_2 import PoiData2
from adyen.models.poi_transaction_id import PoiTransactionId
from adyen.models.predefined_content_2 import PredefinedContent2
from adyen.models.repeated_message_response import RepeatedMessageResponse
from adyen.models.repeated_response_message_body import RepeatedResponseMessageBody
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11
from adyen.models.reversal_response_1 import ReversalResponse1
from adyen.models.sale_data_2 import SaleData2
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.sale_transaction_id import SaleTransactionId
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_status import StoredValueAccountStatus
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1
from adyen.models.stored_value_response_1 import StoredValueResponse1
from adyen.models.stored_value_result import StoredValueResult
from adyen.models.stored_value_transaction_type_2 import StoredValueTransactionType2
from adyen.models.track_data_2 import TrackData2
from adyen.models.track_format_1 import TrackFormat1
from adyen.models.transaction_status_response_2 import TransactionStatusResponse2
from adyen.models.utm_coordinates import UtmCoordinates

transaction_status_response_2 = TransactionStatusResponse2(
    response=Response3(
        result=Result11.PARTIAL,
        error_condition=ErrorCondition1.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
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
    repeated_message_response=RepeatedMessageResponse(
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
        repeated_response_message_body=RepeatedResponseMessageBody(
            loyalty_response=LoyaltyResponse1(
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
                loyalty_result=[
                    LoyaltyResult(
                        loyalty_account=LoyaltyAccount12(
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
                        ),
                        current_balance=171.12,
                        loyalty_acquirer_data=LoyaltyAcquirerData(
                            loyalty_acquirer_id='LoyaltyAcquirerID4',
                            approval_code='ApprovalCode4',
                            loyalty_transaction_id=LoyaltyTransactionId(
                                transaction_id='TransactionID6',
                                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            host_reconciliation_id='HostReconciliationID4',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    LoyaltyResult(
                        loyalty_account=LoyaltyAccount12(
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
                        ),
                        current_balance=171.12,
                        loyalty_acquirer_data=LoyaltyAcquirerData(
                            loyalty_acquirer_id='LoyaltyAcquirerID4',
                            approval_code='ApprovalCode4',
                            loyalty_transaction_id=LoyaltyTransactionId(
                                transaction_id='TransactionID6',
                                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            host_reconciliation_id='HostReconciliationID4',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
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
                    ),
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
                    ),
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
            payment_response=PaymentResponse5(
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
                payment_result=PaymentResult1(
                    payment_type=PaymentType1.ISSUERINSTALMENT,
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
                    amounts_resp=AmountsResp(
                        authorized_amount=133.28,
                        currency='Currency0',
                        total_rebates_amount=120.04,
                        total_fees_amount=181.08,
                        cash_back_amount=206.58,
                        tip_amount=86.96,
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
                    currency_conversion=[
                        CurrencyConversion(
                            converted_amount=ConvertedAmount(
                                amount_value=81.82,
                                currency='Currency0',
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            customer_approved_flag=False,
                            rate=175.8,
                            markup=100.86,
                            commission=197.78,
                            declaration='Declaration4',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        CurrencyConversion(
                            converted_amount=ConvertedAmount(
                                amount_value=81.82,
                                currency='Currency0',
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            customer_approved_flag=False,
                            rate=175.8,
                            markup=100.86,
                            commission=197.78,
                            declaration='Declaration4',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        )
                    ],
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                loyalty_result=[
                    LoyaltyResult(
                        loyalty_account=LoyaltyAccount12(
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
                        ),
                        current_balance=171.12,
                        loyalty_acquirer_data=LoyaltyAcquirerData(
                            loyalty_acquirer_id='LoyaltyAcquirerID4',
                            approval_code='ApprovalCode4',
                            loyalty_transaction_id=LoyaltyTransactionId(
                                transaction_id='TransactionID6',
                                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            host_reconciliation_id='HostReconciliationID4',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    LoyaltyResult(
                        loyalty_account=LoyaltyAccount12(
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
                        ),
                        current_balance=171.12,
                        loyalty_acquirer_data=LoyaltyAcquirerData(
                            loyalty_acquirer_id='LoyaltyAcquirerID4',
                            approval_code='ApprovalCode4',
                            loyalty_transaction_id=LoyaltyTransactionId(
                                transaction_id='TransactionID6',
                                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            host_reconciliation_id='HostReconciliationID4',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    LoyaltyResult(
                        loyalty_account=LoyaltyAccount12(
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
                        ),
                        current_balance=171.12,
                        loyalty_acquirer_data=LoyaltyAcquirerData(
                            loyalty_acquirer_id='LoyaltyAcquirerID4',
                            approval_code='ApprovalCode4',
                            loyalty_transaction_id=LoyaltyTransactionId(
                                transaction_id='TransactionID6',
                                time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            host_reconciliation_id='HostReconciliationID4',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
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
            reversal_response=ReversalResponse1(
                response=Response3(
                    result=Result11.PARTIAL,
                    error_condition=ErrorCondition1.PAYMENTRESTRICTION,
                    additional_response='AdditionalResponse8',
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
                reversed_amount=90.36,
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
                    ),
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
            stored_value_response=StoredValueResponse1(
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
                stored_value_result=[
                    StoredValueResult(
                        stored_value_transaction_type=StoredValueTransactionType2.REVERSE,
                        product_code=20,
                        ean_upc=136,
                        item_amount=5.58,
                        currency='Currency2',
                        stored_value_account_status=StoredValueAccountStatus(
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
                            current_balance=45.56,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    StoredValueResult(
                        stored_value_transaction_type=StoredValueTransactionType2.REVERSE,
                        product_code=20,
                        ean_upc=136,
                        item_amount=5.58,
                        currency='Currency2',
                        stored_value_account_status=StoredValueAccountStatus(
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
                            current_balance=45.56,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    StoredValueResult(
                        stored_value_transaction_type=StoredValueTransactionType2.REVERSE,
                        product_code=20,
                        ean_upc=136,
                        item_amount=5.58,
                        currency='Currency2',
                        stored_value_account_status=StoredValueAccountStatus(
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
                            current_balance=45.56,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
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
)
```

