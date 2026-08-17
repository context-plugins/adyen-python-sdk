
# Fund Destination

## Structure

`FundDestination`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iban` | `str` | Optional | Bank Account Number of the recipient |
| `additional_data` | `Dict[str, str]` | Optional | a map of name/value pairs for passing in additional/industry-specific data |
| `billing_address` | [`Address`](../../doc/models/address.md) | Optional | The address where to send the invoice. |
| `card` | [`Card1`](../../doc/models/card-1.md) | Optional | Credit card data.<br><br>Optional if `shopperReference` and `selectedRecurringDetailReference` are provided. |
| `selected_recurring_detail_reference` | `str` | Optional | The `recurringDetailReference` you want to use for this payment. The value `LATEST` can be used to select the most recently stored recurring detail. |
| `shopper_email` | `str` | Optional | the email address of the person |
| `shopper_name` | [`Name`](../../doc/models/name.md) | Optional | the name of the person |
| `shopper_reference` | `str` | Optional | Required for recurring payments.<br>Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address. |
| `sub_merchant` | [`SubMerchant`](../../doc/models/sub-merchant.md) | Optional | Required for Back-to-Back/ purchase driven load in Wallet transactions.<br>Contains the final merchant who will be receiving the money, also known as subMerchant, information. |
| `telephone_number` | `str` | Optional | the telephone number of the person |
| `wallet_purpose` | `str` | Optional | The purpose of a digital wallet transaction. |

## Example

```python
from adyen.models.address import Address
from adyen.models.card_1 import Card1
from adyen.models.fund_destination import FundDestination

fund_destination = FundDestination(
    iban='IBAN2',
    additional_data={
        'key0': 'additionalData8',
        'key1': 'additionalData9',
        'key2': 'additionalData0'
    },
    billing_address=Address(
        city='city8',
        country='country6',
        house_number_or_name='houseNumberOrName0',
        postal_code='postalCode6',
        street='street2',
        state_or_province='stateOrProvince0'
    ),
    card=Card1(
        cvc='cvc0',
        expiry_month='expiryMonth0',
        expiry_year='expiryYear0',
        holder_name='holderName2',
        issue_number='issueNumber8'
    ),
    selected_recurring_detail_reference='selectedRecurringDetailReference2'
)
```

