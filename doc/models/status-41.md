
# Status 41

The status of the balance account. Payment instruments linked to the balance account can only be used if the balance account status is **active**.

Possible values: **active**, **closed**, **suspended**.

## Enumeration

`Status41`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |
| `SUSPENDED` |

## Example

```python
from adyen.models.status_41 import Status41

status_41 = Status41.INACTIVE
```

