
# Legal Arrangement Detail

*This model accepts additional fields of type Any.*

## Structure

`LegalArrangementDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`ViasAddress`](../../doc/models/vias-address.md) | Required | - |
| `legal_arrangement_code` | `str` | Optional | Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement.<br>Use only when updating an account holder. If you include this field when creating an account holder, the request will fail. |
| `legal_arrangement_entities` | [`List[LegalArrangementEntityDetail]`](../../doc/models/legal-arrangement-entity-detail.md) | Optional | An array containing information about other entities that are part of the legal arrangement. |
| `legal_arrangement_reference` | `str` | Optional | Your reference for the legal arrangement. Must be between 3 to 128 characters. |
| `legal_form` | [`LegalForm`](../../doc/models/legal-form.md) | Optional | - |
| `name` | `str` | Required | The legal name of the legal arrangement. Minimum length: 3 characters. |
| `registration_number` | `str` | Optional | The registration number of the legal arrangement. |
| `tax_number` | `str` | Optional | The tax identification number of the legal arrangement. |
| `mtype` | [`Type1`](../../doc/models/type-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.business_details import BusinessDetails
from adyen.models.gender import Gender
from adyen.models.individual_details import IndividualDetails
from adyen.models.legal_arrangement_detail import LegalArrangementDetail
from adyen.models.legal_arrangement_entity_detail import LegalArrangementEntityDetail
from adyen.models.legal_form import LegalForm
from adyen.models.mtype import Type
from adyen.models.personal_document_data import PersonalDocumentData
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.type_1 import Type1
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details import UltimateParentCompanyBusinessDetails
from adyen.models.vias_address import ViasAddress
from adyen.models.vias_name import ViasName
from adyen.models.vias_personal_data import ViasPersonalData

legal_arrangement_detail = LegalArrangementDetail(
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
    name='name8',
    mtype=Type1.SOLEPROPRIETORSHIP,
    legal_arrangement_code='legalArrangementCode0',
    legal_arrangement_entities=[
        LegalArrangementEntityDetail(
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
            email='email4',
            full_phone_number='fullPhoneNumber6',
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
        ),
        LegalArrangementEntityDetail(
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
            email='email4',
            full_phone_number='fullPhoneNumber6',
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
        ),
        LegalArrangementEntityDetail(
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
            email='email4',
            full_phone_number='fullPhoneNumber6',
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
    ],
    legal_arrangement_reference='legalArrangementReference0',
    legal_form=LegalForm.DECEASEDESTATE,
    registration_number='registrationNumber4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

