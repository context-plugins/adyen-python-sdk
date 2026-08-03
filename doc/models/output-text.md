
# Output Text

Content of text message to display or print.
It conveys information related to the content of the text message and its format. All the data elements related to the format of the text to display or print are parameters valid for the whole text content.

*This model accepts additional fields of type Any.*

## Structure

`OutputText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Required | Content of text message to display, print or play. |
| `character_set` | `int` | Optional | Character height of the text string to display or print. Absence of this data element means the characters have normal height. |
| `start_row` | `int` | Optional | Row where the text string has to be displayed or printed.<br><br>**Constraints**: `>= 1`, `<= 500` |
| `start_column` | `int` | Optional | Column where the text string has to be displayed or printed.<br><br>**Constraints**: `>= 1`, `<= 500` |
| `character_width` | [`CharacterWidth1`](../../doc/models/character-width-1.md) | Optional | - |
| `character_height` | [`CharacterHeight1`](../../doc/models/character-height-1.md) | Optional | - |
| `character_style` | [`CharacterStyle1`](../../doc/models/character-style-1.md) | Optional | - |
| `alignment` | [`Alignment1`](../../doc/models/alignment-1.md) | Optional | - |
| `end_of_line_flag` | `bool` | Optional | Indicates if the text is at the end of a line. Allows the display or the print of a new line and a carry-over return characters after the formatted text.<br><br>**Default**: `True` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.output_text import OutputText

output_text = OutputText(
    text='Text4',
    character_set=102,
    start_row=166,
    start_column=128,
    character_width=CharacterWidth1.SINGLEWIDTH,
    character_height=CharacterHeight1.DOUBLEHEIGHT,
    end_of_line_flag=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

