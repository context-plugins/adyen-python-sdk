
# Status 19

The status of the webhook setting. Possible values:

* **active**: You receive a balance webhook if any of the conditions in this setting are met.
* **inactive**: You do not receive a balance webhook even if the conditions in this settings are met.

## Enumeration

`Status19`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `INACTIVE` |

## Example

```python
from adyen.models.status_19 import Status19

status_19 = Status19.ACTIVE
```

