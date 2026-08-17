
# Print Request 2

Content of the Print Request message.

## Structure

`PrintRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `print_output` | [`PrintOutput2`](../../doc/models/print-output-2.md) | Required | Information to print and how to process it. |

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
from adyen.models.print_request_2 import PrintRequest2
from adyen.models.response_mode_1_enum import ResponseMode1Enum

print_request_2 = PrintRequest2(
    print_output=PrintOutput2(
        document_qualifier=DocumentQualifier2Enum.CUSTOMERRECEIPT,
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
)
```

