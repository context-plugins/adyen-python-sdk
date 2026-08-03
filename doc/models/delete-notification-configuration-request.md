
# Delete Notification Configuration Request

*This model accepts additional fields of type Any.*

## Structure

`DeleteNotificationConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification_ids` | `List[int]` | Required | A list of IDs of the notification subscription configurations to be deleted. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.delete_notification_configuration_request import DeleteNotificationConfigurationRequest

delete_notification_configuration_request = DeleteNotificationConfigurationRequest(
    notification_ids=[
        186,
        187
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

