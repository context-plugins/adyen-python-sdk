
# Logout Request 2

Content of the Logout Request message.

*This model accepts additional fields of type Any.*

## Structure

`LogoutRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `maintenance_allowed` | `bool` | Optional | Indicates that the POI terminal is able to or has to go to maintenance. Sent in the Logout Request to express that after closing the session, the POI may go to maintenance.<br><br>**Default**: `False` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.logout_request_2 import LogoutRequest2

logout_request_2 = LogoutRequest2(
    maintenance_allowed=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

