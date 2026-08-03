
# Status 23

The status of your request.

If you included `adjustAuthorisationData` in your request, possible values are the following:

* **authorised**

* **refused**

Otherwise, the value is **received**.

## Enumeration

`Status23`

## Fields

| Name |
|  --- |
| `AUTHORISED` |
| `RECEIVED` |
| `REFUSED` |

## Example

```python
from adyen.models.status_23 import Status23

status_23 = Status23.AUTHORISED
```

