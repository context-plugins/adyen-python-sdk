
# Grant

*This model accepts additional fields of type Any.*

## Structure

`Grant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balances` | [`Balances`](../../doc/models/balances.md) | Required | - |
| `counterparty` | [`Counterparty10`](../../doc/models/counterparty-10.md) | Optional | - |
| `grant_account_id` | `str` | Required | The unique identifier of the grant account that tracks this grant. |
| `grant_offer_id` | `str` | Required | The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant. |
| `id` | `str` | Required | The unique identifier of the grant reference. |
| `status` | [`Status8`](../../doc/models/status-8.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.action_1 import Action1
from adyen.models.balances import Balances
from adyen.models.code import Code
from adyen.models.counterparty_10 import Counterparty10
from adyen.models.grant import Grant
from adyen.models.status_8 import Status8

grant = Grant(
    balances=Balances(
        currency='currency0',
        fee=72,
        principal=110,
        total=150,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    grant_account_id='grantAccountId8',
    grant_offer_id='grantOfferId4',
    id='id2',
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
```

