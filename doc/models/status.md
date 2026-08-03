
# Status

The status of the store. Possible values: **Pending**, **Active**, **Inactive**, **InactiveWithModifications**, **Closed**.

## Enumeration

`Status`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |
| `INACTIVEWITHMODIFICATIONS` |
| `PENDING` |

## Example

```python
from adyen.models.status import Status

status = Status.INACTIVEWITHMODIFICATIONS
```

