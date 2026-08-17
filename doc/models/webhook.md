
# Webhook

## Structure

`Webhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`WebhookLinks2`](../../doc/models/webhook-links-2.md) | Optional | References to resources connected with this webhook. |
| `accepts_expired_certificate` | `bool` | Optional | Indicates if expired SSL certificates are accepted. Default value: **false**. |
| `accepts_self_signed_certificate` | `bool` | Optional | Indicates if self-signed SSL certificates are accepted. Default value: **false**. |
| `accepts_untrusted_root_certificate` | `bool` | Optional | Indicates if untrusted SSL certificates are accepted. Default value: **false**. |
| `account_reference` | `str` | Optional | Reference to the account the webook is set on. |
| `active` | `bool` | Required | Indicates if the webhook configuration is active. The field must be **true** for you to receive webhooks about events related an account. |
| `additional_settings` | [`AdditionalSettingsResponse1`](../../doc/models/additional-settings-response-1.md) | Optional | Additional shopper and transaction information to be included in your [standard webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes). Find out more about the available [additional settings](https://docs.adyen.com/development-resources/webhooks/additional-settings). |
| `certificate_alias` | `str` | Optional | The alias of our SSL certificate. When you receive a notification from us, the alias from the HMAC signature will match this alias. |
| `communication_format` | [`CommunicationFormatEnum`](../../doc/models/communication-format-enum.md) | Required | Format or protocol for receiving webhooks. Possible values:<br><br>* **soap**<br>* **http**<br>* **json** |
| `description` | `str` | Optional | Your description for this webhook configuration. |
| `encryption_protocol` | [`EncryptionProtocolEnum`](../../doc/models/encryption-protocol-enum.md) | Optional | SSL version to access the public webhook URL specified in the `url` field. Possible values:<br><br>* **TLSv1.3**<br>* **TLSv1.2**<br>* **HTTP** - Only allowed on Test environment.<br><br>If not specified, the webhook will use `sslVersion`: **TLSv1.2**. |
| `filter_merchant_account_type` | [`FilterMerchantAccountType1Enum`](../../doc/models/filter-merchant-account-type-1-enum.md) | Optional | Shows how merchant accounts are included in company-level webhooks. Possible values:<br><br>* **includeAccounts**<br>* **excludeAccounts**<br>* **allAccounts**: Includes all merchant accounts, and does not require specifying `filterMerchantAccounts`. |
| `filter_merchant_accounts` | `List[str]` | Optional | A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion is based on the value defined for `filterMerchantAccountType`.<br><br>Required if `filterMerchantAccountType` is either:<br><br>* **includeAccounts**<br>* **excludeAccounts**<br><br>Not needed for `filterMerchantAccountType`: **allAccounts**. |
| `has_error` | `bool` | Optional | Indicates if the webhook configuration has errors that need troubleshooting. If the value is **true**, troubleshoot the configuration using the [testing endpoint](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookid}/test). |
| `has_password` | `bool` | Optional | Indicates if the webhook is password protected. |
| `hmac_key_check_value` | `str` | Optional | The [checksum](https://en.wikipedia.org/wiki/Key_checksum_value) of the HMAC key generated for this webhook. You can use this value to uniquely identify the HMAC key configured for this webhook. |
| `id` | `str` | Optional | Unique identifier for this webhook. |
| `network_type` | [`NetworkType2Enum`](../../doc/models/network-type-2-enum.md) | Optional | Network type for Terminal API details webhooks. |
| `populate_soap_action_header` | `bool` | Optional | Indicates if the SOAP action header needs to be populated. Default value: **false**.<br><br>Only applies if `communicationFormat`: **soap**. |
| `mtype` | `str` | Required | The type of webhook. Possible values are:<br><br>- **standard**<br>- **account-settings-notification**<br>- **banktransfer-notification**<br>- **boletobancario-notification**<br>- **directdebit-notification**<br>- **ach-notification-of-change-notification**<br>- **direct-debit-notice-of-change-notification**<br>- **pending-notification**<br>- **ideal-notification**<br>- **ideal-pending-notification**<br>- **report-notification**<br>- **terminal-api-notification**<br>- **terminal-settings**<br>- **terminal-boarding**<br><br>Find out more about [standard webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes) and [other types of webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#other-webhooks). |
| `url` | `str` | Required | Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**. |
| `username` | `str` | Optional | Username to access the webhook URL. |

## Example

```python
from adyen.models.communication_format_enum import CommunicationFormatEnum
from adyen.models.encryption_protocol_enum import EncryptionProtocolEnum
from adyen.models.links_element_15 import LinksElement15
from adyen.models.links_element_16 import LinksElement16
from adyen.models.links_element_17 import LinksElement17
from adyen.models.links_element_19 import LinksElement19
from adyen.models.links_element_6 import LinksElement6
from adyen.models.webhook import Webhook
from adyen.models.webhook_links_2 import WebhookLinks2

webhook = Webhook(
    active=False,
    communication_format=CommunicationFormatEnum.SOAP,
    mtype='type8',
    url='http://www.adyen.com',
    links=WebhookLinks2(
        generate_hmac=LinksElement16(
            href='href6'
        ),
        mself=LinksElement6(
            href='href0'
        ),
        test_webhook=LinksElement19(
            href='href6'
        ),
        company=LinksElement15(
            href='href2'
        ),
        merchant=LinksElement17(
            href='href6'
        )
    ),
    accepts_expired_certificate=False,
    accepts_self_signed_certificate=False,
    accepts_untrusted_root_certificate=False,
    account_reference='accountReference0',
    encryption_protocol=EncryptionProtocolEnum.ENUM_TLSV12
)
```

