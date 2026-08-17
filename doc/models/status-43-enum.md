
# Status 43 Enum

The status of the balance account. Payment instruments linked to the balance account can only be used if the balance account status is **active**.

Possible values: **active**, **closed**, **suspended**.

## Enumeration

`Status43Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |
| `SUSPENDED` |

## Example

```python
from adyen.models.status_43_enum import Status43Enum

status_43 = Status43Enum.INACTIVE
```

