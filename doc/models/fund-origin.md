
# Fund Origin

*This model accepts additional fields of type Any.*

## Structure

`FundOrigin`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_address` | [`BillingAddress7`](../../doc/models/billing-address-7.md) | Optional | - |
| `shopper_email` | `str` | Optional | The email address of the person funding the money. |
| `shopper_name` | [`ShopperName`](../../doc/models/shopper-name.md) | Optional | - |
| `telephone_number` | `str` | Optional | The phone number of the person funding the money. |
| `wallet_identifier` | `str` | Optional | The unique identifier of the wallet where the funds are coming from. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.billing_address_7 import BillingAddress7
from adyen.models.fund_origin import FundOrigin
from adyen.models.shopper_name import ShopperName

fund_origin = FundOrigin(
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
    shopper_email='shopperEmail2',
    shopper_name=ShopperName(
        first_name='firstName2',
        last_name='lastName6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    telephone_number='telephoneNumber0',
    wallet_identifier='walletIdentifier2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

