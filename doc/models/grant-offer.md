
# Grant Offer

*This model accepts additional fields of type Any.*

## Structure

`GrantOffer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The identifier of the account holder to which the grant is offered. |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Optional | - |
| `contract_type` | [`ContractType`](../../doc/models/contract-type.md) | Optional | - |
| `expires_at` | `datetime` | Optional | The end date of the grant offer validity period. |
| `fee` | [`Fee2`](../../doc/models/fee-2.md) | Optional | - |
| `id` | `str` | Optional | The unique identifier of the grant offer. |
| `repayment` | [`Repayment8`](../../doc/models/repayment-8.md) | Optional | - |
| `starts_at` | `datetime` | Optional | The starting date of the grant offer validity period. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.contract_type import ContractType
from adyen.models.fee_2 import Fee2
from adyen.models.grant_offer import GrantOffer

grant_offer = GrantOffer(
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
    id='id2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

