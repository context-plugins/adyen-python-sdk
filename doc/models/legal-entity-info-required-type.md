
# Legal Entity Info Required Type

*This model accepts additional fields of type Any.*

## Structure

`LegalEntityInfoRequiredType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`Dict[str, LegalEntityCapability]`](../../doc/models/legal-entity-capability.md) | Optional | Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example, **issueCard** for Issuing. The value is an object containing the settings for the capability. |
| `entity_associations` | [`List[LegalEntityAssociation]`](../../doc/models/legal-entity-association.md) | Optional | List of legal entities associated with the current legal entity.<br>For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories. |
| `individual` | [`Individual`](../../doc/models/individual.md) | Optional | - |
| `organization` | [`Organization`](../../doc/models/organization.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the legal entity, maximum 150 characters.<br><br>**Constraints**: *Maximum Length*: `150` |
| `sole_proprietorship` | [`SoleProprietorship`](../../doc/models/sole-proprietorship.md) | Optional | - |
| `trust` | [`Trust`](../../doc/models/trust.md) | Optional | - |
| `mtype` | [`Type212`](../../doc/models/type-212.md) | Required | - |
| `unincorporated_partnership` | [`UnincorporatedPartnership`](../../doc/models/unincorporated-partnership.md) | Optional | - |
| `verification_plan` | `str` | Optional | A key-value pair that specifies the verification process for a legal entity. Set to **upfront** for upfront verification for [marketplaces](https://docs.adyen.com/marketplaces/verification-overview/verification-types/#upfront-verification). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_1 import Address1
from adyen.models.allowed_level import AllowedLevel
from adyen.models.birth_data import BirthData
from adyen.models.capability_settings_2 import CapabilitySettings2
from adyen.models.funding_source import FundingSource
from adyen.models.identification_data import IdentificationData
from adyen.models.individual import Individual
from adyen.models.interval import Interval
from adyen.models.legal_entity_association import LegalEntityAssociation
from adyen.models.legal_entity_capability import LegalEntityCapability
from adyen.models.legal_entity_info_required_type import LegalEntityInfoRequiredType
from adyen.models.max_amount import MaxAmount
from adyen.models.name_1 import Name1
from adyen.models.organization import Organization
from adyen.models.patchable_amount_dto import PatchableAmountDto
from adyen.models.phone_number import PhoneNumber
from adyen.models.type_132 import Type132
from adyen.models.type_142 import Type142
from adyen.models.type_212 import Type212

legal_entity_info_required_type = LegalEntityInfoRequiredType(
    mtype=Type212.INDIVIDUAL,
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
        ),
        'key2': LegalEntityCapability(
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
    organization=Organization(
        legal_name='legalName2',
        registered_address=Address1(
            country='country4',
            city='city0',
            postal_code='postalCode8',
            state_or_province='stateOrProvince8',
            street='street0',
            street_2='street24',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        country_of_governing_law='countryOfGoverningLaw8',
        date_of_incorporation='dateOfIncorporation4',
        date_of_initiation_of_legal_proceeding='dateOfInitiationOfLegalProceeding6',
        description='description6',
        doing_business_as='doingBusinessAs4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reference='reference4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

