
# Status 14 Enum

The current status of the grant. Possible values: **Pending**, **Active**, **Repaid**, **WrittenOff**, **Failed**, **Revoked**.

## Enumeration

`Status14Enum`

## Fields

| Name |
|  --- |
| `PENDING` |
| `ACTIVE` |
| `REPAID` |
| `FAILED` |
| `WRITTENOFF` |
| `REVOKED` |

## Example

```python
from adyen.models.status_14_enum import Status14Enum

status_14 = Status14Enum.WRITTENOFF
```

