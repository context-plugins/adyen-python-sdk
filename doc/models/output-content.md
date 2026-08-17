
# Output Content

Content to display or print.
This is a sequence of elements if they have different formats.

## Structure

`OutputContent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `output_format` | [`OutputFormat1Enum`](../../doc/models/output-format-1-enum.md) | Required | Format of the content to display or print.<br>Possible values:<br><br>* **BarCode**<br>* **MessageRef**<br>* **Text**<br>* **XHTML** |
| `predefined_content` | [`PredefinedContent1`](../../doc/models/predefined-content-1.md) | Optional | Reference of a predefined message to display or print.<br>Mandatory, if `OutputFormat` is MessageRef, not allowed otherwise. |
| `output_text` | [`List[OutputText]`](../../doc/models/output-text.md) | Optional | Content of text message to display or print.<br>Mandatory, if `OutputFormat` is Text, not allowed otherwise. One instance of `OutputText` per shared format. |
| `output_xhtml` | `str` | Optional | XHTML document body containing the message to display or print.<br>Mandatory if `OutputFormat` is XHTML, not allowed otherwise.<br><br>**Constraints**: *Pattern*: `^.{0,262144}$` |
| `output_barcode` | [`OutputBarcode1`](../../doc/models/output-barcode-1.md) | Optional | Barcode content to display or print.<br>Mandatory if `OutputFormat` is Barcode, not allowed otherwise. |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content import OutputContent
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_text import OutputText
from adyen.models.predefined_content_1 import PredefinedContent1

output_content = OutputContent(
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
        ),
        OutputText(
            text='Text6',
            character_set=194,
            start_row=74,
            start_column=220,
            character_width=CharacterWidth1Enum.SINGLEWIDTH,
            character_height=CharacterHeight1Enum.SINGLEHEIGHT
        ),
        OutputText(
            text='Text6',
            character_set=194,
            start_row=74,
            start_column=220,
            character_width=CharacterWidth1Enum.SINGLEWIDTH,
            character_height=CharacterHeight1Enum.SINGLEHEIGHT
        )
    ],
    output_xhtml='OutputXHTML6',
    output_barcode=OutputBarcode1(
        barcode_value='BarcodeValue2'
    )
)
```

