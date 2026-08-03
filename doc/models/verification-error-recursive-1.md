
# Verification Error Recursive 1

*This model accepts additional fields of type Any.*

## Structure

`VerificationErrorRecursive1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`List[Capability]`](../../doc/models/capability.md) | Optional | Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing the settings for the capability. |
| `code` | `str` | Optional | The general error code. |
| `message` | `str` | Optional | The general error message. |
| `mtype` | [`Type59`](../../doc/models/type-59.md) | Optional | - |
| `remediating_actions` | [`List[RemediatingAction]`](../../doc/models/remediating-action.md) | Optional | An object containing possible solutions to fix a verification error. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.capability import Capability
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_59 import Type59
from adyen.models.verification_error_recursive_1 import VerificationErrorRecursive1

verification_error_recursive_1 = VerificationErrorRecursive1(
    capabilities=[
        Capability.USECARDINRESTRICTEDINDUSTRIES
    ],
    code='code8',
    message='message0',
    mtype=Type59.DATAMISSING,
    remediating_actions=[
        RemediatingAction(
            code='code4',
            message='message6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        RemediatingAction(
            code='code4',
            message='message6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        RemediatingAction(
            code='code4',
            message='message6',
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

