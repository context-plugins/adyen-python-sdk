
# Get Dynamic Offers Response

*This model accepts additional fields of type Any.*

## Structure

`GetDynamicOffersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dynamic_offers` | [`List[DynamicOffer]`](../../doc/models/dynamic-offer.md) | Required | Contains a list of available dynamic offers for the specified account holder. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.contract_type import ContractType
from adyen.models.dynamic_offer import DynamicOffer
from adyen.models.dynamic_offer_repayment import DynamicOfferRepayment
from adyen.models.financing_type_2 import FinancingType2
from adyen.models.get_dynamic_offers_response import GetDynamicOffersResponse
from adyen.models.maximum_amount import MaximumAmount
from adyen.models.minimum_amount import MinimumAmount
from adyen.models.term import Term

get_dynamic_offers_response = GetDynamicOffersResponse(
    dynamic_offers=[
        DynamicOffer(
            account_holder_id='accountHolderId4',
            contract_type=ContractType.CASHADVANCE,
            expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            financing_type=FinancingType2.HARDWAREFINANCING,
            id='id2',
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

