
# Legal Entity Info

## Structure

`LegalEntityInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`Dict[str, LegalEntityCapability]`](../../doc/models/legal-entity-capability.md) | Optional | Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example, **issueCard** for Issuing. The value is an object containing the settings for the capability. |
| `entity_associations` | [`List[LegalEntityAssociation]`](../../doc/models/legal-entity-association.md) | Optional | List of legal entities associated with the current legal entity.<br>For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories. |
| `individual` | [`Individual1`](../../doc/models/individual-1.md) | Optional | Information about the individual. Required if `type` is **individual**. |
| `organization` | [`Organization1`](../../doc/models/organization-1.md) | Optional | Information about the organization. Required if `type` is **organization**. |
| `reference` | `str` | Optional | Your reference for the legal entity, maximum 150 characters.<br><br>**Constraints**: *Maximum Length*: `150` |
| `sole_proprietorship` | [`SoleProprietorship1`](../../doc/models/sole-proprietorship-1.md) | Optional | Information about the sole proprietorship. Required if `type` is **soleProprietorship**. |
| `trust` | [`Trust1`](../../doc/models/trust-1.md) | Optional | Information about the trust. Required if `type` is **trust**. |
| `mtype` | [`Type182Enum`](../../doc/models/type-182-enum.md) | Optional | The type of legal entity.<br><br>Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**. |
| `unincorporated_partnership` | [`UnincorporatedPartnership1`](../../doc/models/unincorporated-partnership-1.md) | Optional | Information about the unincorporated partnership. Required if `type` is **unincorporatedPartnership**. |
| `verification_plan` | `str` | Optional | A key-value pair that specifies the verification process for a legal entity. Set to **upfront** for upfront verification for [marketplaces](https://docs.adyen.com/marketplaces/verification-overview/verification-types/#upfront-verification). |

## Example

```python
from adyen.models.address_13 import Address13
from adyen.models.address_31 import Address31
from adyen.models.birth_data_1 import BirthData1
from adyen.models.capability_settings_11 import CapabilitySettings11
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.identification_data_1 import IdentificationData1
from adyen.models.individual_1 import Individual1
from adyen.models.interval_enum import IntervalEnum
from adyen.models.legal_entity_association import LegalEntityAssociation
from adyen.models.legal_entity_capability import LegalEntityCapability
from adyen.models.legal_entity_info import LegalEntityInfo
from adyen.models.name_23 import Name23
from adyen.models.organization_1 import Organization1
from adyen.models.patchable_amount_dto import PatchableAmountDTO
from adyen.models.phone_number_2 import PhoneNumber2
from adyen.models.type_132_enum import Type132Enum
from adyen.models.type_142_enum import Type142Enum

legal_entity_info = LegalEntityInfo(
    capabilities={
        'key0': LegalEntityCapability(
            allowed_settings=CapabilitySettings11(
                amount_per_industry={
                    'key0': PatchableAmountDTO(
                        currency='currency8',
                        value=56
                    ),
                    'key1': PatchableAmountDTO(
                        currency='currency8',
                        value=56
                    )
                },
                authorized_card_users=False,
                funding_source=[
                    FundingSourceEnum.CREDIT,
                    FundingSourceEnum.DEBIT,
                    FundingSourceEnum.PREPAID
                ],
                interval=IntervalEnum.DAILY,
                max_amount=PatchableAmountDTO(
                    currency='currency4',
                    value=160
                )
            )
        ),
        'key1': LegalEntityCapability(
            allowed_settings=CapabilitySettings11(
                amount_per_industry={
                    'key0': PatchableAmountDTO(
                        currency='currency8',
                        value=56
                    ),
                    'key1': PatchableAmountDTO(
                        currency='currency8',
                        value=56
                    )
                },
                authorized_card_users=False,
                funding_source=[
                    FundingSourceEnum.CREDIT,
                    FundingSourceEnum.DEBIT,
                    FundingSourceEnum.PREPAID
                ],
                interval=IntervalEnum.DAILY,
                max_amount=PatchableAmountDTO(
                    currency='currency4',
                    value=160
                )
            )
        )
    },
    entity_associations=[
        LegalEntityAssociation(
            legal_entity_id='legalEntityId4',
            mtype=Type142Enum.IMMEDIATEPARENTCOMPANY,
            job_title='jobTitle4',
            nominee=False
        ),
        LegalEntityAssociation(
            legal_entity_id='legalEntityId4',
            mtype=Type142Enum.IMMEDIATEPARENTCOMPANY,
            job_title='jobTitle4',
            nominee=False
        ),
        LegalEntityAssociation(
            legal_entity_id='legalEntityId4',
            mtype=Type142Enum.IMMEDIATEPARENTCOMPANY,
            job_title='jobTitle4',
            nominee=False
        )
    ],
    individual=Individual1(
        name=Name23(
            first_name='firstName4',
            last_name='lastName4',
            infix='infix4'
        ),
        residential_address=Address13(
            country='country6',
            city='city2',
            postal_code='postalCode4',
            state_or_province='stateOrProvince0',
            street='street2',
            street_2='street28'
        ),
        birth_data=BirthData1(
            date_of_birth='dateOfBirth8'
        ),
        email='email0',
        identification_data=IdentificationData1(
            mtype=Type132Enum.NATIONALIDNUMBER,
            card_number='cardNumber6',
            expiry_date='expiryDate8',
            issuer_country='issuerCountry6',
            issuer_state='issuerState6',
            national_id_exempt=False
        ),
        nationality='nationality4',
        phone=PhoneNumber2(
            number='number8',
            mtype='type0'
        )
    ),
    organization=Organization1(
        legal_name='legalName2',
        registered_address=Address31(
            country='country4',
            city='city0',
            postal_code='postalCode8',
            state_or_province='stateOrProvince8',
            street='street0',
            street_2='street24'
        ),
        country_of_governing_law='countryOfGoverningLaw8',
        date_of_incorporation='dateOfIncorporation4',
        date_of_initiation_of_legal_proceeding='dateOfInitiationOfLegalProceeding6',
        description='description6',
        doing_business_as='doingBusinessAs4'
    ),
    reference='reference2'
)
```

