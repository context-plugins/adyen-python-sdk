
# Sub Merchant

Required for Back-to-Back/ purchase driven load in Wallet transactions.
Contains the final merchant who will be receiving the money, also known as subMerchant, information.

## Structure

`SubMerchant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The city of the sub-merchant's address.<br><br>* Format: Alphanumeric<br>* Maximum length: 13 characters |
| `country` | `str` | Optional | The three-letter country code of the sub-merchant's address. For example, **BRA** for Brazil.<br><br>* Format: [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3)<br>* Fixed length: 3 characters |
| `mcc` | `str` | Optional | The sub-merchant's 4-digit Merchant Category Code (MCC).<br><br>* Format: Numeric<br>* Fixed length: 4 digits |
| `name` | `str` | Optional | The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement  that will appear in the card statement.<br><br>* Format: Alphanumeric<br>* Maximum length: 22 characters |
| `tax_id` | `str` | Optional | The tax ID of the sub-merchant.<br><br>* Format: Numeric<br>* Fixed length: 11 digits for the CPF or 14 digits for the CNPJ |

## Example

```python
from adyen.models.sub_merchant import SubMerchant

sub_merchant = SubMerchant(
    city='city4',
    country='country0',
    mcc='mcc6',
    name='name6',
    tax_id='taxId8'
)
```

