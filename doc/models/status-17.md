
# Status 17

## Structure

`Status17`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `actions` | [`List[Action1]`](../../doc/models/action-1.md) | Optional | A list of actions that need to be completed to proceed with the grant. |
| `code` | [`CodeEnum`](../../doc/models/code-enum.md) | Required | The code for the status of the grant. Possible values:<br><br>- **Pending**<br>- **Active**<br>- **Repaid**<br>- **WrittenOff**<br>- **Failed**<br>- **Revoked**<br>- **Requested**<br>- **Reviewing**<br>- **Approved**<br>- **Rejected**<br>- **Cancelled** |

## Example

```python
from adyen.models.action_1 import Action1
from adyen.models.code_enum import CodeEnum
from adyen.models.status_17 import Status17

status_17 = Status17(
    code=CodeEnum.REPAID,
    actions=[
        Action1(
            action_code='actionCode6',
            resolved=False
        ),
        Action1(
            action_code='actionCode6',
            resolved=False
        ),
        Action1(
            action_code='actionCode6',
            resolved=False
        )
    ]
)
```

