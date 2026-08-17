
# Get Notification Configuration Request

## Structure

`GetNotificationConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification_id` | `int` | Required | The ID of the notification subscription configuration whose details are to be retrieved. |

## Example

```python
from adyen.models.get_notification_configuration_request import GetNotificationConfigurationRequest

get_notification_configuration_request = GetNotificationConfigurationRequest(
    notification_id=38
)
```

