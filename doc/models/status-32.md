
# Status 32

On a terminal that supports 3G or 4G connectivity, indicates the status of the primary SIM card in the terminal.

## Enumeration

`Status32`

## Fields

| Name |
|  --- |
| `ACTIVATED` |
| `DEACTIVATED` |
| `DEPRECATED` |
| `INVENTORY` |
| `READYFORACTIVATION` |

## Example

```python
from adyen.models.status_32 import Status32

status_32 = Status32.INVENTORY
```

