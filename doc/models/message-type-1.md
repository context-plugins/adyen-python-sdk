
# Message Type 1

Type of message of the Sale to POI protocol.
Possible values:

* **Notification**
* **Request**
* **Response**

## Enumeration

`MessageType1`

## Fields

| Name |
|  --- |
| `REQUEST` |
| `RESPONSE` |
| `NOTIFICATION` |

## Example

```python
from adyen.models.message_type_1 import MessageType1

message_type_1 = MessageType1.NOTIFICATION
```

