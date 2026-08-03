
# Status 22

Contains the status of the grant.

*This model accepts additional fields of type Any.*

## Structure

`Status22`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `actions` | [`List[Action1]`](../../doc/models/action-1.md) | Optional | A list of actions that need to be completed to proceed with the grant. |
| `code` | [`Code`](../../doc/models/code.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.action_1 import Action1
from adyen.models.code import Code
from adyen.models.status_22 import Status22

status_22 = Status22(
    code=Code.REQUESTED,
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
)
```

