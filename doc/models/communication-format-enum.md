
# Communication Format Enum

Format or protocol for receiving webhooks. Possible values:

* **soap**
* **http**
* **json**

## Enumeration

`CommunicationFormatEnum`

## Fields

| Name |
|  --- |
| `HTTP` |
| `JSON` |
| `SOAP` |

## Example

```python
from adyen.models.communication_format_enum import CommunicationFormatEnum

communication_format = CommunicationFormatEnum.HTTP
```

