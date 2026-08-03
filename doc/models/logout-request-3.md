
# Logout Request 3

*This model accepts additional fields of type Any.*

## Structure

`LogoutRequest3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `maintenance_allowed` | `bool` | Optional | Indicates that the POI terminal is able to or has to go to maintenance. Sent in the Logout Request to express that after closing the session, the POI may go to maintenance.<br><br>**Default**: `False` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.logout_request_3 import LogoutRequest3

logout_request_3 = LogoutRequest3(
    maintenance_allowed=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

