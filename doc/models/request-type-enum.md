
# Request Type Enum

Indicates the type of request to which the rule applies. If not provided, by default, this is set to **authorization**.

Possible values: **authorization**, **authentication**, **tokenization**, **bankTransfer**.

## Enumeration

`RequestTypeEnum`

## Fields

| Name |
|  --- |
| `AUTHENTICATION` |
| `AUTHORIZATION` |
| `BANKTRANSFER` |
| `TOKENIZATION` |

## Example

```python
from adyen.models.request_type_enum import RequestTypeEnum

request_type = RequestTypeEnum.AUTHENTICATION
```

