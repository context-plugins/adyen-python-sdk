
# Print Output 2

Information to print and how to process it.

*This model accepts additional fields of type Any.*

## Structure

`PrintOutput2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_qualifier` | [`DocumentQualifier2`](../../doc/models/document-qualifier-2.md) | Required | - |
| `response_mode` | [`ResponseMode1`](../../doc/models/response-mode-1.md) | Required | - |
| `integrated_print_flag` | `bool` | Optional | Type of the print integrated in other prints. Allows a separated printing (paper cut if available), or integration with the sale receipt or other print. If the printing is integrated, the response is always immediate, even if the `ResponseMode` is set to `PrintEnd`.<br><br>**Default**: `False` |
| `required_signature_flag` | `bool` | Optional | Indicates that the cardholder payment receipt requires a physical signature by the Customer.<br><br>**Default**: `False` |
| `output_content` | [`OutputContent2`](../../doc/models/output-content-2.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.document_qualifier_2 import DocumentQualifier2
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_text import OutputText
from adyen.models.predefined_content_2 import PredefinedContent2
from adyen.models.print_output_2 import PrintOutput2
from adyen.models.response_mode_1 import ResponseMode1

print_output_2 = PrintOutput2(
    document_qualifier=DocumentQualifier2.VOUCHER,
    response_mode=ResponseMode1.PRINTEND,
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

