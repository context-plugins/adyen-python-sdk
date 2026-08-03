
# Global Status 1

Global status of a POI Server or POI Terminal.
Possible values:

* **Busy**
* **Maintenance**
* **OK**
* **Unreachable**

## Enumeration

`GlobalStatus1`

## Fields

| Name |
|  --- |
| `OK` |
| `BUSY` |
| `MAINTENANCE` |
| `UNREACHABLE` |

## Example

```python
from adyen.models.global_status_1 import GlobalStatus1

global_status_1 = GlobalStatus1.OK
```

