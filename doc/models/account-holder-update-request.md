
# Account Holder Update Request

*This model accepts additional fields of type Any.*

## Structure

`AccountHolderUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform` | `str` | Optional | The unique identifier of the [balance platform](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id) to which the account holder belongs. Required in the request if your API credentials can be used for multiple balance platforms. |
| `capabilities` | [`Dict[str, AccountHolderCapability]`](../../doc/models/account-holder-capability.md) | Optional | Contains key-value pairs that specify the actions that an account holder can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing. The value is an object containing the settings for the capability. |
| `contact_details` | [`ContactDetails`](../../doc/models/contact-details.md) | Optional | - |
| `description` | `str` | Optional | Your description for the account holder.<br><br>**Constraints**: *Maximum Length*: `300` |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs for general use.<br>The keys do not have specific names and may be used for storing miscellaneous data as desired.<br><br>> Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| `migrated_account_holder_code` | `str` | Optional, Read-only | The unique identifier of the migrated account holder in the classic integration. |
| `primary_balance_account` | `str` | Optional | The ID of the account holder's primary balance account. By default, this is set to the first balance account that you create for the account holder. To assign a different balance account, send a PATCH request. |
| `reference` | `str` | Optional | Your reference for the account holder.<br><br>**Constraints**: *Maximum Length*: `150` |
| `status` | [`Status5`](../../doc/models/status-5.md) | Optional | - |
| `time_zone` | `str` | Optional | The time zone of the account holder. For example, **Europe/Amsterdam**.<br>Defaults to the time zone of the balance platform if no time zone is set. For possible values, see the [list of time zone codes](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
| `verification_deadlines` | [`List[VerificationDeadline]`](../../doc/models/verification-deadline.md) | Optional, Read-only | List of verification deadlines and the capabilities that will be disallowed if verification errors are not resolved. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_holder_capability import AccountHolderCapability
from adyen.models.account_holder_update_request import AccountHolderUpdateRequest
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
from adyen.models.phone import Phone
from adyen.models.remediating_action import RemediatingAction
from adyen.models.type_21 import Type21
from adyen.models.type_3 import Type3
from adyen.models.type_4 import Type4
from adyen.models.verification_error import VerificationError
from adyen.models.verification_error_recursive import VerificationErrorRecursive

account_holder_update_request = AccountHolderUpdateRequest(
    balance_platform='balancePlatform8',
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
    description='description6',
    metadata={
        'key0': 'metadata3',
        'key1': 'metadata2',
        'key2': 'metadata1'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

