
# Output Format Enum

Format of the content to display or print. Display or print device function.
Possible values:

* **MessageRef**
* **Text**
* **XHTML**
* **BarCode**

## Enumeration

`OutputFormatEnum`

## Fields

| Name |
|  --- |
| `MESSAGEREF` |
| `TEXT` |
| `XHTML` |
| `BARCODE` |

## Example

```python
from adyen.models.output_format_enum import OutputFormatEnum

output_format = OutputFormatEnum.MESSAGEREF
```

