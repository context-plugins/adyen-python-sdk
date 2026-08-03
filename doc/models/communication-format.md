
# Communication Format

Format or protocol for receiving webhooks. Possible values:

* **soap**
* **http**
* **json**

## Enumeration

`CommunicationFormat`

## Fields

| Name |
|  --- |
| `HTTP` |
| `JSON` |
| `SOAP` |

## Example

```python
from adyen.models.communication_format import CommunicationFormat

communication_format = CommunicationFormat.HTTP
```

