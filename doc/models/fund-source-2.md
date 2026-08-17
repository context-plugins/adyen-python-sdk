
# Fund Source 2

## Structure

`FundSource2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | A map of name-value pairs for passing additional or industry-specific data. |
| `billing_address` | [`Address`](../../doc/models/address.md) | Optional | The address where to send the invoice. |
| `card` | [`Card`](../../doc/models/card.md) | Optional | Credit card data.<br><br>Optional if `shopperReference` and `selectedRecurringDetailReference` are provided. |
| `shopper_email` | `str` | Optional | Email address of the person. |
| `shopper_name` | [`Name`](../../doc/models/name.md) | Optional | Name of the person. |
| `telephone_number` | `str` | Optional | Phone number of the person |

## Example

```python
from adyen.models.address import Address
from adyen.models.card import Card
from adyen.models.fund_source_2 import FundSource2
from adyen.models.name import Name

fund_source_2 = FundSource2(
    additional_data={
        'key0': 'additionalData6'
    },
    billing_address=Address(
        city='city8',
        country='country6',
        house_number_or_name='houseNumberOrName0',
        postal_code='postalCode6',
        street='street2',
        state_or_province='stateOrProvince0'
    ),
    card=Card(
        cvc='cvc0',
        expiry_month='expiryMonth0',
        expiry_year='expiryYear0',
        holder_name='holderName2',
        issue_number='issueNumber8'
    ),
    shopper_email='shopperEmail2',
    shopper_name=Name(
        first_name='firstName2',
        last_name='lastName6'
    )
)
```

