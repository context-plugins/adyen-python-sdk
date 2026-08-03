
# Create Notification Configuration Request

*This model accepts additional fields of type Any.*

## Structure

`CreateNotificationConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configuration_details` | [`NotificationConfigurationDetails`](../../doc/models/notification-configuration-details.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.create_notification_configuration_request import CreateNotificationConfigurationRequest
from adyen.models.event_type import EventType
from adyen.models.include_mode import IncludeMode
from adyen.models.notification_configuration_details import NotificationConfigurationDetails
from adyen.models.notification_event_configuration import NotificationEventConfiguration

create_notification_configuration_request = CreateNotificationConfigurationRequest(
    configuration_details=NotificationConfigurationDetails(
        active=False,
        api_version=106,
        description='description6',
        event_configs=[
            NotificationEventConfiguration(
                event_type=EventType.SCHEDULED_REFUNDS,
                include_mode=IncludeMode.EXCLUDE,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            NotificationEventConfiguration(
                event_type=EventType.SCHEDULED_REFUNDS,
                include_mode=IncludeMode.EXCLUDE,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        hmac_signature_key='hmacSignatureKey2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

