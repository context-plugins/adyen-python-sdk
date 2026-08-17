
# Character Style 1 Enum

Typographic style of the sequence of characters to display or print. Absence of this data element means the characters have normal style.
Possible values:

* **Bold**
* **Italic**
* **Normal**
* **Underline**

## Enumeration

`CharacterStyle1Enum`

## Fields

| Name |
|  --- |
| `NORMAL` |
| `BOLD` |
| `ITALIC` |
| `UNDERLINE` |

## Example

```python
from adyen.models.character_style_1_enum import CharacterStyle1Enum

character_style_1 = CharacterStyle1Enum.NORMAL
```

