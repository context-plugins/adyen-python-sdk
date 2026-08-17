
# Fund Origin 1

The person or entity funding the money.

## Structure

`FundOrigin1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_address` | [`Address3`](../../doc/models/address-3.md) | Optional | The address where to send the invoice. |
| `shopper_email` | `str` | Optional | The email address of the person funding the money. |
| `shopper_name` | [`Name1`](../../doc/models/name-1.md) | Optional | The name of the person funding the money. |
| `telephone_number` | `str` | Optional | The phone number of the person funding the money. |
| `wallet_identifier` | `str` | Optional | The unique identifier of the wallet where the funds are coming from. |

## Example

```python
from adyen.models.address_3 import Address3
from adyen.models.fund_origin_1 import FundOrigin1
from adyen.models.name_1 import Name1

fund_origin_1 = FundOrigin1(
    billing_address=Address3(
        city='city8',
        country='country6',
        house_number_or_name='houseNumberOrName0',
        postal_code='postalCode6',
        street='street2',
        state_or_province='stateOrProvince0'
    ),
    shopper_email='shopperEmail8',
    shopper_name=Name1(
        first_name='firstName2',
        last_name='lastName6'
    ),
    telephone_number='telephoneNumber6',
    wallet_identifier='walletIdentifier8'
)
```

