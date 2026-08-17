
# Update Company Webhook Request

## Structure

`UpdateCompanyWebhookRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accepts_expired_certificate` | `bool` | Optional | Indicates if expired SSL certificates are accepted. Default value: **false**. |
| `accepts_self_signed_certificate` | `bool` | Optional | Indicates if self-signed SSL certificates are accepted. Default value: **false**. |
| `accepts_untrusted_root_certificate` | `bool` | Optional | Indicates if untrusted SSL certificates are accepted. Default value: **false**. |
| `active` | `bool` | Optional | Indicates if the webhook configuration is active. The field must be **true** for us to send webhooks about events related an account. |
| `additional_settings` | [`AdditionalSettings1`](../../doc/models/additional-settings-1.md) | Optional | Additional shopper and transaction information to be included in your [standard webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes). Find out more about the available [additional settings](https://docs.adyen.com/development-resources/webhooks/additional-settings). |
| `communication_format` | [`CommunicationFormatEnum`](../../doc/models/communication-format-enum.md) | Optional | Format or protocol for receiving webhooks. Possible values:<br><br>* **soap**<br>* **http**<br>* **json** |
| `description` | `str` | Optional | Your description for this webhook configuration. |
| `encryption_protocol` | [`EncryptionProtocolEnum`](../../doc/models/encryption-protocol-enum.md) | Optional | SSL version to access the public webhook URL specified in the `url` field. Possible values:<br><br>* **TLSv1.3**<br>* **TLSv1.2**<br>* **HTTP** - Only allowed on Test environment.<br><br>If not specified, the webhook will use `sslVersion`: **TLSv1.2**. |
| `filter_merchant_account_type` | [`FilterMerchantAccountType2Enum`](../../doc/models/filter-merchant-account-type-2-enum.md) | Optional | Shows how merchant accounts are filtered when configuring the webhook. Possible values:<br><br>* **includeAccounts**: The webhook is configured for the merchant accounts listed in `filterMerchantAccounts`.<br>* **excludeAccounts**: The webhook is not configured for the merchant accounts listed in `filterMerchantAccounts`.<br>* **allAccounts**: Includes all merchant accounts, and does not require specifying `filterMerchantAccounts`. |
| `filter_merchant_accounts` | `List[str]` | Optional | A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion is based on the value defined for `filterMerchantAccountType`.<br><br>Required if `filterMerchantAccountType` is either:<br><br>* **includeAccounts**<br>* **excludeAccounts**<br><br>Not needed for `filterMerchantAccountType`: **allAccounts**. |
| `network_type` | [`NetworkTypeEnum`](../../doc/models/network-type-enum.md) | Optional | Network type for Terminal API notification webhooks. Possible values:<br><br>* **public**<br>* **local**<br><br>Default Value: **public**. |
| `password` | `str` | Optional | Password to access the webhook URL. |
| `populate_soap_action_header` | `bool` | Optional | Indicates if the SOAP action header needs to be populated. Default value: **false**.<br><br>Only applies if `communicationFormat`: **soap**. |
| `url` | `str` | Optional | Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**. |
| `username` | `str` | Optional | Username to access the webhook URL.<br><br>**Constraints**: *Maximum Length*: `255` |

## Example

```python
from adyen.models.additional_settings_1 import AdditionalSettings1
from adyen.models.communication_format_enum import CommunicationFormatEnum
from adyen.models.encryption_protocol_enum import EncryptionProtocolEnum
from adyen.models.update_company_webhook_request import UpdateCompanyWebhookRequest

update_company_webhook_request = UpdateCompanyWebhookRequest(
    accepts_expired_certificate=False,
    accepts_self_signed_certificate=False,
    accepts_untrusted_root_certificate=False,
    active=False,
    additional_settings=AdditionalSettings1(
        include_event_codes=[
            'includeEventCodes8'
        ],
        properties={
            'key0': False,
            'key1': True
        }
    ),
    communication_format=CommunicationFormatEnum.SOAP,
    encryption_protocol=EncryptionProtocolEnum.ENUM_TLSV12,
    url='http://www.adyen.com'
)
```

