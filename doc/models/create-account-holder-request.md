
# Create Account Holder Request

*This model accepts additional fields of type Any.*

## Structure

`CreateAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | Your unique identifier for the prospective account holder.<br>The length must be between three (3) and fifty (50) characters long. Only letters, digits, and hyphens (-) are allowed. |
| `account_holder_details` | [`AccountHolderDetails`](../../doc/models/account-holder-details.md) | Required | - |
| `create_default_account` | `bool` | Optional | If set to **true**, an account with the default options is automatically created for the account holder.<br>By default, this field is set to **true**. |
| `description` | `str` | Optional | A description of the prospective account holder, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores `_`. |
| `legal_entity` | [`LegalEntity`](../../doc/models/legal-entity.md) | Required | - |
| `primary_currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals. |
| `processing_tier` | `int` | Optional | The starting [processing tier](https://docs.adyen.com/classic-platforms/onboarding-and-verification/precheck-kyc-information) for the prospective account holder. |
| `verification_profile` | `str` | Optional | The identifier of the profile that applies to this entity. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_holder_details import AccountHolderDetails
from adyen.models.bank_account_detail import BankAccountDetail
from adyen.models.business_details import BusinessDetails
from adyen.models.create_account_holder_request import CreateAccountHolderRequest
from adyen.models.gender import Gender
from adyen.models.legal_entity import LegalEntity
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details import UltimateParentCompanyBusinessDetails
from adyen.models.vias_address import ViasAddress
from adyen.models.vias_name import ViasName

create_account_holder_request = CreateAccountHolderRequest(
    account_holder_code='accountHolderCode0',
    account_holder_details=AccountHolderDetails(
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
        bank_account_details=[
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        bank_aggregator_data_reference='bankAggregatorDataReference6',
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
        email='email2',
        full_phone_number='fullPhoneNumber8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    legal_entity=LegalEntity.NONPROFIT,
    create_default_account=False,
    description='description6',
    primary_currency='primaryCurrency6',
    processing_tier=202,
    verification_profile='verificationProfile4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

