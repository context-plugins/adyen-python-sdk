
# Status 1 Enum

The status of the donation transaction.

Possible values:

* **completed**
* **pending**
* **refused**

## Enumeration

`Status1Enum`

## Fields

| Name |
|  --- |
| `COMPLETED` |
| `PENDING` |
| `REFUSED` |

## Example

```python
from adyen.models.status_1_enum import Status1Enum

status_1 = Status1Enum.COMPLETED
```

