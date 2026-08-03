
# Printer Status

Indicates if the printer is working and usable.
Possible values:

* **OK**
* **PaperLow**
* **NoPaper**
* **PaperJam**
* **OutOfOrder**

## Enumeration

`PrinterStatus`

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
from adyen.models.printer_status import PrinterStatus

printer_status = PrinterStatus.OUTOFORDER
```

