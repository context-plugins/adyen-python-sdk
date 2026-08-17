
# Service Enum

The service for which you are creating the business line.

Possible values:

* **paymentProcessing**
* **issuing**
* **banking**

## Enumeration

`ServiceEnum`

## Fields

| Name |
|  --- |
| `PAYMENTPROCESSING` |
| `ISSUING` |
| `BANKING` |

## Example

```python
from adyen.models.service_enum import ServiceEnum

service = ServiceEnum.ISSUING
```

