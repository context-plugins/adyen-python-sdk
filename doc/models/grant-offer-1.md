
# Grant Offer 1

*This model accepts additional fields of type Any.*

## Structure

`GrantOffer1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder to which the grant is offered. |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Optional | - |
| `contract_type` | [`ContractType`](../../doc/models/contract-type.md) | Optional | - |
| `expires_at` | `datetime` | Optional | The expiration date and time of the offer validity period. |
| `fee` | [`GrantOfferFee`](../../doc/models/grant-offer-fee.md) | Optional | - |
| `id` | `str` | Optional | The unique identifier of the offer. |
| `repayment` | [`Repayment1`](../../doc/models/repayment-1.md) | Optional | - |
| `starts_at` | `datetime` | Optional | The starting date and time of the offer validity period. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.contract_type import ContractType
from adyen.models.grant_offer_1 import GrantOffer1
from adyen.models.grant_offer_fee import GrantOfferFee

grant_offer_1 = GrantOffer1(
    account_holder_id='accountHolderId8',
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    contract_type=ContractType.CASHADVANCE,
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    fee=GrantOfferFee(
        amount=Amount5(
            currency='currency2',
            value=110,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        apr_basis_points=142,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    id='id6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

