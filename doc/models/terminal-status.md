
# Terminal Status

The status of the terminal:

- `OnlineToday`, `OnlineLast1Day`, `OnlineLast2Days` etcetera to `OnlineLast7Days`: Indicates when in the past week the terminal was last online.

- `SwitchedOff`: Indicates it was more than a week ago that the terminal was last online.

- `ReAssignToInventoryPending`, `ReAssignToStorePending`, `ReAssignToMerchantInventoryPending`: Indicates the terminal is scheduled to be reassigned.

## Enumeration

`TerminalStatus`

## Fields

| Name |
|  --- |
| `ONLINELAST1DAY` |
| `ONLINELAST2DAYS` |
| `ONLINELAST3DAYS` |
| `ONLINELAST4DAYS` |
| `ONLINELAST5DAYS` |
| `ONLINELAST6DAYS` |
| `ONLINELAST7DAYS` |
| `ONLINETODAY` |
| `REASSIGNTOINVENTORYPENDING` |
| `REASSIGNTOMERCHANTINVENTORYPENDING` |
| `REASSIGNTOSTOREPENDING` |
| `SWITCHEDOFF` |

## Example

```python
from adyen.models.terminal_status import TerminalStatus

terminal_status = TerminalStatus.ONLINELAST3DAYS
```

