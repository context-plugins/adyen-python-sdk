
# Service

The service for which you are creating the business line.

Possible values:

* **paymentProcessing**
* **issuing**
* **banking**

## Enumeration

`Service`

## Fields

| Name |
|  --- |
| `PAYMENTPROCESSING` |
| `ISSUING` |
| `BANKING` |

## Example

```python
from adyen.models.service import Service

service = Service.ISSUING
```

