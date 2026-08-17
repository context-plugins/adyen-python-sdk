
# Input Update

Definition: Content of the Input Update message. : It conveys
update of the display of an Input request in progress.

## Structure

`InputUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_reference` | [`MessageReference`](../../doc/models/message-reference.md) | Required | Identification of a previous POI transaction.<br>To abort a transaction in progress or to request the status of a transaction from which no response has been received. It identifies the message header of the message request to abort or request the status. |
| `output_content` | [`OutputContent`](../../doc/models/output-content.md) | Required | Content to display or print.<br>This is a sequence of elements if they have different formats. |
| `menu_entry` | [`List[MenuEntry]`](../../doc/models/menu-entry.md) | Optional | - |
| `output_signature` | `str` | Optional | **Constraints**: *Pattern*: `^.+$` |
| `min_length` | `int` | Optional | - |
| `max_length` | `int` | Optional | - |
| `max_decimal_length` | `int` | Optional | - |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.input_update import InputUpdate
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1_enum import MenuEntryTag1Enum
from adyen.models.message_category_2_enum import MessageCategory2Enum
from adyen.models.message_reference import MessageReference
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content import OutputContent
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_format_2_enum import OutputFormat2Enum
from adyen.models.output_text import OutputText
from adyen.models.predefined_content import PredefinedContent
from adyen.models.predefined_content_1 import PredefinedContent1

input_update = InputUpdate(
    message_reference=MessageReference(
        message_category=MessageCategory2Enum.PAYMENT,
        service_id='ServiceID0',
        device_id='DeviceID2',
        sale_id='SaleID8',
        poiid='POIID2'
    ),
    output_content=OutputContent(
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
    menu_entry=[
        MenuEntry(
            output_format=OutputFormat2Enum.XHTML,
            menu_entry_tag=MenuEntryTag1Enum.SUBMENU,
            default_selected_flag=False,
            predefined_content=PredefinedContent(
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
                )
            ],
            output_xhtml='OutputXHTML8'
        )
    ],
    output_signature='OutputSignature2',
    min_length=166,
    max_length=190,
    max_decimal_length=198
)
```

