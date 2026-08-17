
# Printer Status Enum

Indicates if the printer is working and usable.
Possible values:

* **OK**
* **PaperLow**
* **NoPaper**
* **PaperJam**
* **OutOfOrder**

## Enumeration

`PrinterStatusEnum`

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
from adyen.models.printer_status_enum import PrinterStatusEnum

printer_status = PrinterStatusEnum.OUTOFORDER
```

