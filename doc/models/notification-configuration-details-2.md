
# Notification Configuration Details 2

Details of the notification subscription configuration.

## Structure

`NotificationConfigurationDetails2`

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
| `ssl_protocol` | [`SslProtocolEnum`](../../doc/models/ssl-protocol-enum.md) | Optional | The SSL protocol employed by the endpoint.<br><br>> Permitted values: `TLSv12`, `TLSv13`. |

## Example

```python
from adyen.models.event_type_enum import EventTypeEnum
from adyen.models.include_mode_enum import IncludeModeEnum
from adyen.models.notification_configuration_details_2 import NotificationConfigurationDetails2
from adyen.models.notification_event_configuration import NotificationEventConfiguration

notification_configuration_details_2 = NotificationConfigurationDetails2(
    active=False,
    api_version=30,
    description='description6',
    event_configs=[
        NotificationEventConfiguration(
            event_type=EventTypeEnum.SCHEDULED_REFUNDS,
            include_mode=IncludeModeEnum.EXCLUDE
        )
    ],
    hmac_signature_key='hmacSignatureKey2'
)
```

