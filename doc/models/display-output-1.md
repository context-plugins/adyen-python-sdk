
# Display Output 1

Information to display and the way to process the display.
To display an abort message to the Customer.

## Structure

`DisplayOutput1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_required_flag` | `bool` | Optional | Indicates if the message response is required.<br><br>**Default**: `True` |
| `minimum_display_time` | `int` | Optional | Number of seconds the message has to be displayed.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0`, `<= 999` |
| `device` | [`Device11Enum`](../../doc/models/device-11-enum.md) | Required | Logical device located on a Sale Terminal or a POI Terminal, in terms of class of information to output (display, print, or store), or input (keyboard) for the Cashier or the Customer.<br>Possible values:<br><br>* **CashierDisplay**<br>* **CashierInput**<br>* **CustomerDisplay**<br>* **CustomerInput** |
| `info_qualify` | [`InfoQualify1Enum`](../../doc/models/info-qualify-1-enum.md) | Required | Qualification of the information to sent to an output logical device, to display or print to the Cashier or the Customer. Allows the manager of the device, Sale or POI Terminal, to send the information to a particular physical device or to present the information accordingly.<br>Possible values:<br><br>* **CustomerAssistance**<br>* **Display**<br>* **Document**<br>* **Error**<br>* **Input**<br>* **POIReplication**<br>* **Receipt**<br>* **Sound**<br>* **Status**<br>* **Voucher** |
| `output_content` | [`OutputContent1`](../../doc/models/output-content-1.md) | Required | Content to display or print. |
| `menu_entry` | [`List[MenuEntry]`](../../doc/models/menu-entry.md) | Optional | An entry of the menu to present to the Cashier. It conveys the message text and parameters of the menu entry. This output data could be only provided for an input command, in order to choose an entryof the menu. |
| `output_signature` | `str` | Optional | Vendor-specific signature of the text message to display or print.<br>If protection has to be provided to the vendor on the text to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.device_11_enum import Device11Enum
from adyen.models.display_output_1 import DisplayOutput1
from adyen.models.info_qualify_1_enum import InfoQualify1Enum
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1_enum import MenuEntryTag1Enum
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_format_2_enum import OutputFormat2Enum
from adyen.models.output_text import OutputText
from adyen.models.predefined_content import PredefinedContent
from adyen.models.predefined_content_1 import PredefinedContent1

display_output_1 = DisplayOutput1(
    device=Device11Enum.CASHIERINPUT,
    info_qualify=InfoQualify1Enum.DISPLAY,
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
    response_required_flag=True,
    minimum_display_time=0,
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
        ),
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
        ),
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
    output_signature='OutputSignature2'
)
```

