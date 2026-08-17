
# Legal Entity 3

## Structure

`LegalEntity3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capabilities` | [`Dict[str, LegalEntityCapability]`](../../doc/models/legal-entity-capability.md) | Optional | Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example, **issueCard** for Issuing. The value is an object containing the settings for the capability. |
| `document_details` | [`List[DocumentReference]`](../../doc/models/document-reference.md) | Optional | List of documents uploaded for the legal entity. |
| `documents` | [`List[UploadAndroidAppResponse]`](../../doc/models/upload-android-app-response.md) | Optional | List of documents uploaded for the legal entity. |
| `entity_associations` | [`List[LegalEntityAssociation]`](../../doc/models/legal-entity-association.md) | Optional | List of legal entities associated with the current legal entity.<br>For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories. |
| `id` | `str` | Required, Read-only | The unique identifier of the legal entity. |
| `individual` | [`Individual1`](../../doc/models/individual-1.md) | Optional | Information about the individual. Required if `type` is **individual**. |
| `organization` | [`Organization1`](../../doc/models/organization-1.md) | Optional | Information about the organization. Required if `type` is **organization**. |
| `problems` | [`List[CapabilityProblem1]`](../../doc/models/capability-problem-1.md) | Optional | List of verification errors related to capabilities for the legal entity. |
| `reference` | `str` | Optional | Your reference for the legal entity, maximum 150 characters.<br><br>**Constraints**: *Maximum Length*: `150` |
| `sole_proprietorship` | [`SoleProprietorship1`](../../doc/models/sole-proprietorship-1.md) | Optional | Information about the sole proprietorship. Required if `type` is **soleProprietorship**. |
| `transfer_instruments` | [`List[TransferInstrumentReference]`](../../doc/models/transfer-instrument-reference.md) | Optional, Read-only | List of transfer instruments that the legal entity owns. |
| `trust` | [`Trust1`](../../doc/models/trust-1.md) | Optional | Information about the trust. Required if `type` is **trust**. |
| `mtype` | [`Type182Enum`](../../doc/models/type-182-enum.md) | Optional | The type of legal entity.<br><br>Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**. |
| `unincorporated_partnership` | [`UnincorporatedPartnership1`](../../doc/models/unincorporated-partnership-1.md) | Optional | Information about the unincorporated partnership. Required if `type` is **unincorporatedPartnership**. |
| `verification_deadlines` | [`List[VerificationDeadline]`](../../doc/models/verification-deadline.md) | Optional, Read-only | List of verification deadlines and the capabilities that will be disallowed if verification errors are not resolved. |
| `verification_plan` | `str` | Optional | A key-value pair that specifies the verification process for a legal entity. Set to **upfront** for upfront verification for [marketplaces](https://docs.adyen.com/marketplaces/verification-overview/verification-types/#upfront-verification). |

## Example

```python
import dateutil.parser

from adyen.models.address_13 import Address13
from adyen.models.birth_data_1 import BirthData1
from adyen.models.capability_settings_11 import CapabilitySettings11
from adyen.models.document_reference import DocumentReference
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.identification_data_1 import IdentificationData1
from adyen.models.individual_1 import Individual1
from adyen.models.interval_enum import IntervalEnum
from adyen.models.legal_entity_3 import LegalEntity3
from adyen.models.legal_entity_association import LegalEntityAssociation
from adyen.models.legal_entity_capability import LegalEntityCapability
from adyen.models.name_23 import Name23
from adyen.models.patchable_amount_dto import PatchableAmountDTO
from adyen.models.phone_number_2 import PhoneNumber2
from adyen.models.type_132_enum import Type132Enum
from adyen.models.type_142_enum import Type142Enum
from adyen.models.upload_android_app_response import UploadAndroidAppResponse

legal_entity_3 = LegalEntity3(
    id=None,
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
    document_details=[
        DocumentReference(
            active=False,
            description='description4',
            file_name='fileName8',
            id='id4',
            modification_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ],
    documents=[
        UploadAndroidAppResponse(
            id='id4'
        ),
        UploadAndroidAppResponse(
            id='id4'
        ),
        UploadAndroidAppResponse(
            id='id4'
        )
    ],
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
    )
)
```

