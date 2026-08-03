
# Verification Error 1

*This model accepts additional fields of type Any.*

## Structure

`VerificationError1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`List[Capability]`](../../doc/models/capability.md) | Optional | Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing the settings for the capability. |
| `code` | `str` | Optional | The general error code. |
| `message` | `str` | Optional | The general error message. |
| `remediating_actions` | [`List[RemediatingAction]`](../../doc/models/remediating-action.md) | Optional | An object containing possible solutions to fix a verification error. |
| `sub_errors` | [`List[VerificationErrorRecursive1]`](../../doc/models/verification-error-recursive-1.md) | Optional | An array containing more granular information about the cause of the verification error. |
| `mtype` | [`Type59`](../../doc/models/type-59.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.capability import Capability
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_59 import Type59
from adyen.models.verification_error_1 import VerificationError1
from adyen.models.verification_error_recursive_1 import VerificationErrorRecursive1

verification_error_1 = VerificationError1(
    capabilities=[
        Capability.ATMWITHDRAWAL
    ],
    code='code4',
    message='message6',
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
        )
    ],
    sub_errors=[
        VerificationErrorRecursive1(
            capabilities=[
                Capability.PROCESSING,
                Capability.PAYOUTTOTRANSFERINSTRUMENT
            ],
            code='code2',
            message='message4',
            mtype=Type59.DATAREVIEW,
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
        ),
        VerificationErrorRecursive1(
            capabilities=[
                Capability.PROCESSING,
                Capability.PAYOUTTOTRANSFERINSTRUMENT
            ],
            code='code2',
            message='message4',
            mtype=Type59.DATAREVIEW,
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
        ),
        VerificationErrorRecursive1(
            capabilities=[
                Capability.PROCESSING,
                Capability.PAYOUTTOTRANSFERINSTRUMENT
            ],
            code='code2',
            message='message4',
            mtype=Type59.DATAREVIEW,
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

