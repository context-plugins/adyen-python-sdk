
# Print Request 2

Content of the Print Request message.

*This model accepts additional fields of type Any.*

## Structure

`PrintRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `print_output` | [`PrintOutput`](../../doc/models/print-output.md) | Required | - |
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
from adyen.models.print_output import PrintOutput
from adyen.models.print_request_2 import PrintRequest2
from adyen.models.response_mode_1 import ResponseMode1

print_request_2 = PrintRequest2(
    print_output=PrintOutput(
        document_qualifier=DocumentQualifier2.CUSTOMERRECEIPT,
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

