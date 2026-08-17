
# Message Type 1 Enum

Type of message of the Sale to POI protocol.
Possible values:

* **Notification**
* **Request**
* **Response**

## Enumeration

`MessageType1Enum`

## Fields

| Name |
|  --- |
| `REQUEST` |
| `RESPONSE` |
| `NOTIFICATION` |

## Example

```python
from adyen.models.message_type_1_enum import MessageType1Enum

message_type_1 = MessageType1Enum.NOTIFICATION
```

