
# Verification Error Recursive 1

## Structure

`VerificationErrorRecursive1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`List[CapabilityEnum]`](../../doc/models/capability-enum.md) | Optional | Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing the settings for the capability. |
| `code` | `str` | Optional | The general error code. |
| `message` | `str` | Optional | The general error message. |
| `mtype` | [`Type512Enum`](../../doc/models/type-512-enum.md) | Optional | The type of error.<br><br>Possible values:<br><br>* **invalidInput**<br>* **dataMissing**<br>* **pendingStatus**<br>* **rejected**<br>* **dataReview** |
| `remediating_actions` | [`List[RemediatingAction]`](../../doc/models/remediating-action.md) | Optional | An object containing possible solutions to fix a verification error. |

## Example

```python
from adyen.models.capability_enum import CapabilityEnum
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_512_enum import Type512Enum
from adyen.models.verification_error_recursive_1 import VerificationErrorRecursive1

verification_error_recursive_1 = VerificationErrorRecursive1(
    capabilities=[
        CapabilityEnum.USECARDINRESTRICTEDINDUSTRIES
    ],
    code='code8',
    message='message0',
    mtype=Type512Enum.DATAMISSING,
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
```

