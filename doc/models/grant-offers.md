
# Grant Offers

*This model accepts additional fields of type Any.*

## Structure

`GrantOffers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_offers` | [`List[GrantOffer]`](../../doc/models/grant-offer.md) | Required | A list of available grant offers. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.contract_type import ContractType
from adyen.models.fee_2 import Fee2
from adyen.models.grant_offer import GrantOffer
from adyen.models.grant_offers import GrantOffers

grant_offers = GrantOffers(
    grant_offers=[
        GrantOffer(
            account_holder_id='accountHolderId0',
            amount=Amount5(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            contract_type=ContractType.CASHADVANCE,
            expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            fee=Fee2(
                amount=Amount5(
                    currency='currency2',
                    value=110,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id8',
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

