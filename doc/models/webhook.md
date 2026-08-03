
# Webhook

*This model accepts additional fields of type Any.*

## Structure

`Webhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`WebhookLinks`](../../doc/models/webhook-links.md) | Optional | - |
| `accepts_expired_certificate` | `bool` | Optional | Indicates if expired SSL certificates are accepted. Default value: **false**. |
| `accepts_self_signed_certificate` | `bool` | Optional | Indicates if self-signed SSL certificates are accepted. Default value: **false**. |
| `accepts_untrusted_root_certificate` | `bool` | Optional | Indicates if untrusted SSL certificates are accepted. Default value: **false**. |
| `account_reference` | `str` | Optional | Reference to the account the webook is set on. |
| `active` | `bool` | Required | Indicates if the webhook configuration is active. The field must be **true** for you to receive webhooks about events related an account. |
| `additional_settings` | [`AdditionalSettingsResponse`](../../doc/models/additional-settings-response.md) | Optional | - |
| `certificate_alias` | `str` | Optional | The alias of our SSL certificate. When you receive a notification from us, the alias from the HMAC signature will match this alias. |
| `communication_format` | [`CommunicationFormat`](../../doc/models/communication-format.md) | Required | - |
| `description` | `str` | Optional | Your description for this webhook configuration. |
| `encryption_protocol` | [`EncryptionProtocol`](../../doc/models/encryption-protocol.md) | Optional | - |
| `filter_merchant_account_type` | [`FilterMerchantAccountType1`](../../doc/models/filter-merchant-account-type-1.md) | Optional | - |
| `filter_merchant_accounts` | `List[str]` | Optional | A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion is based on the value defined for `filterMerchantAccountType`.<br><br>Required if `filterMerchantAccountType` is either:<br><br>* **includeAccounts**<br>* **excludeAccounts**<br><br>Not needed for `filterMerchantAccountType`: **allAccounts**. |
| `has_error` | `bool` | Optional | Indicates if the webhook configuration has errors that need troubleshooting. If the value is **true**, troubleshoot the configuration using the [testing endpoint](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookid}/test). |
| `has_password` | `bool` | Optional | Indicates if the webhook is password protected. |
| `hmac_key_check_value` | `str` | Optional | The [checksum](https://en.wikipedia.org/wiki/Key_checksum_value) of the HMAC key generated for this webhook. You can use this value to uniquely identify the HMAC key configured for this webhook. |
| `id` | `str` | Optional | Unique identifier for this webhook. |
| `network_type` | [`NetworkType2`](../../doc/models/network-type-2.md) | Optional | - |
| `populate_soap_action_header` | `bool` | Optional | Indicates if the SOAP action header needs to be populated. Default value: **false**.<br><br>Only applies if `communicationFormat`: **soap**. |
| `mtype` | `str` | Required | The type of webhook. Possible values are:<br><br>- **standard**<br>- **account-settings-notification**<br>- **banktransfer-notification**<br>- **boletobancario-notification**<br>- **directdebit-notification**<br>- **ach-notification-of-change-notification**<br>- **direct-debit-notice-of-change-notification**<br>- **pending-notification**<br>- **ideal-notification**<br>- **ideal-pending-notification**<br>- **report-notification**<br>- **terminal-api-notification**<br>- **terminal-settings**<br>- **terminal-boarding**<br><br>Find out more about [standard webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes) and [other types of webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#other-webhooks). |
| `url` | `str` | Required | Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**. |
| `username` | `str` | Optional | Username to access the webhook URL. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.communication_format import CommunicationFormat
from adyen.models.company_4 import Company4
from adyen.models.generate_hmac import GenerateHmac
from adyen.models.merchant_1 import Merchant1
from adyen.models.mself import Self
from adyen.models.test_webhook import TestWebhook
from adyen.models.webhook import Webhook
from adyen.models.webhook_links import WebhookLinks

webhook = Webhook(
    active=False,
    communication_format=CommunicationFormat.HTTP,
    mtype='type8',
    url='http://www.adyen.com',
    links=WebhookLinks(
        generate_hmac=GenerateHmac(
            href='href6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mself=Self(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        test_webhook=TestWebhook(
            href='href6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        company=Company4(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        merchant=Merchant1(
            href='href6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    accepts_expired_certificate=False,
    accepts_self_signed_certificate=False,
    accepts_untrusted_root_certificate=False,
    account_reference='accountReference0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

