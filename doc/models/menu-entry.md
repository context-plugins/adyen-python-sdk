
# Menu Entry

An entry of the menu to present to the Cashier.
It conveys message text and parameters of the menu entry. This output data could be only provided for an input command, in order to choose an entry of the menu.

*This model accepts additional fields of type Any.*

## Structure

`MenuEntry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `menu_entry_tag` | [`MenuEntryTag1`](../../doc/models/menu-entry-tag-1.md) | Optional | - |
| `default_selected_flag` | `bool` | Optional | Selection of a menu entry to be displayed. In Input request message, it allows selection of one or several menu entries before any user action.<br><br>**Default**: `False` |
| `output_format` | [`OutputFormat2`](../../doc/models/output-format-2.md) | Required | - |
| `predefined_content` | [`PredefinedContent2`](../../doc/models/predefined-content-2.md) | Optional | - |
| `output_text` | [`List[OutputText]`](../../doc/models/output-text.md) | Optional | Content of text message to display or print. It conveys Information related to the content of the text message and its format. All the data elements related to the format of the text to display or print are parameters valid for the whole Text content. |
| `output_xhtml` | `str` | Optional | XHTML document body containing the message to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1 import MenuEntryTag1
from adyen.models.output_format_2 import OutputFormat2
from adyen.models.output_text import OutputText
from adyen.models.predefined_content_2 import PredefinedContent2

menu_entry = MenuEntry(
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
    output_xhtml='OutputXHTML2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

