
# Dynamic Offer

*This model accepts additional fields of type Any.*

## Structure

`DynamicOffer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder that the dynamic offer is for. |
| `contract_type` | [`ContractType`](../../doc/models/contract-type.md) | Required | - |
| `expires_at` | `datetime` | Required | The expiration date and time of the offer validity period. |
| `financing_type` | [`FinancingType2`](../../doc/models/financing-type-2.md) | Required | - |
| `id` | `str` | Required | The unique identifier of the dynamic offer. |
| `maximum_amount` | [`MaximumAmount`](../../doc/models/maximum-amount.md) | Required | - |
| `minimum_amount` | [`MinimumAmount`](../../doc/models/minimum-amount.md) | Required | - |
| `repayment` | [`DynamicOfferRepayment`](../../doc/models/dynamic-offer-repayment.md) | Required | - |
| `starts_at` | `datetime` | Required | The starting date and time of the offer validity period. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.contract_type import ContractType
from adyen.models.dynamic_offer import DynamicOffer
from adyen.models.dynamic_offer_repayment import DynamicOfferRepayment
from adyen.models.financing_type_2 import FinancingType2
from adyen.models.maximum_amount import MaximumAmount
from adyen.models.minimum_amount import MinimumAmount
from adyen.models.term import Term

dynamic_offer = DynamicOffer(
    account_holder_id='accountHolderId8',
    contract_type=ContractType.CASHADVANCE,
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    financing_type=FinancingType2.HARDWAREFINANCING,
    id='id6',
    maximum_amount=MaximumAmount(
        currency='currency0',
        value=190,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    minimum_amount=MinimumAmount(
        currency='currency2',
        value=96,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    repayment=DynamicOfferRepayment(
        term=Term(
            estimated_days=248,
            maximum_days=24,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

