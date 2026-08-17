
# Update Account Holder State Request

## Structure

`UpdateAccountHolderStateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder on which to update the state. |
| `disable` | `bool` | Required | If true, disable the requested state.  If false, enable the requested state. |
| `reason` | `str` | Optional | The reason that the state is being updated.<br><br>> Required if the state is being disabled. |
| `state_type` | [`StateTypeEnum`](../../doc/models/state-type-enum.md) | Required | The state to be updated.<br><br>> Permitted values are: `Processing`, `Payout` |

## Example

```python
from adyen.models.state_type_enum import StateTypeEnum
from adyen.models.update_account_holder_state_request import UpdateAccountHolderStateRequest

update_account_holder_state_request = UpdateAccountHolderStateRequest(
    account_holder_code='accountHolderCode6',
    disable=False,
    state_type=StateTypeEnum.PAYOUT,
    reason='reason6'
)
```

