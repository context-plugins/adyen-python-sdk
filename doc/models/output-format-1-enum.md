
# Output Format 1 Enum

Format of the content to display or print.
Possible values:

* **BarCode**
* **MessageRef**
* **Text**
* **XHTML**

## Enumeration

`OutputFormat1Enum`

## Fields

| Name |
|  --- |
| `MESSAGEREF` |
| `TEXT` |
| `XHTML` |
| `BARCODE` |

## Example

```python
from adyen.models.output_format_1_enum import OutputFormat1Enum

output_format_1 = OutputFormat1Enum.MESSAGEREF
```

