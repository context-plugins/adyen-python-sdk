
# Notification Configuration Details 4

Details of the prospective notification subscription configuration.

*This model accepts additional fields of type Any.*

## Structure

`NotificationConfigurationDetails4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `bool` | Optional | Indicates whether the notification subscription is active. |
| `api_version` | `int` | Optional | The version of the notification to which you are subscribing. To make sure that your integration can properly process the notification, subscribe to the same version as the API that you're using. |
| `description` | `str` | Optional | A description of the notification subscription configuration. |
| `event_configs` | [`List[NotificationEventConfiguration]`](../../doc/models/notification-event-configuration.md) | Optional | Contains objects that define event types and their subscription settings. |
| `hmac_signature_key` | `str` | Optional | A string with which to salt the notification(s) before hashing. If this field is provided, a hash value will be included under the notification header `HmacSignature` and the hash protocol will be included under the notification header `Protocol`. A notification body along with its `hmacSignatureKey` and `Protocol` can be used to calculate a hash value; matching this hash value with the `HmacSignature` will ensure that the notification body has not been tampered with or corrupted.<br><br>> Must be a 32-byte hex-encoded string (i.e. a string containing 64 hexadecimal characters; e.g. "b0ea55c2fe60d4d1d605e9c385e0e7f7e6cafbb939ce07010f31a327a0871f27").<br><br>The omission of this field will preclude the provision of the `HmacSignature` and `Protocol` headers in notification(s). |
| `notification_id` | `int` | Optional | Adyen-generated ID for the entry, returned in the response when you create a notification configuration. Required when updating an existing configuration using [`/updateNotificationConfiguration`](https://docs.adyen.com/api-explorer/#/NotificationConfigurationService/latest/post/updateNotificationConfiguration). |
| `notify_password` | `str` | Optional | The password to use when accessing the notifyURL with the specified username. |
| `notify_url` | `str` | Optional | The URL to which the notifications are to be sent. |
| `notify_username` | `str` | Optional | The username to use when accessing the notifyURL. |
| `ssl_protocol` | [`SslProtocol`](../../doc/models/ssl-protocol.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.event_type import EventType
from adyen.models.include_mode import IncludeMode
from adyen.models.notification_configuration_details_4 import NotificationConfigurationDetails4
from adyen.models.notification_event_configuration import NotificationEventConfiguration

notification_configuration_details_4 = NotificationConfigurationDetails4(
    active=False,
    api_version=228,
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
```

