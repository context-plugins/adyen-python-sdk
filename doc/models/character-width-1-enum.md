
# Character Width 1 Enum

Character width of the text string to display or print. Absence of this data element means the characters have normal width.
Possible values:

* **DoubleWidth**
* **SingleWidth**

## Enumeration

`CharacterWidth1Enum`

## Fields

| Name |
|  --- |
| `SINGLEWIDTH` |
| `DOUBLEWIDTH` |

## Example

```python
from adyen.models.character_width_1_enum import CharacterWidth1Enum

character_width_1 = CharacterWidth1Enum.SINGLEWIDTH
```

