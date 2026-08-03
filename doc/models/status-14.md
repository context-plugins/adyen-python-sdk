
# Status 14

The status of the transaction rule. If you provide a `startDate` in the request, the rule is automatically created
with an **active** status.

Possible values: **active**, **inactive**.

## Enumeration

`Status14`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `INACTIVE` |

## Example

```python
from adyen.models.status_14 import Status14

status_14 = Status14.ACTIVE
```

