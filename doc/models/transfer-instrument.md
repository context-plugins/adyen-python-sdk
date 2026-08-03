
# Transfer Instrument

*This model accepts additional fields of type Any.*

## Structure

`TransferInstrument`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account` | [`BankAccountInfo`](../../doc/models/bank-account-info.md) | Required | - |
| `capabilities` | [`Dict[str, SupportingEntityCapability]`](../../doc/models/supporting-entity-capability.md) | Optional | List of capabilities for this transfer instrument. |
| `document_details` | [`List[DocumentReference]`](../../doc/models/document-reference.md) | Optional | List of documents uploaded for the transfer instrument. |
| `id` | `str` | Required, Read-only | The unique identifier of the transfer instrument. |
| `legal_entity_id` | `str` | Required | The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id) that owns the transfer instrument. |
| `problems` | [`List[CapabilityProblem1]`](../../doc/models/capability-problem-1.md) | Optional | The verification errors related to capabilities for this transfer instrument. |
| `mtype` | [`Type222`](../../doc/models/type-222.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.au_local_account_identification import AuLocalAccountIdentification
from adyen.models.bank_account_info import BankAccountInfo
from adyen.models.capability import Capability
from adyen.models.capability_problem_1 import CapabilityProblem1
from adyen.models.capability_problem_entity_1 import CapabilityProblemEntity1
from adyen.models.capability_problem_entity_recursive import CapabilityProblemEntityRecursive
from adyen.models.document_reference import DocumentReference
from adyen.models.remediating_action import RemediatingAction
from adyen.models.supporting_entity_capability import SupportingEntityCapability
from adyen.models.transfer_instrument import TransferInstrument
from adyen.models.type_222 import Type222
from adyen.models.type_3 import Type3
from adyen.models.type_32 import Type32
from adyen.models.type_413 import Type413
from adyen.models.type_59 import Type59
from adyen.models.verification_error_1 import VerificationError1
from adyen.models.verification_error_recursive_1 import VerificationErrorRecursive1

transfer_instrument = TransferInstrument(
    bank_account=BankAccountInfo(
        account_identification=AuLocalAccountIdentification(
            account_number='accountNumber4',
            bsb_code='bsbCode8',
            mtype=Type413.AULOCAL,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        account_type='accountType8',
        bank_name='bankName6',
        country_code='countryCode6',
        trusted_source=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    id='id0',
    legal_entity_id='legalEntityId4',
    mtype=Type222.BANKACCOUNT,
    capabilities={
        'key0': SupportingEntityCapability(
            allowed=False,
            id='id4',
            requested=False,
            verification_status='verificationStatus6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        'key1': SupportingEntityCapability(
            allowed=False,
            id='id4',
            requested=False,
            verification_status='verificationStatus6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        'key2': SupportingEntityCapability(
            allowed=False,
            id='id4',
            requested=False,
            verification_status='verificationStatus6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    },
    document_details=[
        DocumentReference(
            active=False,
            description='description4',
            file_name='fileName8',
            id='id4',
            modification_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
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
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

