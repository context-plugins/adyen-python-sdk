
# Capability Problem

*This model accepts additional fields of type Any.*

## Structure

`CapabilityProblem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity` | [`CapabilityProblemEntity`](../../doc/models/capability-problem-entity.md) | Optional | - |
| `verification_errors` | [`List[VerificationError]`](../../doc/models/verification-error.md) | Optional | Contains information about the verification error. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.capability import Capability
from adyen.models.capability_problem import CapabilityProblem
from adyen.models.capability_problem_entity import CapabilityProblemEntity
from adyen.models.capability_problem_entity_recursive import CapabilityProblemEntityRecursive
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_21 import Type21
from adyen.models.type_3 import Type3
from adyen.models.verification_error import VerificationError
from adyen.models.verification_error_recursive import VerificationErrorRecursive

capability_problem = CapabilityProblem(
    entity=CapabilityProblemEntity(
        documents=[
            'documents1',
            'documents2'
        ],
        id='id2',
        owner=CapabilityProblemEntityRecursive(
            documents=[
                'documents3',
                'documents4'
            ],
            id='id4',
            mtype=Type3.LEGALENTITY,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mtype=Type3.LEGALENTITY,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    verification_errors=[
        VerificationError(
            capabilities=[
                Capability.USECARDINRESTRICTEDINDUSTRIESCOMMERCIAL
            ],
            code='code0',
            message='message8',
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
                VerificationErrorRecursive(
                    capabilities=[
                        Capability.PROCESSING,
                        Capability.PAYOUTTOTRANSFERINSTRUMENT
                    ],
                    code='code2',
                    message='message4',
                    mtype=Type21.INVALIDINPUT,
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
                VerificationErrorRecursive(
                    capabilities=[
                        Capability.PROCESSING,
                        Capability.PAYOUTTOTRANSFERINSTRUMENT
                    ],
                    code='code2',
                    message='message4',
                    mtype=Type21.INVALIDINPUT,
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
                VerificationErrorRecursive(
                    capabilities=[
                        Capability.PROCESSING,
                        Capability.PAYOUTTOTRANSFERINSTRUMENT
                    ],
                    code='code2',
                    message='message4',
                    mtype=Type21.INVALIDINPUT,
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

