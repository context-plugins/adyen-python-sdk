
# PIN Request Type Enum

Type of PIN Service.
Possible values:

* **PINVerify**
* **PINVerifyOnly**
* **PINEnter**

## Enumeration

`PINRequestTypeEnum`

## Fields

| Name |
|  --- |
| `PINVERIFY` |
| `PINVERIFYONLY` |
| `PINENTER` |

## Example

```python
from adyen.models.pin_request_type_enum import PINRequestTypeEnum

pin_request_type = PINRequestTypeEnum.PINENTER
```

