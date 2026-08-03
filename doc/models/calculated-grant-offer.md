
# Calculated Grant Offer

*This model accepts additional fields of type Any.*

## Structure

`CalculatedGrantOffer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder that the dynamic offer is for. |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `contract_type` | [`ContractType`](../../doc/models/contract-type.md) | Required | - |
| `expires_at` | `datetime` | Required | The expiration date and time of the offer validity period. |
| `fee` | [`GrantOfferFee`](../../doc/models/grant-offer-fee.md) | Required | - |
| `repayment` | [`Repayment1`](../../doc/models/repayment-1.md) | Required | - |
| `starts_at` | `datetime` | Required | The starting date and time of the offer validity period. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.calculated_grant_offer import CalculatedGrantOffer
from adyen.models.contract_type import ContractType
from adyen.models.grant_offer_fee import GrantOfferFee
from adyen.models.repayment_1 import Repayment1
from adyen.models.term import Term
from adyen.models.threshold_repayment import ThresholdRepayment

calculated_grant_offer = CalculatedGrantOffer(
    account_holder_id='accountHolderId4',
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
    repayment=Repayment1(
        basis_points=18,
        term=Term(
            estimated_days=248,
            maximum_days=24,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        threshold=ThresholdRepayment(
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

