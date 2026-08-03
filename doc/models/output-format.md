
# Output Format

Format of the content to display or print. Display or print device function.
Possible values:

* **MessageRef**
* **Text**
* **XHTML**
* **BarCode**

## Enumeration

`OutputFormat`

## Fields

| Name |
|  --- |
| `MESSAGEREF` |
| `TEXT` |
| `XHTML` |
| `BARCODE` |

## Example

```python
from adyen.models.output_format import OutputFormat

output_format = OutputFormat.MESSAGEREF
```

