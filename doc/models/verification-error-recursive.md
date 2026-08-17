
# Verification Error Recursive

## Structure

`VerificationErrorRecursive`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`List[CapabilityEnum]`](../../doc/models/capability-enum.md) | Optional | Contains the capabilities that the verification error applies to. |
| `code` | `str` | Optional | The verification error code. |
| `message` | `str` | Optional | A description of the error. |
| `mtype` | [`Type212Enum`](../../doc/models/type-212-enum.md) | Optional | The type of error.<br><br>Possible values:<br><br>* **invalidInput**<br>* **dataMissing**<br>* **pendingStatus**<br>* **dataReview** |
| `remediating_actions` | [`List[RemediatingAction]`](../../doc/models/remediating-action.md) | Optional | Contains the actions that you can take to resolve the verification error. |

## Example

```python
from adyen.models.capability_enum import CapabilityEnum
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_212_enum import Type212Enum
from adyen.models.verification_error_recursive import VerificationErrorRecursive

verification_error_recursive = VerificationErrorRecursive(
    capabilities=[
        CapabilityEnum.ATMWITHDRAWALCOMMERCIAL,
        CapabilityEnum.ATMWITHDRAWAL
    ],
    code='code4',
    message='message6',
    mtype=Type212Enum.INVALIDINPUT,
    remediating_actions=[
        RemediatingAction(
            code='code4',
            message='message6'
        )
    ]
)
```

