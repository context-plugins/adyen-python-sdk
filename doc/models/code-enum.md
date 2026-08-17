
# Code Enum

The code for the status of the grant. Possible values:

- **Pending**
- **Active**
- **Repaid**
- **WrittenOff**
- **Failed**
- **Revoked**
- **Requested**
- **Reviewing**
- **Approved**
- **Rejected**
- **Cancelled**

## Enumeration

`CodeEnum`

## Fields

| Name |
|  --- |
| `PENDING` |
| `ACTIVE` |
| `REPAID` |
| `WRITTENOFF` |
| `FAILED` |
| `REVOKED` |
| `REQUESTED` |
| `REVIEWING` |
| `APPROVED` |
| `REJECTED` |
| `CANCELLED` |

## Example

```python
from adyen.models.code_enum import CodeEnum

code = CodeEnum.CANCELLED
```

