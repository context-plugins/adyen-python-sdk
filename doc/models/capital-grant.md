
# Capital Grant

*This model accepts additional fields of type Any.*

## Structure

`CapitalGrant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Optional | - |
| `balances` | [`Balances`](../../doc/models/balances.md) | Required | - |
| `counterparty` | [`Counterparty10`](../../doc/models/counterparty-10.md) | Optional | - |
| `fee` | [`Fee2`](../../doc/models/fee-2.md) | Optional | - |
| `grant_account_id` | `str` | Required | The identifier of the grant account used for the grant. |
| `grant_offer_id` | `str` | Required | The identifier of the grant offer that has been selected and from which the grant details will be used. |
| `id` | `str` | Required | The identifier of the grant reference. |
| `repayment` | [`Repayment8`](../../doc/models/repayment-8.md) | Optional | - |
| `status` | [`Status18`](../../doc/models/status-18.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.balances import Balances
from adyen.models.capital_grant import CapitalGrant
from adyen.models.counterparty_10 import Counterparty10
from adyen.models.fee_2 import Fee2
from adyen.models.repayment_8 import Repayment8
from adyen.models.status_18 import Status18
from adyen.models.term import Term
from adyen.models.threshold_repayment import ThresholdRepayment

capital_grant = CapitalGrant(
    balances=Balances(
        currency='currency0',
        fee=72,
        principal=110,
        total=150,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    grant_account_id='grantAccountId4',
    grant_offer_id='grantOfferId8',
    id='id8',
    status=Status18.REPAID,
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    counterparty=Counterparty10(
        account_holder_id='accountHolderId0',
        balance_account_id='balanceAccountId0',
        transfer_instrument_id='transferInstrumentId4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
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
    repayment=Repayment8(
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

