
# Alignment 1 Enum

Alignment of the text string on the display line or print line. Absence of this data element means the characters have normal alignment.
Possible values:

* **Centred**
* **Justified**
* **Left**
* **Right**

## Enumeration

`Alignment1Enum`

## Fields

| Name |
|  --- |
| `LEFT` |
| `RIGHT` |
| `CENTRED` |
| `JUSTIFIED` |

## Example

```python
from adyen.models.alignment_1_enum import Alignment1Enum

alignment_1 = Alignment1Enum.LEFT
```

