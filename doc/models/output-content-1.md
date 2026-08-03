
# Output Content 1

Content to display or print.

*This model accepts additional fields of type Any.*

## Structure

`OutputContent1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `output_format` | [`OutputFormat1`](../../doc/models/output-format-1.md) | Required | - |
| `predefined_content` | [`PredefinedContent2`](../../doc/models/predefined-content-2.md) | Optional | - |
| `output_text` | [`List[OutputText]`](../../doc/models/output-text.md) | Optional | Content of text message to display or print.<br>Mandatory, if `OutputFormat` is Text, not allowed otherwise. One instance of `OutputText` per shared format. |
| `output_xhtml` | `str` | Optional | XHTML document body containing the message to display or print.<br>Mandatory if `OutputFormat` is XHTML, not allowed otherwise.<br><br>**Constraints**: *Pattern*: `^.{0,262144}$` |
| `output_barcode` | [`OutputBarcode`](../../doc/models/output-barcode.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_text import OutputText
from adyen.models.predefined_content_2 import PredefinedContent2

output_content_1 = OutputContent1(
    output_format=OutputFormat1.MESSAGEREF,
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
)
```

