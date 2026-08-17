
# Sub Merchant Data 2

## Structure

`SubMerchantData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The city of the sub-merchant's address. |
| `country` | `str` | Optional | The country/region of the sub-merchant's address, specified as the three-letter country code in [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) format. |
| `display_name` | `str` | Required | The name of the sub-merchant as it should appear on the display of the mobile device during transactions. |
| `email` | `str` | Optional | The email address of the sub-merchant. Required for American Express. |
| `id` | `str` | Required | Your unique identifier of the sub-merchant. |
| `mcc` | `str` | Required | The sub-merchant's four-digit Merchant Category Code (MCC). This parameter is used to correctly route the transaction. |
| `name` | `str` | Required | The name of the sub-merchant. |
| `phone_number` | `str` | Optional | The phone number of the sub-merchant. Required for American Express. |
| `postal_code` | `str` | Optional | The postal code of the sub-merchant's address, without dashes. |
| `state` | `str` | Optional | The state code of the sub-merchant's address, if applicable for the country or region. |
| `street` | `str` | Optional | The street name and house number of the sub-merchant's address. |
| `tax_id` | `str` | Optional | The tax ID of the sub-merchant. Required only in Brazil and for Cartes Bancaires in France.<br>For Brazil, this is the 11-digit CPF or 14-digit CNPJ.<br>For France, this is the SIRET, with a maximum of 14 digits. |

## Example

```python
from adyen.models.sub_merchant_data_2 import SubMerchantData2

sub_merchant_data_2 = SubMerchantData2(
    display_name='displayName4',
    id='id8',
    mcc='mcc8',
    name='name8',
    city='city8',
    country='country2',
    email='email8',
    phone_number='phoneNumber2',
    postal_code='postalCode0'
)
```

