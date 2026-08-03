
# Business Details 1

Required when creating an entity with `legalEntityType` **Business**, **NonProfit**, **PublicCompany**, or **Partnership**.

*This model accepts additional fields of type Any.*

## Structure

`BusinessDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `doing_business_as` | `str` | Optional | The registered name of the company (if it differs from the legal name of the company). |
| `legal_business_name` | `str` | Optional | The legal name of the company. |
| `listed_ultimate_parent_company` | [`List[UltimateParentCompany]`](../../doc/models/ultimate-parent-company.md) | Optional | Information about the parent public company. Required if the account holder is 100% owned by a publicly listed company. |
| `registration_number` | `str` | Optional | The registration number of the company. |
| `shareholders` | [`List[ShareholderContact]`](../../doc/models/shareholder-contact.md) | Optional | Array containing information about individuals associated with the account holder either through ownership or control. For details about how you can identify them, refer to [our verification guide](https://docs.adyen.com/classic-platforms/verification-process#identify-ubos). |
| `signatories` | [`List[SignatoryContact]`](../../doc/models/signatory-contact.md) | Optional | Signatories associated with the company.<br>Each array entry should represent one signatory. |
| `stock_exchange` | `str` | Optional | Market Identifier Code (MIC). |
| `stock_number` | `str` | Optional | International Securities Identification Number (ISIN). |
| `stock_ticker` | `str` | Optional | Stock Ticker symbol. |
| `tax_id` | `str` | Optional | The tax ID of the company. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.business_details_1 import BusinessDetails1
from adyen.models.gender import Gender
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details import UltimateParentCompanyBusinessDetails
from adyen.models.vias_address import ViasAddress
from adyen.models.vias_name import ViasName

business_details_1 = BusinessDetails1(
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
    registration_number='registrationNumber4',
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
)
```

