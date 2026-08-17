
# Capability Problem 1

## Structure

`CapabilityProblem1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity` | [`CapabilityProblemEntity1`](../../doc/models/capability-problem-entity-1.md) | Optional | - |
| `verification_errors` | [`List[VerificationError1]`](../../doc/models/verification-error-1.md) | Optional | - |

## Example

```python
from adyen.models.capability_enum import CapabilityEnum
from adyen.models.capability_problem_1 import CapabilityProblem1
from adyen.models.capability_problem_entity_1 import CapabilityProblemEntity1
from adyen.models.capability_problem_entity_recursive_1 import CapabilityProblemEntityRecursive1
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_311_enum import Type311Enum
from adyen.models.type_512_enum import Type512Enum
from adyen.models.verification_error_1 import VerificationError1
from adyen.models.verification_error_recursive_1 import VerificationErrorRecursive1

capability_problem_1 = CapabilityProblem1(
    entity=CapabilityProblemEntity1(
        documents=[
            'documents1',
            'documents2'
        ],
        id='id2',
        owner=CapabilityProblemEntityRecursive1(
            documents=[
                'documents3',
                'documents4'
            ],
            id='id4',
            mtype=Type311Enum.LEGALENTITY
        ),
        mtype=Type311Enum.BANKACCOUNT
    ),
    verification_errors=[
        VerificationError1(
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
    ]
)
```

