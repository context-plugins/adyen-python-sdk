
# Logout Request 2

Content of the Logout Request message.

## Structure

`LogoutRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `maintenance_allowed` | `bool` | Optional | Indicates that the POI terminal is able to or has to go to maintenance. Sent in the Logout Request to express that after closing the session, the POI may go to maintenance.<br><br>**Default**: `False` |

## Example

```python
from adyen.models.logout_request_2 import LogoutRequest2

logout_request_2 = LogoutRequest2(
    maintenance_allowed=False
)
```

