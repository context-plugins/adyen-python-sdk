
# Get Notification Configuration List Response

*This model accepts additional fields of type Any.*

## Structure

`GetNotificationConfigurationListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configurations` | [`List[NotificationConfigurationDetails]`](../../doc/models/notification-configuration-details.md) | Optional | Details of the notification subscription configurations. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.error_field_type import ErrorFieldType
from adyen.models.event_type import EventType
from adyen.models.field_name import FieldName
from adyen.models.field_type_2 import FieldType2
from adyen.models.get_notification_configuration_list_response import GetNotificationConfigurationListResponse
from adyen.models.include_mode import IncludeMode
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
                    event_type=EventType.SCHEDULED_REFUNDS,
                    include_mode=IncludeMode.EXCLUDE,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            hmac_signature_key='hmacSignatureKey6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        NotificationConfigurationDetails(
            active=False,
            api_version=80,
            description='description0',
            event_configs=[
                NotificationEventConfiguration(
                    event_type=EventType.SCHEDULED_REFUNDS,
                    include_mode=IncludeMode.EXCLUDE,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            hmac_signature_key='hmacSignatureKey6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    invalid_fields=[
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType2(
                field='field6',
                field_name=FieldName.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    psp_reference='pspReference6',
    result_code='resultCode2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

