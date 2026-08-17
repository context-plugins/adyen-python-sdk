
# Reversal Response

It conveys Information related to the reversal processed by the POI System.
Content of the Reversal Response message.

## Structure

`ReversalResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |
| `poi_data` | [`POIData4`](../../doc/models/poi-data-4.md) | Optional | Data related to the POI System.<br>If Result is Success. |
| `original_poi_transaction` | [`OriginalPOITransaction`](../../doc/models/original-poi-transaction.md) | Optional | Identification of a previous POI transaction.<br>In the Payment Request message, it allows using the card of a previous CardAcquisition or Payment request. |
| `reversed_amount` | `float` | Optional | Amount of the payment or loyalty to reverse.<br>Copy.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `payment_receipt` | [`List[PaymentReceipt]`](../../doc/models/payment-receipt.md) | Optional | - |

## Example

```python
import dateutil.parser

from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.document_qualifier_1_enum import DocumentQualifier1Enum
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.original_poi_transaction import OriginalPOITransaction
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_text import OutputText
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.poi_data_4 import POIData4
from adyen.models.predefined_content_1 import PredefinedContent1
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum
from adyen.models.reversal_response import ReversalResponse
from adyen.models.transaction_id_type_2 import TransactionIDType2
from adyen.models.transaction_id_type_4 import TransactionIDType4

reversal_response = ReversalResponse(
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
    reversed_amount=57.02,
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

