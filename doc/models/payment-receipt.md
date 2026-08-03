
# Payment Receipt

Customer or Merchant payment receipt.
If the payment receipts are printed by the Sale system and the POI or the Sale does not implement the Print exchange (Basic profile).

*This model accepts additional fields of type Any.*

## Structure

`PaymentReceipt`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_qualifier` | [`DocumentQualifier1`](../../doc/models/document-qualifier-1.md) | Required | - |
| `integrated_print_flag` | `bool` | Optional | Type of the print integrated to other prints. |
| `required_signature_flag` | `bool` | Optional | Indicate that the cardholder payment receipt requires a physical signature by the Customer.<br><br>**Default**: `False` |
| `output_content` | [`OutputContent2`](../../doc/models/output-content-2.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.document_qualifier_1 import DocumentQualifier1
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_text import OutputText
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.predefined_content_2 import PredefinedContent2

payment_receipt = PaymentReceipt(
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
```

