
# Printer Status 1

Possible values:

* **NoPaper**
* **OK**
* **OutOfOrder**
* **PaperJam**
* **PaperLow**

## Enumeration

`PrinterStatus1`

## Fields

| Name |
|  --- |
| `OK` |
| `PAPERLOW` |
| `NOPAPER` |
| `PAPERJAM` |
| `OUTOFORDER` |

## Example

```python
from adyen.models.printer_status_1 import PrinterStatus1

printer_status_1 = PrinterStatus1.NOPAPER
```

