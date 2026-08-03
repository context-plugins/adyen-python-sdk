
# Pan Entry Mode

Indicates the method used for entering the PAN to initiate a transaction.

Possible values: **manual**, **chip**, **magstripe**, **contactless**, **cof**, **ecommerce**, **token**.

## Enumeration

`PanEntryMode`

## Fields

| Name |
|  --- |
| `CHIP` |
| `COF` |
| `CONTACTLESS` |
| `ECOMMERCE` |
| `MAGSTRIPE` |
| `MANUAL` |
| `TOKEN` |

## Example

```python
from adyen.models.pan_entry_mode import PanEntryMode

pan_entry_mode = PanEntryMode.TOKEN
```

