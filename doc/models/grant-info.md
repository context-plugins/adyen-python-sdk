
# Grant Info

*This model accepts additional fields of type Any.*

## Structure

`GrantInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `counterparty` | [`Counterparty12`](../../doc/models/counterparty-12.md) | Optional | - |
| `grant_account_id` | `str` | Required | The unique identifier of the grant account that tracks this grant. |
| `grant_offer_id` | `str` | Required | The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.counterparty_12 import Counterparty12
from adyen.models.grant_info import GrantInfo

grant_info = GrantInfo(
    grant_account_id='grantAccountId2',
    grant_offer_id='grantOfferId0',
    counterparty=Counterparty12(
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

