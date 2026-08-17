
# Menu Entry

An entry of the menu to present to the Cashier.
It conveys message text and parameters of the menu entry. This output data could be only provided for an input command, in order to choose an entry of the menu.

## Structure

`MenuEntry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `menu_entry_tag` | [`MenuEntryTag1Enum`](../../doc/models/menu-entry-tag-1-enum.md) | Optional | Characteristics related to the selection of a menu entry.<br>Possible values:<br><br>* **NonSelectable**<br>* **NonSelectableSubMenu**<br>* **Selectable**<br>* **SubMenu** |
| `default_selected_flag` | `bool` | Optional | Selection of a menu entry to be displayed. In Input request message, it allows selection of one or several menu entries before any user action.<br><br>**Default**: `False` |
| `output_format` | [`OutputFormat2Enum`](../../doc/models/output-format-2-enum.md) | Required | Possible values:<br><br>* **BarCode**<br>* **MessageRef**<br>* **Text**<br>* **XHTML** |
| `predefined_content` | [`PredefinedContent`](../../doc/models/predefined-content.md) | Optional | Reference of a predefined message to display or print.<br>It conveys information related to the predefined message. |
| `output_text` | [`List[OutputText]`](../../doc/models/output-text.md) | Optional | Content of text message to display or print. It conveys Information related to the content of the text message and its format. All the data elements related to the format of the text to display or print are parameters valid for the whole Text content. |
| `output_xhtml` | `str` | Optional | XHTML document body containing the message to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1_enum import MenuEntryTag1Enum
from adyen.models.output_format_2_enum import OutputFormat2Enum
from adyen.models.output_text import OutputText
from adyen.models.predefined_content import PredefinedContent

menu_entry = MenuEntry(
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
    output_xhtml='OutputXHTML2'
)
```

