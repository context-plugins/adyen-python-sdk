
# Response

Indicates if the modification request has been received for processing.

## Enumeration

`Response`

## Fields

| Name |
|  --- |
| `ENUM_CAPTURERECEIVED` |
| `ENUM_CANCELRECEIVED` |
| `ENUM_REFUNDRECEIVED` |
| `ENUM_CANCELORREFUNDRECEIVED` |
| `ENUM_ADJUSTAUTHORISATIONRECEIVED` |
| `ENUM_DONATIONRECEIVED` |
| `ENUM_TECHNICALCANCELRECEIVED` |
| `ENUM_VOIDPENDINGREFUNDRECEIVED` |
| `AUTHORISED` |
| `REFUSED` |
| `ERROR` |

## Example

```python
from adyen.models.response import Response

response = Response.ENUM_REFUNDRECEIVED
```

