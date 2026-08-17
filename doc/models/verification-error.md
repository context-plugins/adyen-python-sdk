
# Verification Error

## Structure

`VerificationError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`List[CapabilityEnum]`](../../doc/models/capability-enum.md) | Optional | Contains the capabilities that the verification error applies to. |
| `code` | `str` | Optional | The verification error code. |
| `message` | `str` | Optional | A description of the error. |
| `remediating_actions` | [`List[RemediatingAction]`](../../doc/models/remediating-action.md) | Optional | Contains the actions that you can take to resolve the verification error. |
| `sub_errors` | [`List[VerificationErrorRecursive]`](../../doc/models/verification-error-recursive.md) | Optional | Contains more granular information about the verification error. |
| `mtype` | [`Type212Enum`](../../doc/models/type-212-enum.md) | Optional | The type of error.<br><br>Possible values:<br><br>* **invalidInput**<br>* **dataMissing**<br>* **pendingStatus**<br>* **dataReview** |

## Example

```python
from adyen.models.capability_enum import CapabilityEnum
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_212_enum import Type212Enum
from adyen.models.verification_error import VerificationError
from adyen.models.verification_error_recursive import VerificationErrorRecursive

verification_error = VerificationError(
    capabilities=[
        CapabilityEnum.ISSUECARD
    ],
    code='code8',
    message='message0',
    remediating_actions=[
        RemediatingAction(
            code='code4',
            message='message6'
        ),
        RemediatingAction(
            code='code4',
            message='message6'
        )
    ],
    sub_errors=[
        VerificationErrorRecursive(
            capabilities=[
                CapabilityEnum.PROCESSING,
                CapabilityEnum.PAYOUTTOTRANSFERINSTRUMENT
            ],
            code='code2',
            message='message4',
            mtype=Type212Enum.INVALIDINPUT,
            remediating_actions=[
                RemediatingAction(
                    code='code4',
                    message='message6'
                ),
                RemediatingAction(
                    code='code4',
                    message='message6'
                ),
                RemediatingAction(
                    code='code4',
                    message='message6'
                )
            ]
        ),
        VerificationErrorRecursive(
            capabilities=[
                CapabilityEnum.PROCESSING,
                CapabilityEnum.PAYOUTTOTRANSFERINSTRUMENT
            ],
            code='code2',
            message='message4',
            mtype=Type212Enum.INVALIDINPUT,
            remediating_actions=[
                RemediatingAction(
                    code='code4',
                    message='message6'
                ),
                RemediatingAction(
                    code='code4',
                    message='message6'
                ),
                RemediatingAction(
                    code='code4',
                    message='message6'
                )
            ]
        ),
        VerificationErrorRecursive(
            capabilities=[
                CapabilityEnum.PROCESSING,
                CapabilityEnum.PAYOUTTOTRANSFERINSTRUMENT
            ],
            code='code2',
            message='message4',
            mtype=Type212Enum.INVALIDINPUT,
            remediating_actions=[
                RemediatingAction(
                    code='code4',
                    message='message6'
                ),
                RemediatingAction(
                    code='code4',
                    message='message6'
                ),
                RemediatingAction(
                    code='code4',
                    message='message6'
                )
            ]
        )
    ]
)
```

