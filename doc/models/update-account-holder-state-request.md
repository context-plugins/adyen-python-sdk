
# Update Account Holder State Request

*This model accepts additional fields of type Any.*

## Structure

`UpdateAccountHolderStateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder on which to update the state. |
| `disable` | `bool` | Required | If true, disable the requested state.  If false, enable the requested state. |
| `reason` | `str` | Optional | The reason that the state is being updated.<br><br>> Required if the state is being disabled. |
| `state_type` | [`StateType`](../../doc/models/state-type.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.state_type import StateType
from adyen.models.update_account_holder_state_request import UpdateAccountHolderStateRequest

update_account_holder_state_request = UpdateAccountHolderStateRequest(
    account_holder_code='accountHolderCode6',
    disable=False,
    state_type=StateType.PAYOUT,
    reason='reason6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

