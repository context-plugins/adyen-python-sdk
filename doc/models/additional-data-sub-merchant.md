
# Additional Data Sub Merchant

## Structure

`AdditionalDataSubMerchant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sub_merchant_number_of_sub_sellers` | `str` | Optional | Required for transactions performed by registered payment facilitators. Indicates the number of sub-merchants contained in the request. For example, **3**. |
| `sub_merchant_sub_seller_sub_seller_nr_city` | `str` | Optional | Required for transactions performed by registered payment facilitators. The city of the sub-merchant's address.<br><br>* Format: Alphanumeric<br>* Maximum length: 13 characters |
| `sub_merchant_sub_seller_sub_seller_nr_country` | `str` | Optional | Required for transactions performed by registered payment facilitators. The three-letter country code of the sub-merchant's address. For example, **BRA** for Brazil.<br><br>* Format: [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3)<br>* Fixed length: 3 characters |
| `sub_merchant_sub_seller_sub_seller_nr_email` | `str` | Optional | Required for transactions performed by registered payment facilitators. The email address of the sub-merchant.<br><br>* Format: Alphanumeric<br>* Maximum length: 40 characters |
| `sub_merchant_sub_seller_sub_seller_nr_id` | `str` | Optional | Required for transactions performed by registered payment facilitators. A unique identifier that you create for the sub-merchant, used by schemes to identify the sub-merchant.<br><br>* Format: Alphanumeric<br>* Maximum length: 15 characters |
| `sub_merchant_sub_seller_sub_seller_nr_mcc` | `str` | Optional | Required for transactions performed by registered payment facilitators. The sub-merchant's 4-digit Merchant Category Code (MCC).<br><br>* Format: Numeric<br>* Fixed length: 4 digits |
| `sub_merchant_sub_seller_sub_seller_nr_name` | `str` | Optional | Required for transactions performed by registered payment facilitators. The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement  that will appear in the card statement.<br>Exception: for acquirers in Brazil, this value does not overwrite the shopper statement.<br><br>* Format: Alphanumeric<br>* Maximum length: 22 characters |
| `sub_merchant_sub_seller_sub_seller_nr_phone_number` | `str` | Optional | Required for transactions performed by registered payment facilitators. The phone number of the sub-merchant.<br><br>* Format: Alphanumeric and special characters<br>* Maximum length: 20 characters |
| `sub_merchant_sub_seller_sub_seller_nr_postal_code` | `str` | Optional | Required for transactions performed by registered payment facilitators. The postal code of the sub-merchant's address, without dashes.<br><br>* Format: Numeric<br>* Fixed length: 8 digits |
| `sub_merchant_sub_seller_sub_seller_nr_state` | `str` | Optional | Required for transactions performed by registered payment facilitators. The state code of the sub-merchant's address, if applicable to the country.<br><br>* Format: Alphanumeric<br>* Maximum length: 2 characters |
| `sub_merchant_sub_seller_sub_seller_nr_street` | `str` | Optional | Required for transactions performed by registered payment facilitators. The street name and house number of the sub-merchant's address.<br><br>* Format: Alphanumeric<br>* Maximum length: 60 characters |
| `sub_merchant_sub_seller_sub_seller_nr_tax_id` | `str` | Optional | Required for transactions performed by registered payment facilitators. The tax ID of the sub-merchant.<br><br>* Format: Numeric<br>* Fixed length: 11 digits for the CPF or 14 digits for the CNPJ |

## Example

```python
from adyen.models.additional_data_sub_merchant import AdditionalDataSubMerchant

additional_data_sub_merchant = AdditionalDataSubMerchant(
    sub_merchant_number_of_sub_sellers='subMerchant.numberOfSubSellers4',
    sub_merchant_sub_seller_sub_seller_nr_city=Liquid error: Value cannot be null. (Parameter 'key'),
    sub_merchant_sub_seller_sub_seller_nr_country=Liquid error: Value cannot be null. (Parameter 'key'),
    sub_merchant_sub_seller_sub_seller_nr_email=Liquid error: Value cannot be null. (Parameter 'key'),
    sub_merchant_sub_seller_sub_seller_nr_id=Liquid error: Value cannot be null. (Parameter 'key')
)
```

