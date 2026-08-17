
# Capability Problem

## Structure

`CapabilityProblem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity` | [`CapabilityProblemEntity2`](../../doc/models/capability-problem-entity-2.md) | Optional | Contains the type of the entity and the corresponding ID. |
| `verification_errors` | [`List[VerificationError]`](../../doc/models/verification-error.md) | Optional | Contains information about the verification error. |

## Example

```python
from adyen.models.capability_enum import CapabilityEnum
from adyen.models.capability_problem import CapabilityProblem
from adyen.models.capability_problem_entity_2 import CapabilityProblemEntity2
from adyen.models.capability_problem_entity_recursive_2 import CapabilityProblemEntityRecursive2
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_212_enum import Type212Enum
from adyen.models.type_33_enum import Type33Enum
from adyen.models.verification_error import VerificationError
from adyen.models.verification_error_recursive import VerificationErrorRecursive

capability_problem = CapabilityProblem(
    entity=CapabilityProblemEntity2(
        documents=[
            'documents1',
            'documents2'
        ],
        id='id2',
        owner=CapabilityProblemEntityRecursive2(
            documents=[
                'documents3',
                'documents4'
            ],
            id='id4',
            mtype=Type33Enum.LEGALENTITY
        ),
        mtype=Type33Enum.LEGALENTITY
    ),
    verification_errors=[
        VerificationError(
            capabilities=[
                CapabilityEnum.USECARDINRESTRICTEDINDUSTRIESCOMMERCIAL
            ],
            code='code0',
            message='message8',
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
    ]
)
```

