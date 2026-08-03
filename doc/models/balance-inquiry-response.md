
# Balance Inquiry Response

Content of the Balance Inquiry Response message.
It conveys the balance and the identification of the associated payment, loyalty or stored value account.

*This model accepts additional fields of type Any.*

## Structure

`BalanceInquiryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `payment_account_status` | [`PaymentAccountStatus`](../../doc/models/payment-account-status.md) | Optional | - |
| `payment_receipt` | [`List[PaymentReceipt]`](../../doc/models/payment-receipt.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.acquirer_transaction_id import AcquirerTransactionId
from adyen.models.balance_inquiry_response import BalanceInquiryResponse
from adyen.models.card_data_2 import CardData2
from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.check_data_2 import CheckData2
from adyen.models.document_qualifier_1 import DocumentQualifier1
from adyen.models.entry_mode import EntryMode
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation import Geolocation
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.mobile_data_2 import MobileData2
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_text import OutputText
from adyen.models.payment_account_status import PaymentAccountStatus
from adyen.models.payment_acquirer_data_1 import PaymentAcquirerData1
from adyen.models.payment_instrument_data_2 import PaymentInstrumentData2
from adyen.models.payment_instrument_type_11 import PaymentInstrumentType11
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.predefined_content_2 import PredefinedContent2
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1
from adyen.models.track_data_2 import TrackData2
from adyen.models.track_format_1 import TrackFormat1
from adyen.models.utm_coordinates import UtmCoordinates

balance_inquiry_response = BalanceInquiryResponse(
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
)
```

