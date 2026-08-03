
# Account Holder Capability

*This model accepts additional fields of type Any.*

## Structure

`AccountHolderCapability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed` | `bool` | Optional, Read-only | Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful and the account holder is permitted to use the capability. |
| `allowed_level` | [`AllowedLevel`](../../doc/models/allowed-level.md) | Optional, Read-only | - |
| `allowed_settings` | [`CapabilitySettings`](../../doc/models/capability-settings.md) | Optional | - |
| `enabled` | `bool` | Optional | Indicates whether the capability is enabled. If **false**, the capability is temporarily disabled for the account holder. |
| `problems` | [`List[CapabilityProblem]`](../../doc/models/capability-problem.md) | Optional, Read-only | Contains verification errors and the actions that you can take to resolve them. |
| `requested` | `bool` | Optional | Indicates whether the capability is requested. To check whether the account holder is permitted to use the capability, refer to the `allowed` field. |
| `requested_level` | [`RequestedLevel`](../../doc/models/requested-level.md) | Optional | - |
| `requested_settings` | [`CapabilitySettings`](../../doc/models/capability-settings.md) | Optional | - |
| `transfer_instruments` | [`List[AccountSupportingEntityCapability]`](../../doc/models/account-supporting-entity-capability.md) | Optional, Read-only | Contains the status of the transfer instruments associated with this capability. |
| `verification_status` | [`VerificationStatus1`](../../doc/models/verification-status-1.md) | Optional, Read-only | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_holder_capability import AccountHolderCapability
from adyen.models.allowed_level import AllowedLevel
from adyen.models.amount_3 import Amount3
from adyen.models.capability import Capability
from adyen.models.capability_problem import CapabilityProblem
from adyen.models.capability_problem_entity import CapabilityProblemEntity
from adyen.models.capability_problem_entity_recursive import CapabilityProblemEntityRecursive
from adyen.models.capability_settings import CapabilitySettings
from adyen.models.funding_source import FundingSource
from adyen.models.interval import Interval
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_21 import Type21
from adyen.models.type_3 import Type3
from adyen.models.verification_error import VerificationError
from adyen.models.verification_error_recursive import VerificationErrorRecursive

account_holder_capability = AccountHolderCapability(
    allowed=False,
    allowed_level=AllowedLevel.MEDIUM,
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
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

