
# Delete Notification Configuration Request

## Structure

`DeleteNotificationConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification_ids` | `List[int]` | Required | A list of IDs of the notification subscription configurations to be deleted. |

## Example

```python
from adyen.models.delete_notification_configuration_request import DeleteNotificationConfigurationRequest

delete_notification_configuration_request = DeleteNotificationConfigurationRequest(
    notification_ids=[
        186,
        187
    ]
)
```

