
# Verification Errors

*This model accepts additional fields of type Any.*

## Structure

`VerificationErrors`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `problems` | [`List[CapabilityProblem1]`](../../doc/models/capability-problem-1.md) | Optional | List of the verification errors. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.capability import Capability
from adyen.models.capability_problem_1 import CapabilityProblem1
from adyen.models.capability_problem_entity_1 import CapabilityProblemEntity1
from adyen.models.capability_problem_entity_recursive import CapabilityProblemEntityRecursive
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_3 import Type3
from adyen.models.type_32 import Type32
from adyen.models.type_59 import Type59
from adyen.models.verification_error_1 import VerificationError1
from adyen.models.verification_error_recursive_1 import VerificationErrorRecursive1
from adyen.models.verification_errors import VerificationErrors

verification_errors = VerificationErrors(
    problems=[
        CapabilityProblem1(
            entity=CapabilityProblemEntity1(
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
                mtype=Type32.BANKACCOUNT,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            verification_errors=[
                VerificationError1(
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
                ),
                VerificationError1(
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
                ),
                VerificationError1(
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

