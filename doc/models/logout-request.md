
# Logout Request

Empty.
Content of the Logout Request message.

## Structure

`LogoutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `maintenance_allowed` | `bool` | Optional | Indicates that the POI terminal is able to or has to go to maintenance. Sent in the Logout Request to express that after closing the session, the POI may go to maintenance.<br><br>**Default**: `False` |

## Example

```python
from adyen.models.logout_request import LogoutRequest

logout_request = LogoutRequest(
    maintenance_allowed=False
)
```

