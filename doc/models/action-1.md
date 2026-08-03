
# Action 1

*This model accepts additional fields of type Any.*

## Structure

`Action1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_code` | `str` | Required | The code identifying the action that needs to be completed. |
| `resolved` | `bool` | Required | Indicates whether this action has been successfully completed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.action_1 import Action1

action_1 = Action1(
    action_code='actionCode2',
    resolved=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

