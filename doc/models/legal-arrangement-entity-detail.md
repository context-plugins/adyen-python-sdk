
# Legal Arrangement Entity Detail

## Structure

`LegalArrangementEntityDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`ViasAddress5`](../../doc/models/vias-address-5.md) | Optional | The address of the entity. |
| `business_details` | [`BusinessDetails1`](../../doc/models/business-details-1.md) | Optional | Required when creating an entity with `legalEntityType` **Business**, **NonProfit**, **PublicCompany**, or **Partnership**. |
| `email` | `str` | Optional | The e-mail address of the entity. |
| `full_phone_number` | `str` | Optional | The phone number of the contact provided as a single string.  It will be handled as a landline phone.<br>**Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344" |
| `individual_details` | [`IndividualDetails1`](../../doc/models/individual-details-1.md) | Optional | Required when creating an entity with `legalEntityType` **Individual**. |
| `legal_arrangement_entity_code` | `str` | Optional | Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement entity.<br>Use only when updating an account holder. If you include this field when creating an account holder, the request will fail. |
| `legal_arrangement_entity_reference` | `str` | Optional | Your reference for the legal arrangement entity. |
| `legal_arrangement_members` | [`List[LegalArrangementMemberEnum]`](../../doc/models/legal-arrangement-member-enum.md) | Optional | An array containing the roles of the entity in the legal arrangement.<br><br>The possible values depend on the legal arrangement `type`.<br><br>- For `type` **Association**: **ControllingPerson** and **Shareholder**.<br><br>- For `type` **Partnership**: **Partner** and **Shareholder**.<br><br>- For `type` **Trust**: **Trustee**, **Settlor**, **Protector**, **Beneficiary**,  and **Shareholder**. |
| `legal_entity_type` | [`LegalEntityTypeEnum`](../../doc/models/legal-entity-type-enum.md) | Optional | The legal entity type.<br><br>Possible values: **Business**, **Individual**, **NonProfit**, **PublicCompany**, or **Partnership**. |
| `phone_number` | [`ViasPhoneNumber2`](../../doc/models/vias-phone-number-2.md) | Optional | The phone number of the entity. |
| `web_address` | `str` | Optional | The URL of the website of the contact. |

## Example

```python
from adyen.models.business_details_1 import BusinessDetails1
from adyen.models.gender_enum import GenderEnum
from adyen.models.individual_details_1 import IndividualDetails1
from adyen.models.legal_arrangement_entity_detail import LegalArrangementEntityDetail
from adyen.models.personal_document_data import PersonalDocumentData
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.type_15_enum import Type15Enum
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details_2 import UltimateParentCompanyBusinessDetails2
from adyen.models.vias_address_1 import ViasAddress1
from adyen.models.vias_address_2 import ViasAddress2
from adyen.models.vias_address_5 import ViasAddress5
from adyen.models.vias_name_1 import ViasName1
from adyen.models.vias_name_2 import ViasName2
from adyen.models.vias_personal_data_2 import ViasPersonalData2

legal_arrangement_entity_detail = LegalArrangementEntityDetail(
    address=ViasAddress5(
        country='country0',
        city='city6',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4',
        street='street6'
    ),
    business_details=BusinessDetails1(
        doing_business_as='doingBusinessAs6',
        legal_business_name='legalBusinessName8',
        listed_ultimate_parent_company=[
            UltimateParentCompany(
                address=ViasAddress1(
                    country='country0',
                    city='city6',
                    house_number_or_name='houseNumberOrName4',
                    postal_code='postalCode8',
                    state_or_province='stateOrProvince4',
                    street='street6'
                ),
                business_details=UltimateParentCompanyBusinessDetails2(
                    legal_business_name='legalBusinessName8',
                    registration_number='registrationNumber6',
                    stock_exchange='stockExchange4',
                    stock_number='stockNumber6',
                    stock_ticker='stockTicker6'
                ),
                ultimate_parent_company_code='ultimateParentCompanyCode2'
            ),
            UltimateParentCompany(
                address=ViasAddress1(
                    country='country0',
                    city='city6',
                    house_number_or_name='houseNumberOrName4',
                    postal_code='postalCode8',
                    state_or_province='stateOrProvince4',
                    street='street6'
                ),
                business_details=UltimateParentCompanyBusinessDetails2(
                    legal_business_name='legalBusinessName8',
                    registration_number='registrationNumber6',
                    stock_exchange='stockExchange4',
                    stock_number='stockNumber6',
                    stock_ticker='stockTicker6'
                ),
                ultimate_parent_company_code='ultimateParentCompanyCode2'
            )
        ],
        registration_number='registrationNumber6',
        shareholders=[
            ShareholderContact(
                address=ViasAddress2(
                    country='country0',
                    city='city6',
                    house_number_or_name='houseNumberOrName4',
                    postal_code='postalCode8',
                    state_or_province='stateOrProvince4',
                    street='street6'
                ),
                email='email8',
                full_phone_number='fullPhoneNumber2',
                job_title='jobTitle2',
                name=ViasName1(
                    first_name='firstName4',
                    gender=GenderEnum.MALE,
                    infix='infix4',
                    last_name='lastName4'
                )
            ),
            ShareholderContact(
                address=ViasAddress2(
                    country='country0',
                    city='city6',
                    house_number_or_name='houseNumberOrName4',
                    postal_code='postalCode8',
                    state_or_province='stateOrProvince4',
                    street='street6'
                ),
                email='email8',
                full_phone_number='fullPhoneNumber2',
                job_title='jobTitle2',
                name=ViasName1(
                    first_name='firstName4',
                    gender=GenderEnum.MALE,
                    infix='infix4',
                    last_name='lastName4'
                )
            )
        ]
    ),
    email='email6',
    full_phone_number='fullPhoneNumber4',
    individual_details=IndividualDetails1(
        name=ViasName2(
            first_name='firstName4',
            gender=GenderEnum.MALE,
            infix='infix4',
            last_name='lastName4'
        ),
        personal_data=ViasPersonalData2(
            date_of_birth='dateOfBirth2',
            document_data=[
                PersonalDocumentData(
                    mtype=Type15Enum.ID,
                    expiration_date='expirationDate8',
                    issuer_country='issuerCountry0',
                    issuer_state='issuerState0',
                    number='number8'
                ),
                PersonalDocumentData(
                    mtype=Type15Enum.ID,
                    expiration_date='expirationDate8',
                    issuer_country='issuerCountry0',
                    issuer_state='issuerState0',
                    number='number8'
                ),
                PersonalDocumentData(
                    mtype=Type15Enum.ID,
                    expiration_date='expirationDate8',
                    issuer_country='issuerCountry0',
                    issuer_state='issuerState0',
                    number='number8'
                )
            ],
            nationality='nationality4'
        )
    )
)
```

