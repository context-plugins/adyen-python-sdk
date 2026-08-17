
# Get Notification Configuration List Response

## Structure

`GetNotificationConfigurationListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configurations` | [`List[NotificationConfigurationDetails]`](../../doc/models/notification-configuration-details.md) | Optional | Details of the notification subscription configurations. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |

## Example

```python
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.event_type_enum import EventTypeEnum
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType
from adyen.models.get_notification_configuration_list_response import GetNotificationConfigurationListResponse
from adyen.models.include_mode_enum import IncludeModeEnum
from adyen.models.notification_configuration_details import NotificationConfigurationDetails
from adyen.models.notification_event_configuration import NotificationEventConfiguration

get_notification_configuration_list_response = GetNotificationConfigurationListResponse(
    configurations=[
        NotificationConfigurationDetails(
            active=False,
            api_version=80,
            description='description0',
            event_configs=[
                NotificationEventConfiguration(
                    event_type=EventTypeEnum.SCHEDULED_REFUNDS,
                    include_mode=IncludeModeEnum.EXCLUDE
                )
            ],
            hmac_signature_key='hmacSignatureKey6'
        ),
        NotificationConfigurationDetails(
            active=False,
            api_version=80,
            description='description0',
            event_configs=[
                NotificationEventConfiguration(
                    event_type=EventTypeEnum.SCHEDULED_REFUNDS,
                    include_mode=IncludeModeEnum.EXCLUDE
                )
            ],
            hmac_signature_key='hmacSignatureKey6'
        )
    ],
    invalid_fields=[
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        )
    ],
    psp_reference='pspReference6',
    result_code='resultCode2'
)
```

