
# Status 2 Enum

The status of your request.

If you included `adjustAuthorisationData` in your request, possible values are the following:

* **authorised**

* **refused**

Otherwise, the value is **received**.

## Enumeration

`Status2Enum`

## Fields

| Name |
|  --- |
| `AUTHORISED` |
| `RECEIVED` |
| `REFUSED` |

## Example

```python
from adyen.models.status_2_enum import Status2Enum

status_2 = Status2Enum.RECEIVED
```

