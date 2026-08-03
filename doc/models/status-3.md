
# Status 3

The status of the check.

Possible values: **AWAITING_DATA** , **DATA_PROVIDED**, **FAILED**, **INVALID_DATA**, **PASSED**, **PENDING**, **RETRY_LIMIT_REACHED**.

## Enumeration

`Status3`

## Fields

| Name |
|  --- |
| `AWAITING_DATA` |
| `DATA_PROVIDED` |
| `FAILED` |
| `INVALID_DATA` |
| `PASSED` |
| `PENDING` |
| `PENDING_REVIEW` |
| `RETRY_LIMIT_REACHED` |
| `UNCHECKED` |

## Example

```python
from adyen.models.status_3 import Status3

status_3 = Status3.UNCHECKED
```

