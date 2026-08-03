
# Request Type

Indicates the type of request to which the rule applies. If not provided, by default, this is set to **authorization**.

Possible values: **authorization**, **authentication**, **tokenization**, **bankTransfer**.

## Enumeration

`RequestType`

## Fields

| Name |
|  --- |
| `AUTHENTICATION` |
| `AUTHORIZATION` |
| `BANKTRANSFER` |
| `TOKENIZATION` |

## Example

```python
from adyen.models.request_type import RequestType

request_type = RequestType.AUTHENTICATION
```

