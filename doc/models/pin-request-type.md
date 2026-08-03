
# Pin Request Type

Type of PIN Service.
Possible values:

* **PINVerify**
* **PINVerifyOnly**
* **PINEnter**

## Enumeration

`PinRequestType`

## Fields

| Name |
|  --- |
| `PINVERIFY` |
| `PINVERIFYONLY` |
| `PINENTER` |

## Example

```python
from adyen.models.pin_request_type import PinRequestType

pin_request_type = PinRequestType.PINENTER
```

