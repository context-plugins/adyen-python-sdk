
# Transfer Notification Merchant Data

## Structure

`TransferNotificationMerchantData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquirer_id` | `str` | Optional | The unique identifier of the merchant's acquirer. |
| `city` | `str` | Optional | The city where the merchant is located. |
| `country` | `str` | Optional | The country where the merchant is located. |
| `country_code` | `str` | Optional | The two-character country code of the merchant's location, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |
| `mcc` | `str` | Optional | The merchant category code. |
| `merchant_id` | `str` | Optional | The unique identifier of the merchant. |
| `name` | `str` | Optional | The name of the merchant's shop or service. |
| `postal_code` | `str` | Optional | The postal code of the merchant. |

## Example

```python
from adyen.models.transfer_notification_merchant_data import TransferNotificationMerchantData

transfer_notification_merchant_data = TransferNotificationMerchantData(
    acquirer_id='acquirerId8',
    city='city4',
    country='country0',
    country_code='countryCode8',
    mcc='mcc6'
)
```

