
# Capital Grants

*This model accepts additional fields of type Any.*

## Structure

`CapitalGrants`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grants` | [`List[CapitalGrant]`](../../doc/models/capital-grant.md) | Required | The unique identifier of the grant. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.balances import Balances
from adyen.models.capital_grant import CapitalGrant
from adyen.models.capital_grants import CapitalGrants
from adyen.models.counterparty_10 import Counterparty10
from adyen.models.fee_2 import Fee2
from adyen.models.repayment_8 import Repayment8
from adyen.models.status_18 import Status18
from adyen.models.term import Term
from adyen.models.threshold_repayment import ThresholdRepayment

capital_grants = CapitalGrants(
    grants=[
        CapitalGrant(
            balances=Balances(
                currency='currency0',
                fee=72,
                principal=110,
                total=150,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            grant_account_id='grantAccountId6',
            grant_offer_id='grantOfferId6',
            id='id0',
            status=Status18.PENDING,
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

