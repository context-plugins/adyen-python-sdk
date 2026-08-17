
# Global Status 1 Enum

Global status of a POI Server or POI Terminal.
Possible values:

* **Busy**
* **Maintenance**
* **OK**
* **Unreachable**

## Enumeration

`GlobalStatus1Enum`

## Fields

| Name |
|  --- |
| `OK` |
| `BUSY` |
| `MAINTENANCE` |
| `UNREACHABLE` |

## Example

```python
from adyen.models.global_status_1_enum import GlobalStatus1Enum

global_status_1 = GlobalStatus1Enum.OK
```

