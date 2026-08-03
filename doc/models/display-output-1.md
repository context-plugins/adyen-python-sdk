
# Display Output 1

Information to display and the way to process the display.
To display an abort message to the Customer.

*This model accepts additional fields of type Any.*

## Structure

`DisplayOutput1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_required_flag` | `bool` | Optional | Indicates if the message response is required.<br><br>**Default**: `True` |
| `minimum_display_time` | `int` | Optional | Number of seconds the message has to be displayed.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0`, `<= 999` |
| `device` | [`Device11`](../../doc/models/device-11.md) | Required | - |
| `info_qualify` | [`InfoQualify1`](../../doc/models/info-qualify-1.md) | Required | - |
| `output_content` | [`OutputContent2`](../../doc/models/output-content-2.md) | Required | - |
| `menu_entry` | [`List[MenuEntry]`](../../doc/models/menu-entry.md) | Optional | An entry of the menu to present to the Cashier. It conveys the message text and parameters of the menu entry. This output data could be only provided for an input command, in order to choose an entryof the menu. |
| `output_signature` | `str` | Optional | Vendor-specific signature of the text message to display or print.<br>If protection has to be provided to the vendor on the text to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.device_11 import Device11
from adyen.models.display_output_1 import DisplayOutput1
from adyen.models.info_qualify_1 import InfoQualify1
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1 import MenuEntryTag1
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_format_2 import OutputFormat2
from adyen.models.output_text import OutputText
from adyen.models.predefined_content_2 import PredefinedContent2

display_output_1 = DisplayOutput1(
    device=Device11.CASHIERINPUT,
    info_qualify=InfoQualify1.DISPLAY,
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
    response_required_flag=True,
    minimum_display_time=0,
    menu_entry=[
        MenuEntry(
            output_format=OutputFormat2.XHTML,
            menu_entry_tag=MenuEntryTag1.SUBMENU,
            default_selected_flag=False,
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
                ),
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
            output_xhtml='OutputXHTML8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        MenuEntry(
            output_format=OutputFormat2.XHTML,
            menu_entry_tag=MenuEntryTag1.SUBMENU,
            default_selected_flag=False,
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
                ),
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
            output_xhtml='OutputXHTML8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        MenuEntry(
            output_format=OutputFormat2.XHTML,
            menu_entry_tag=MenuEntryTag1.SUBMENU,
            default_selected_flag=False,
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
                ),
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
            output_xhtml='OutputXHTML8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    output_signature='OutputSignature2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

