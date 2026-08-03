
# Status 18

The current status of the grant. Possible values: **Pending**, **Active**, **Repaid**, **WrittenOff**, **Failed**, **Revoked**.

## Enumeration

`Status18`

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
from adyen.models.status_18 import Status18

status_18 = Status18.REPAID
```

