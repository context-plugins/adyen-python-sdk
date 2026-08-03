
# Grants

*This model accepts additional fields of type Any.*

## Structure

`Grants`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grants` | [`List[Grant]`](../../doc/models/grant.md) | Required | Contains a list of the grants that the account holder has received. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.action_1 import Action1
from adyen.models.balances import Balances
from adyen.models.code import Code
from adyen.models.counterparty_10 import Counterparty10
from adyen.models.grant import Grant
from adyen.models.grants import Grants
from adyen.models.status_8 import Status8

grants = Grants(
    grants=[
        Grant(
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
            status=Status8(
                code=Code.REJECTED,
                actions=[
                    Action1(
                        action_code='actionCode6',
                        resolved=False,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
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

