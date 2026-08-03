
# Fund Destination 1

the person or entity receiving the money

*This model accepts additional fields of type Any.*

## Structure

`FundDestination1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iban` | `str` | Optional | Bank Account Number of the recipient |
| `additional_data` | `Dict[str, str]` | Optional | a map of name/value pairs for passing in additional/industry-specific data |
| `billing_address` | [`BillingAddress7`](../../doc/models/billing-address-7.md) | Optional | - |
| `card` | [`Card6`](../../doc/models/card-6.md) | Optional | - |
| `selected_recurring_detail_reference` | `str` | Optional | The `recurringDetailReference` you want to use for this payment. The value `LATEST` can be used to select the most recently stored recurring detail. |
| `shopper_email` | `str` | Optional | the email address of the person |
| `shopper_name` | [`ShopperName`](../../doc/models/shopper-name.md) | Optional | - |
| `shopper_reference` | `str` | Optional | Required for recurring payments.<br>Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address. |
| `sub_merchant` | [`SubMerchant1`](../../doc/models/sub-merchant-1.md) | Optional | - |
| `telephone_number` | `str` | Optional | the telephone number of the person |
| `wallet_purpose` | `str` | Optional | The purpose of a digital wallet transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.billing_address_7 import BillingAddress7
from adyen.models.card_6 import Card6
from adyen.models.fund_destination_1 import FundDestination1

fund_destination_1 = FundDestination1(
    iban='IBAN2',
    additional_data={
        'key0': 'additionalData2',
        'key1': 'additionalData3',
        'key2': 'additionalData4'
    },
    billing_address=BillingAddress7(
        city='city8',
        country='country6',
        house_number_or_name='houseNumberOrName0',
        postal_code='postalCode6',
        street='street2',
        state_or_province='stateOrProvince0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card=Card6(
        cvc='cvc0',
        expiry_month='expiryMonth0',
        expiry_year='expiryYear0',
        holder_name='holderName2',
        issue_number='issueNumber8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    selected_recurring_detail_reference='selectedRecurringDetailReference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

