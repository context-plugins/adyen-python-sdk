
# Legal Entity 3

*This model accepts additional fields of type Any.*

## Structure

`LegalEntity3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`Dict[str, LegalEntityCapability]`](../../doc/models/legal-entity-capability.md) | Optional | Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example, **issueCard** for Issuing. The value is an object containing the settings for the capability. |
| `document_details` | [`List[DocumentReference]`](../../doc/models/document-reference.md) | Optional | List of documents uploaded for the legal entity. |
| `documents` | [`List[EntityReference]`](../../doc/models/entity-reference.md) | Optional | List of documents uploaded for the legal entity. |
| `entity_associations` | [`List[LegalEntityAssociation]`](../../doc/models/legal-entity-association.md) | Optional | List of legal entities associated with the current legal entity.<br>For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories. |
| `id` | `str` | Required, Read-only | The unique identifier of the legal entity. |
| `individual` | [`Individual`](../../doc/models/individual.md) | Optional | - |
| `organization` | [`Organization`](../../doc/models/organization.md) | Optional | - |
| `problems` | [`List[CapabilityProblem1]`](../../doc/models/capability-problem-1.md) | Optional | List of verification errors related to capabilities for the legal entity. |
| `reference` | `str` | Optional | Your reference for the legal entity, maximum 150 characters.<br><br>**Constraints**: *Maximum Length*: `150` |
| `sole_proprietorship` | [`SoleProprietorship`](../../doc/models/sole-proprietorship.md) | Optional | - |
| `transfer_instruments` | [`List[TransferInstrumentReference]`](../../doc/models/transfer-instrument-reference.md) | Optional, Read-only | List of transfer instruments that the legal entity owns. |
| `trust` | [`Trust`](../../doc/models/trust.md) | Optional | - |
| `mtype` | [`Type182`](../../doc/models/type-182.md) | Optional | - |
| `unincorporated_partnership` | [`UnincorporatedPartnership`](../../doc/models/unincorporated-partnership.md) | Optional | - |
| `verification_deadlines` | [`List[VerificationDeadline]`](../../doc/models/verification-deadline.md) | Optional, Read-only | List of verification deadlines and the capabilities that will be disallowed if verification errors are not resolved. |
| `verification_plan` | `str` | Optional | A key-value pair that specifies the verification process for a legal entity. Set to **upfront** for upfront verification for [marketplaces](https://docs.adyen.com/marketplaces/verification-overview/verification-types/#upfront-verification). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.address_1 import Address1
from adyen.models.allowed_level import AllowedLevel
from adyen.models.birth_data import BirthData
from adyen.models.capability_settings_2 import CapabilitySettings2
from adyen.models.document_reference import DocumentReference
from adyen.models.entity_reference import EntityReference
from adyen.models.funding_source import FundingSource
from adyen.models.identification_data import IdentificationData
from adyen.models.individual import Individual
from adyen.models.interval import Interval
from adyen.models.legal_entity_3 import LegalEntity3
from adyen.models.legal_entity_association import LegalEntityAssociation
from adyen.models.legal_entity_capability import LegalEntityCapability
from adyen.models.max_amount import MaxAmount
from adyen.models.name_1 import Name1
from adyen.models.patchable_amount_dto import PatchableAmountDto
from adyen.models.phone_number import PhoneNumber
from adyen.models.type_132 import Type132
from adyen.models.type_142 import Type142

legal_entity_3 = LegalEntity3(
    id='id8',
    capabilities={
        'key0': LegalEntityCapability(
            allowed=False,
            allowed_level=AllowedLevel.HIGH,
            allowed_settings=CapabilitySettings2(
                amount_per_industry={
                    'key0': PatchableAmountDto(
                        currency='currency8',
                        value=56,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    'key1': PatchableAmountDto(
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
                max_amount=MaxAmount(
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
            requested=False,
            requested_level=AllowedLevel.HIGH,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        'key1': LegalEntityCapability(
            allowed=False,
            allowed_level=AllowedLevel.HIGH,
            allowed_settings=CapabilitySettings2(
                amount_per_industry={
                    'key0': PatchableAmountDto(
                        currency='currency8',
                        value=56,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    'key1': PatchableAmountDto(
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
                max_amount=MaxAmount(
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
            requested=False,
            requested_level=AllowedLevel.HIGH,
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
    documents=[
        EntityReference(
            id='id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        EntityReference(
            id='id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        EntityReference(
            id='id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    entity_associations=[
        LegalEntityAssociation(
            legal_entity_id='legalEntityId4',
            mtype=Type142.IMMEDIATEPARENTCOMPANY,
            associator_id='associatorId2',
            entity_type='entityType8',
            job_title='jobTitle4',
            name='name0',
            nominee=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        LegalEntityAssociation(
            legal_entity_id='legalEntityId4',
            mtype=Type142.IMMEDIATEPARENTCOMPANY,
            associator_id='associatorId2',
            entity_type='entityType8',
            job_title='jobTitle4',
            name='name0',
            nominee=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    individual=Individual(
        name=Name1(
            first_name='firstName4',
            last_name='lastName4',
            infix='infix4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        residential_address=Address1(
            country='country6',
            city='city2',
            postal_code='postalCode4',
            state_or_province='stateOrProvince0',
            street='street2',
            street_2='street28',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        birth_data=BirthData(
            date_of_birth='dateOfBirth8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        email='email0',
        identification_data=IdentificationData(
            mtype=Type132.NATIONALIDNUMBER,
            card_number='cardNumber6',
            expiry_date='expiryDate8',
            issuer_country='issuerCountry6',
            issuer_state='issuerState6',
            national_id_exempt=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        nationality='nationality4',
        phone=PhoneNumber(
            number='number8',
            phone_country_code='phoneCountryCode8',
            mtype='type0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

