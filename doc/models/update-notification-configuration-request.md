
# Update Notification Configuration Request

## Structure

`UpdateNotificationConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configuration_details` | [`NotificationConfigurationDetails3`](../../doc/models/notification-configuration-details-3.md) | Required | Details of the notification subscription configuration to be updated. |

## Example

```python
from adyen.models.event_type_enum import EventTypeEnum
from adyen.models.include_mode_enum import IncludeModeEnum
from adyen.models.notification_configuration_details_3 import NotificationConfigurationDetails3
from adyen.models.notification_event_configuration import NotificationEventConfiguration
from adyen.models.update_notification_configuration_request import UpdateNotificationConfigurationRequest

update_notification_configuration_request = UpdateNotificationConfigurationRequest(
    configuration_details=NotificationConfigurationDetails3(
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

