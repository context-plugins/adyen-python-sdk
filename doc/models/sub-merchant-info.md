
# Sub Merchant Info

*This model accepts additional fields of type Any.*

## Structure

`SubMerchantInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`BillingAddress`](../../doc/models/billing-address.md) | Optional | - |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `email` | `str` | Optional | Required for transactions performed by registered payment facilitators. The email associated with the sub-merchant's account.<br><br>**Constraints**: *Maximum Length*: `320` |
| `id` | `str` | Optional | Required for transactions performed by registered payment facilitators. A unique identifier that you create for the sub-merchant, used by schemes to identify the sub-merchant.<br><br>* Format: Alphanumeric<br>* Maximum length: 15 characters |
| `mcc` | `str` | Optional | Required for transactions performed by registered payment facilitators. The sub-merchant's 4-digit Merchant Category Code (MCC).<br><br>* Format: Numeric<br>* Fixed length: 4 digits |
| `name` | `str` | Optional | Required for transactions performed by registered payment facilitators. The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement that will appear in the card statement.<br>Exception: for acquirers in Brazil, this value does not overwrite the shopper statement.<br><br>* Format: Alphanumeric<br>* Maximum length: 22 characters |
| `phone_number` | `str` | Optional | Required for transactions performed by registered payment facilitators. The phone number associated with the sub-merchant's account.<br><br>**Constraints**: *Maximum Length*: `20` |
| `registered_since` | `str` | Optional | - |
| `tax_id` | `str` | Optional | Required for transactions performed by registered payment facilitators. The tax ID of the sub-merchant.<br><br>* Format: Numeric<br>* Fixed length: 11 digits for the CPF or 14 digits for the CNPJ |
| `url` | `str` | Optional | Required for transactions performed by registered payment facilitators. The sub-merchant's URL on the platform, i.e. the sub-merchant's shop.<br><br>**Constraints**: *Maximum Length*: `320` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.billing_address import BillingAddress
from adyen.models.sub_merchant_info import SubMerchantInfo

sub_merchant_info = SubMerchantInfo(
    address=BillingAddress(
        city='city6',
        country='country0',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode8',
        street='street6',
        state_or_province='stateOrProvince4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    email='email8',
    id='id8',
    mcc='mcc8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

