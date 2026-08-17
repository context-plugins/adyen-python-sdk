
# Status 32 Enum

The status of the check.

Possible values: **AWAITING_DATA** , **DATA_PROVIDED**, **FAILED**, **INVALID_DATA**, **PASSED**, **PENDING**, **RETRY_LIMIT_REACHED**.

## Enumeration

`Status32Enum`

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
from adyen.models.status_32_enum import Status32Enum

status_32 = Status32Enum.INVALID_DATA
```

