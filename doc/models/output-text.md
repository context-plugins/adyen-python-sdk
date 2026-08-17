
# Output Text

Content of text message to display or print.
It conveys information related to the content of the text message and its format. All the data elements related to the format of the text to display or print are parameters valid for the whole text content.

## Structure

`OutputText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Required | Content of text message to display, print or play. |
| `character_set` | `int` | Optional | Character height of the text string to display or print. Absence of this data element means the characters have normal height. |
| `start_row` | `int` | Optional | Row where the text string has to be displayed or printed.<br><br>**Constraints**: `>= 1`, `<= 500` |
| `start_column` | `int` | Optional | Column where the text string has to be displayed or printed.<br><br>**Constraints**: `>= 1`, `<= 500` |
| `character_width` | [`CharacterWidth1Enum`](../../doc/models/character-width-1-enum.md) | Optional | Character width of the text string to display or print. Absence of this data element means the characters have normal width.<br>Possible values:<br><br>* **DoubleWidth**<br>* **SingleWidth** |
| `character_height` | [`CharacterHeight1Enum`](../../doc/models/character-height-1-enum.md) | Optional | Character height of the text string to display or print. Absence of this data element means the characters have normal height.<br>Possible values:<br><br>* **DoubleHeight**<br>* **HalfHeight**<br>* **SingleHeight** |
| `character_style` | [`CharacterStyle1Enum`](../../doc/models/character-style-1-enum.md) | Optional | Typographic style of the sequence of characters to display or print. Absence of this data element means the characters have normal style.<br>Possible values:<br><br>* **Bold**<br>* **Italic**<br>* **Normal**<br>* **Underline** |
| `alignment` | [`Alignment1Enum`](../../doc/models/alignment-1-enum.md) | Optional | Alignment of the text string on the display line or print line. Absence of this data element means the characters have normal alignment.<br>Possible values:<br><br>* **Centred**<br>* **Justified**<br>* **Left**<br>* **Right** |
| `end_of_line_flag` | `bool` | Optional | Indicates if the text is at the end of a line. Allows the display or the print of a new line and a carry-over return characters after the formatted text.<br><br>**Default**: `True` |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.output_text import OutputText

output_text = OutputText(
    text='Text4',
    character_set=102,
    start_row=166,
    start_column=128,
    character_width=CharacterWidth1Enum.SINGLEWIDTH,
    character_height=CharacterHeight1Enum.DOUBLEHEIGHT,
    end_of_line_flag=True
)
```

