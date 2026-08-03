
# Business Lines

*This model accepts additional fields of type Any.*

## Structure

`BusinessLines`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `business_lines` | [`List[BusinessLine]`](../../doc/models/business-line.md) | Required | List of business lines. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_64 import Amount64
from adyen.models.business_line import BusinessLine
from adyen.models.business_lines import BusinessLines
from adyen.models.capability import Capability
from adyen.models.capability_problem_1 import CapabilityProblem1
from adyen.models.capability_problem_entity_1 import CapabilityProblemEntity1
from adyen.models.capability_problem_entity_recursive import CapabilityProblemEntityRecursive
from adyen.models.remediating_action import RemediatingAction
from adyen.models.service import Service
from adyen.models.source_of_funds import SourceOfFunds
from adyen.models.type_3 import Type3
from adyen.models.type_32 import Type32
from adyen.models.type_59 import Type59
from adyen.models.verification_error_1 import VerificationError1
from adyen.models.verification_error_recursive_1 import VerificationErrorRecursive1
from adyen.models.web_data import WebData

business_lines = BusinessLines(
    business_lines=[
        BusinessLine(
            id='id0',
            industry_code='industryCode2',
            legal_entity_id='legalEntityId4',
            service=Service.ISSUING,
            industry_code_description='industryCodeDescription4',
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
                ),
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
                ),
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
            sales_channels=[
                'salesChannels4',
                'salesChannels5'
            ],
            source_of_funds=SourceOfFunds(
                adyen_processed_funds=False,
                amount=Amount64(
                    currency='currency2',
                    value=110,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                asset_months_held=46,
                cryptocurrency_exchange='cryptocurrencyExchange2',
                date_of_funds_received=dateutil.parser.parse('2016-03-13').date(),
                date_of_source_event=dateutil.parser.parse('2016-03-13').date(),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            web_data=[
                WebData(
                    web_address='webAddress4',
                    web_address_id='webAddressId8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                WebData(
                    web_address='webAddress4',
                    web_address_id='webAddressId8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                WebData(
                    web_address='webAddress4',
                    web_address_id='webAddressId8',
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

