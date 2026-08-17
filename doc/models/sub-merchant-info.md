
# Sub Merchant Info

## Structure

`SubMerchantInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`BillingAddress4`](../../doc/models/billing-address-4.md) | Optional | Required for transactions performed by registered payment facilitators. The sub-merchant's address. |
| `amount` | [`Amount32`](../../doc/models/amount-32.md) | Optional | Required for transactions performed by registered payment facilitators. The amount of the payment corresponding to each sub-merchant. This value will be different than the request amount if shopper is purchasing items at different sub-merchants' shops. |
| `email` | `str` | Optional | Required for transactions performed by registered payment facilitators. The email associated with the sub-merchant's account.<br><br>**Constraints**: *Maximum Length*: `320` |
| `id` | `str` | Optional | Required for transactions performed by registered payment facilitators. A unique identifier that you create for the sub-merchant, used by schemes to identify the sub-merchant.<br><br>* Format: Alphanumeric<br>* Maximum length: 15 characters |
| `mcc` | `str` | Optional | Required for transactions performed by registered payment facilitators. The sub-merchant's 4-digit Merchant Category Code (MCC).<br><br>* Format: Numeric<br>* Fixed length: 4 digits |
| `name` | `str` | Optional | Required for transactions performed by registered payment facilitators. The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement that will appear in the card statement.<br>Exception: for acquirers in Brazil, this value does not overwrite the shopper statement.<br><br>* Format: Alphanumeric<br>* Maximum length: 22 characters |
| `phone_number` | `str` | Optional | Required for transactions performed by registered payment facilitators. The phone number associated with the sub-merchant's account.<br><br>**Constraints**: *Maximum Length*: `20` |
| `registered_since` | `str` | Optional | - |
| `tax_id` | `str` | Optional | Required for transactions performed by registered payment facilitators. The tax ID of the sub-merchant.<br><br>* Format: Numeric<br>* Fixed length: 11 digits for the CPF or 14 digits for the CNPJ |
| `url` | `str` | Optional | Required for transactions performed by registered payment facilitators. The sub-merchant's URL on the platform, i.e. the sub-merchant's shop.<br><br>**Constraints**: *Maximum Length*: `320` |

## Example

```python
from adyen.models.amount_32 import Amount32
from adyen.models.billing_address_4 import BillingAddress4
from adyen.models.sub_merchant_info import SubMerchantInfo

sub_merchant_info = SubMerchantInfo(
    address=BillingAddress4(
        city='city6',
        country='country0',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode8',
        street='street6',
        state_or_province='stateOrProvince4'
    ),
    amount=Amount32(
        currency='currency2',
        value=110
    ),
    email='email8',
    id='id8',
    mcc='mcc8'
)
```

