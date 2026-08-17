
# Verification Error 1

## Structure

`VerificationError1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`List[CapabilityEnum]`](../../doc/models/capability-enum.md) | Optional | Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing the settings for the capability. |
| `code` | `str` | Optional | The general error code. |
| `message` | `str` | Optional | The general error message. |
| `remediating_actions` | [`List[RemediatingAction]`](../../doc/models/remediating-action.md) | Optional | An object containing possible solutions to fix a verification error. |
| `sub_errors` | [`List[VerificationErrorRecursive1]`](../../doc/models/verification-error-recursive-1.md) | Optional | An array containing more granular information about the cause of the verification error. |
| `mtype` | [`Type512Enum`](../../doc/models/type-512-enum.md) | Optional | The type of error.<br><br>Possible values:<br><br>* **invalidInput**<br>* **dataMissing**<br>* **pendingStatus**<br>* **rejected**<br>* **dataReview** |

## Example

```python
from adyen.models.capability_enum import CapabilityEnum
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_512_enum import Type512Enum
from adyen.models.verification_error_1 import VerificationError1
from adyen.models.verification_error_recursive_1 import VerificationErrorRecursive1

verification_error_1 = VerificationError1(
    capabilities=[
        CapabilityEnum.ATMWITHDRAWAL
    ],
    code='code4',
    message='message6',
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
        VerificationErrorRecursive1(
            capabilities=[
                CapabilityEnum.PROCESSING,
                CapabilityEnum.PAYOUTTOTRANSFERINSTRUMENT
            ],
            code='code2',
            message='message4',
            mtype=Type512Enum.DATAREVIEW,
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
        VerificationErrorRecursive1(
            capabilities=[
                CapabilityEnum.PROCESSING,
                CapabilityEnum.PAYOUTTOTRANSFERINSTRUMENT
            ],
            code='code2',
            message='message4',
            mtype=Type512Enum.DATAREVIEW,
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
        VerificationErrorRecursive1(
            capabilities=[
                CapabilityEnum.PROCESSING,
                CapabilityEnum.PAYOUTTOTRANSFERINSTRUMENT
            ],
            code='code2',
            message='message4',
            mtype=Type512Enum.DATAREVIEW,
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

