
# Create Notification Configuration Request

## Structure

`CreateNotificationConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configuration_details` | [`NotificationConfigurationDetails4`](../../doc/models/notification-configuration-details-4.md) | Required | Details of the prospective notification subscription configuration. |

## Example

```python
from adyen.models.create_notification_configuration_request import CreateNotificationConfigurationRequest
from adyen.models.event_type_enum import EventTypeEnum
from adyen.models.include_mode_enum import IncludeModeEnum
from adyen.models.notification_configuration_details_4 import NotificationConfigurationDetails4
from adyen.models.notification_event_configuration import NotificationEventConfiguration

create_notification_configuration_request = CreateNotificationConfigurationRequest(
    configuration_details=NotificationConfigurationDetails4(
        active=False,
        api_version=106,
        description='description6',
        event_configs=[
            NotificationEventConfiguration(
                event_type=EventTypeEnum.SCHEDULED_REFUNDS,
                include_mode=IncludeModeEnum.EXCLUDE
            ),
            NotificationEventConfiguration(
                event_type=EventTypeEnum.SCHEDULED_REFUNDS,
                include_mode=IncludeModeEnum.EXCLUDE
            )
        ],
        hmac_signature_key='hmacSignatureKey2'
    )
)
```

