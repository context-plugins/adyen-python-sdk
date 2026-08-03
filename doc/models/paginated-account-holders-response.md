
# Paginated Account Holders Response

*This model accepts additional fields of type Any.*

## Structure

`PaginatedAccountHoldersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holders` | [`List[AccountHolder2]`](../../doc/models/account-holder-2.md) | Required | List of account holders. |
| `has_next` | `bool` | Required | Indicates whether there are more items on the next page. |
| `has_previous` | `bool` | Required | Indicates whether there are more items on the previous page. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_holder_2 import AccountHolder2
from adyen.models.account_holder_capability import AccountHolderCapability
from adyen.models.address_112 import Address112
from adyen.models.allowed_level import AllowedLevel
from adyen.models.amount_3 import Amount3
from adyen.models.capability import Capability
from adyen.models.capability_problem import CapabilityProblem
from adyen.models.capability_problem_entity import CapabilityProblemEntity
from adyen.models.capability_problem_entity_recursive import CapabilityProblemEntityRecursive
from adyen.models.capability_settings import CapabilitySettings
from adyen.models.contact_details import ContactDetails
from adyen.models.funding_source import FundingSource
from adyen.models.interval import Interval
from adyen.models.paginated_account_holders_response import PaginatedAccountHoldersResponse
from adyen.models.phone import Phone
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_21 import Type21
from adyen.models.type_3 import Type3
from adyen.models.type_4 import Type4
from adyen.models.verification_error import VerificationError
from adyen.models.verification_error_recursive import VerificationErrorRecursive

paginated_account_holders_response = PaginatedAccountHoldersResponse(
    account_holders=[
        AccountHolder2(
            id='id2',
            legal_entity_id='legalEntityId8',
            balance_platform='balancePlatform4',
            capabilities={
                'key0': AccountHolderCapability(
                    allowed=False,
                    allowed_level=AllowedLevel.HIGH,
                    allowed_settings=CapabilitySettings(
                        amount_per_industry={
                            'key0': Amount3(
                                currency='currency8',
                                value=56,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            'key1': Amount3(
                                currency='currency8',
                                value=56,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            )
                        },
                        authorized_card_users=False,
                        funding_source=[
                            FundingSource.CREDIT,
                            FundingSource.DEBIT,
                            FundingSource.PREPAID
                        ],
                        interval=Interval.DAILY,
                        max_amount=Amount3(
                            currency='currency4',
                            value=160,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    enabled=False,
                    problems=[
                        CapabilityProblem(
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
                                ),
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
                                ),
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
                        ),
                        CapabilityProblem(
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
                                ),
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
                                ),
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
                        ),
                        CapabilityProblem(
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
                                ),
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
                                ),
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
                    ],
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                'key1': AccountHolderCapability(
                    allowed=False,
                    allowed_level=AllowedLevel.HIGH,
                    allowed_settings=CapabilitySettings(
                        amount_per_industry={
                            'key0': Amount3(
                                currency='currency8',
                                value=56,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            'key1': Amount3(
                                currency='currency8',
                                value=56,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            )
                        },
                        authorized_card_users=False,
                        funding_source=[
                            FundingSource.CREDIT,
                            FundingSource.DEBIT,
                            FundingSource.PREPAID
                        ],
                        interval=Interval.DAILY,
                        max_amount=Amount3(
                            currency='currency4',
                            value=160,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    enabled=False,
                    problems=[
                        CapabilityProblem(
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
                                ),
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
                                ),
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
                        ),
                        CapabilityProblem(
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
                                ),
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
                                ),
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
                        ),
                        CapabilityProblem(
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
                                ),
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
                                ),
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
                    ],
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            },
            contact_details=ContactDetails(
                address=Address112(
                    city='city6',
                    country='country0',
                    house_number_or_name='houseNumberOrName4',
                    postal_code='postalCode8',
                    street='street6',
                    state_or_province='stateOrProvince4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                email='email6',
                phone=Phone(
                    number='number8',
                    mtype=Type4.LANDLINE,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                web_address='webAddress0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            description='description2',
            metadata={
                'key0': 'metadata9',
                'key1': 'metadata8'
            },
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    has_next=False,
    has_previous=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

