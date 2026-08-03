
# Loyalty Response 1

*This model accepts additional fields of type Any.*

## Structure

`LoyaltyResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `sale_data` | [`SaleData2`](../../doc/models/sale-data-2.md) | Required | - |
| `poi_data` | [`PoiData2`](../../doc/models/poi-data-2.md) | Required | - |
| `loyalty_result` | [`List[LoyaltyResult]`](../../doc/models/loyalty-result.md) | Optional | Data related to the result of a processed loyalty transaction.<br>If loyalty account identified. |
| `payment_receipt` | [`List[PaymentReceipt]`](../../doc/models/payment-receipt.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.document_qualifier_1 import DocumentQualifier1
from adyen.models.entry_mode import EntryMode
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.identification_support_1 import IdentificationSupport1
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.loyalty_account_12 import LoyaltyAccount12
from adyen.models.loyalty_account_id_3 import LoyaltyAccountId3
from adyen.models.loyalty_acquirer_data import LoyaltyAcquirerData
from adyen.models.loyalty_response_1 import LoyaltyResponse1
from adyen.models.loyalty_result import LoyaltyResult
from adyen.models.loyalty_transaction_id import LoyaltyTransactionId
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_text import OutputText
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.poi_data_2 import PoiData2
from adyen.models.poi_transaction_id import PoiTransactionId
from adyen.models.predefined_content_2 import PredefinedContent2
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11
from adyen.models.sale_data_2 import SaleData2
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.sale_transaction_id import SaleTransactionId

loyalty_response_1 = LoyaltyResponse1(
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
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

