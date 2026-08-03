
# Legal Arrangement Entity Detail

*This model accepts additional fields of type Any.*

## Structure

`LegalArrangementEntityDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`ViasAddress`](../../doc/models/vias-address.md) | Optional | - |
| `business_details` | [`BusinessDetails`](../../doc/models/business-details.md) | Optional | - |
| `email` | `str` | Optional | The e-mail address of the entity. |
| `full_phone_number` | `str` | Optional | The phone number of the contact provided as a single string.  It will be handled as a landline phone.<br>**Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344" |
| `individual_details` | [`IndividualDetails`](../../doc/models/individual-details.md) | Optional | - |
| `legal_arrangement_entity_code` | `str` | Optional | Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement entity.<br>Use only when updating an account holder. If you include this field when creating an account holder, the request will fail. |
| `legal_arrangement_entity_reference` | `str` | Optional | Your reference for the legal arrangement entity. |
| `legal_arrangement_members` | [`List[LegalArrangementMember]`](../../doc/models/legal-arrangement-member.md) | Optional | An array containing the roles of the entity in the legal arrangement.<br><br>The possible values depend on the legal arrangement `type`.<br><br>- For `type` **Association**: **ControllingPerson** and **Shareholder**.<br><br>- For `type` **Partnership**: **Partner** and **Shareholder**.<br><br>- For `type` **Trust**: **Trustee**, **Settlor**, **Protector**, **Beneficiary**,  and **Shareholder**. |
| `legal_entity_type` | [`LegalEntityType`](../../doc/models/legal-entity-type.md) | Optional | - |
| `phone_number` | [`PhoneNumber3`](../../doc/models/phone-number-3.md) | Optional | - |
| `web_address` | `str` | Optional | The URL of the website of the contact. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.business_details import BusinessDetails
from adyen.models.gender import Gender
from adyen.models.individual_details import IndividualDetails
from adyen.models.legal_arrangement_entity_detail import LegalArrangementEntityDetail
from adyen.models.mtype import Type
from adyen.models.personal_document_data import PersonalDocumentData
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details import UltimateParentCompanyBusinessDetails
from adyen.models.vias_address import ViasAddress
from adyen.models.vias_name import ViasName
from adyen.models.vias_personal_data import ViasPersonalData

legal_arrangement_entity_detail = LegalArrangementEntityDetail(
    address=ViasAddress(
        country='country0',
        city='city6',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4',
        street='street6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    business_details=BusinessDetails(
        doing_business_as='doingBusinessAs6',
        legal_business_name='legalBusinessName8',
        listed_ultimate_parent_company=[
            UltimateParentCompany(
                address=ViasAddress(
                    country='country0',
                    city='city6',
                    house_number_or_name='houseNumberOrName4',
                    postal_code='postalCode8',
                    state_or_province='stateOrProvince4',
                    street='street6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                business_details=UltimateParentCompanyBusinessDetails(
                    legal_business_name='legalBusinessName8',
                    registration_number='registrationNumber6',
                    stock_exchange='stockExchange4',
                    stock_number='stockNumber6',
                    stock_ticker='stockTicker6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ultimate_parent_company_code='ultimateParentCompanyCode2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            UltimateParentCompany(
                address=ViasAddress(
                    country='country0',
                    city='city6',
                    house_number_or_name='houseNumberOrName4',
                    postal_code='postalCode8',
                    state_or_province='stateOrProvince4',
                    street='street6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                business_details=UltimateParentCompanyBusinessDetails(
                    legal_business_name='legalBusinessName8',
                    registration_number='registrationNumber6',
                    stock_exchange='stockExchange4',
                    stock_number='stockNumber6',
                    stock_ticker='stockTicker6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ultimate_parent_company_code='ultimateParentCompanyCode2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        registration_number='registrationNumber6',
        shareholders=[
            ShareholderContact(
                address=ViasAddress(
                    country='country0',
                    city='city6',
                    house_number_or_name='houseNumberOrName4',
                    postal_code='postalCode8',
                    state_or_province='stateOrProvince4',
                    street='street6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                email='email8',
                full_phone_number='fullPhoneNumber2',
                job_title='jobTitle2',
                name=ViasName(
                    first_name='firstName4',
                    gender=Gender.MALE,
                    infix='infix4',
                    last_name='lastName4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ShareholderContact(
                address=ViasAddress(
                    country='country0',
                    city='city6',
                    house_number_or_name='houseNumberOrName4',
                    postal_code='postalCode8',
                    state_or_province='stateOrProvince4',
                    street='street6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                email='email8',
                full_phone_number='fullPhoneNumber2',
                job_title='jobTitle2',
                name=ViasName(
                    first_name='firstName4',
                    gender=Gender.MALE,
                    infix='infix4',
                    last_name='lastName4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    email='email6',
    full_phone_number='fullPhoneNumber4',
    individual_details=IndividualDetails(
        name=ViasName(
            first_name='firstName4',
            gender=Gender.MALE,
            infix='infix4',
            last_name='lastName4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        personal_data=ViasPersonalData(
            date_of_birth='dateOfBirth2',
            document_data=[
                PersonalDocumentData(
                    mtype=Type.ID,
                    expiration_date='expirationDate8',
                    issuer_country='issuerCountry0',
                    issuer_state='issuerState0',
                    number='number8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                PersonalDocumentData(
                    mtype=Type.ID,
                    expiration_date='expirationDate8',
                    issuer_country='issuerCountry0',
                    issuer_state='issuerState0',
                    number='number8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                PersonalDocumentData(
                    mtype=Type.ID,
                    expiration_date='expirationDate8',
                    issuer_country='issuerCountry0',
                    issuer_state='issuerState0',
                    number='number8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            nationality='nationality4',
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

