
# Print Output 2

Information to print and how to process it.

## Structure

`PrintOutput2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_qualifier` | [`DocumentQualifier2Enum`](../../doc/models/document-qualifier-2-enum.md) | Required | Qualification of the document to print to the Cashier or the Customer. Allows the manager of the printer, Sale or POI Terminal, to send information to a physical printer or to use the paper type accordingly.<br>Possible values:<br><br>* **CashierReceipt**<br>* **CustomerReceipt**<br>* **Document**<br>* **Journal**<br>* **SaleReceipt**<br>* **Voucher** |
| `response_mode` | [`ResponseMode1Enum`](../../doc/models/response-mode-1-enum.md) | Required | Message response awaited by the initiator of the Request. Allows various types and synchronisation of requests for Print or Sound.<br>Possible values:<br><br>* **Immediate**<br>* **NotRequired**<br>* **PrintEnd**<br>* **SoundEnd** |
| `integrated_print_flag` | `bool` | Optional | Type of the print integrated in other prints. Allows a separated printing (paper cut if available), or integration with the sale receipt or other print. If the printing is integrated, the response is always immediate, even if the `ResponseMode` is set to `PrintEnd`.<br><br>**Default**: `False` |
| `required_signature_flag` | `bool` | Optional | Indicates that the cardholder payment receipt requires a physical signature by the Customer.<br><br>**Default**: `False` |
| `output_content` | [`OutputContent3`](../../doc/models/output-content-3.md) | Required | Content to display or print. This is a sequence of elements if they have different formats. |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.document_qualifier_2_enum import DocumentQualifier2Enum
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_3 import OutputContent3
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_text import OutputText
from adyen.models.predefined_content_1 import PredefinedContent1
from adyen.models.print_output_2 import PrintOutput2
from adyen.models.response_mode_1_enum import ResponseMode1Enum

print_output_2 = PrintOutput2(
    document_qualifier=DocumentQualifier2Enum.VOUCHER,
    response_mode=ResponseMode1Enum.PRINTEND,
    output_content=OutputContent3(
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
```

