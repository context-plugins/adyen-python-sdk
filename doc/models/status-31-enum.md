
# Status 31 Enum

On a terminal that supports 3G or 4G connectivity, indicates the status of the primary SIM card in the terminal.

## Enumeration

`Status31Enum`

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
from adyen.models.status_31_enum import Status31Enum

status_31 = Status31Enum.INVENTORY
```

