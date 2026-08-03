
# Verification Error Recursive

*This model accepts additional fields of type Any.*

## Structure

`VerificationErrorRecursive`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`List[Capability]`](../../doc/models/capability.md) | Optional | Contains the capabilities that the verification error applies to. |
| `code` | `str` | Optional | The verification error code. |
| `message` | `str` | Optional | A description of the error. |
| `mtype` | [`Type21`](../../doc/models/type-21.md) | Optional | - |
| `remediating_actions` | [`List[RemediatingAction]`](../../doc/models/remediating-action.md) | Optional | Contains the actions that you can take to resolve the verification error. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.capability import Capability
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_21 import Type21
from adyen.models.verification_error_recursive import VerificationErrorRecursive

verification_error_recursive = VerificationErrorRecursive(
    capabilities=[
        Capability.ATMWITHDRAWALCOMMERCIAL,
        Capability.ATMWITHDRAWAL
    ],
    code='code4',
    message='message6',
    mtype=Type21.INVALIDINPUT,
    remediating_actions=[
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

