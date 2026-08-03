
# Force Entry Mode

## Enumeration

`ForceEntryMode`

## Fields

| Name |
|  --- |
| `RFID` |
| `KEYED` |
| `MANUAL` |
| `FILE` |
| `SCANNED` |
| `MAGSTRIPE` |
| `ICC` |
| `SYNCHRONOUSICC` |
| `TAPPED` |
| `CONTACTLESS` |
| `CHECKREADER` |

## Example

```python
from adyen.models.force_entry_mode import ForceEntryMode

force_entry_mode = ForceEntryMode.KEYED
```

