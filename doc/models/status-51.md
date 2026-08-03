
# Status 51

The status of the sweep. If not provided, by default, this is set to **active**.

Possible values:

* **active**:  the sweep is enabled and funds will be pulled in or pushed out based on the defined configuration.

* **inactive**: the sweep is disabled and cannot be triggered.

## Enumeration

`Status51`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `INACTIVE` |

## Example

```python
from adyen.models.status_51 import Status51

status_51 = Status51.ACTIVE
```

