
# Character Height 1 Enum

Character height of the text string to display or print. Absence of this data element means the characters have normal height.
Possible values:

* **DoubleHeight**
* **HalfHeight**
* **SingleHeight**

## Enumeration

`CharacterHeight1Enum`

## Fields

| Name |
|  --- |
| `SINGLEHEIGHT` |
| `DOUBLEHEIGHT` |
| `HALFHEIGHT` |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum

character_height_1 = CharacterHeight1Enum.DOUBLEHEIGHT
```

