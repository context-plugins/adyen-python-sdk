
# Action 1

## Structure

`Action1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_code` | `str` | Required | The code identifying the action that needs to be completed. |
| `resolved` | `bool` | Required | Indicates whether this action has been successfully completed. |

## Example

```python
from adyen.models.action_1 import Action1

action_1 = Action1(
    action_code='actionCode2',
    resolved=False
)
```

