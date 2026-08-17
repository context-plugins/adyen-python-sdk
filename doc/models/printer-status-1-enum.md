
# Printer Status 1 Enum

Possible values:

* **NoPaper**
* **OK**
* **OutOfOrder**
* **PaperJam**
* **PaperLow**

## Enumeration

`PrinterStatus1Enum`

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
from adyen.models.printer_status_1_enum import PrinterStatus1Enum

printer_status_1 = PrinterStatus1Enum.NOPAPER
```

