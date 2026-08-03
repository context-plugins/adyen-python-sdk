
# Update Merchant Webhook Request

*This model accepts additional fields of type Any.*

## Structure

`UpdateMerchantWebhookRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accepts_expired_certificate` | `bool` | Optional | Indicates if expired SSL certificates are accepted. Default value: **false**. |
| `accepts_self_signed_certificate` | `bool` | Optional | Indicates if self-signed SSL certificates are accepted. Default value: **false**. |
| `accepts_untrusted_root_certificate` | `bool` | Optional | Indicates if untrusted SSL certificates are accepted. Default value: **false**. |
| `active` | `bool` | Optional | Indicates if the webhook configuration is active. The field must be **true** for us to send webhooks about events related an account. |
| `additional_settings` | [`AdditionalSettings`](../../doc/models/additional-settings.md) | Optional | - |
| `communication_format` | [`CommunicationFormat`](../../doc/models/communication-format.md) | Optional | - |
| `description` | `str` | Optional | Your description for this webhook configuration. |
| `encryption_protocol` | [`EncryptionProtocol`](../../doc/models/encryption-protocol.md) | Optional | - |
| `network_type` | [`NetworkType`](../../doc/models/network-type.md) | Optional | - |
| `password` | `str` | Optional | Password to access the webhook URL. |
| `populate_soap_action_header` | `bool` | Optional | Indicates if the SOAP action header needs to be populated. Default value: **false**.<br><br>Only applies if `communicationFormat`: **soap**. |
| `url` | `str` | Optional | Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**. |
| `username` | `str` | Optional | Username to access the webhook URL.<br><br>**Constraints**: *Maximum Length*: `255` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_settings import AdditionalSettings
from adyen.models.update_merchant_webhook_request import UpdateMerchantWebhookRequest

update_merchant_webhook_request = UpdateMerchantWebhookRequest(
    accepts_expired_certificate=False,
    accepts_self_signed_certificate=False,
    accepts_untrusted_root_certificate=False,
    active=False,
    additional_settings=AdditionalSettings(
        include_event_codes=[
            'includeEventCodes8'
        ],
        properties={
            'key0': False,
            'key1': True
        },
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    url='http://www.adyen.com',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

