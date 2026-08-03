
# Get Notification Configuration Request

*This model accepts additional fields of type Any.*

## Structure

`GetNotificationConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification_id` | `int` | Required | The ID of the notification subscription configuration whose details are to be retrieved. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_notification_configuration_request import GetNotificationConfigurationRequest

get_notification_configuration_request = GetNotificationConfigurationRequest(
    notification_id=38,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

