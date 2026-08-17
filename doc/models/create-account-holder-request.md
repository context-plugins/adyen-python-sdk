
# Create Account Holder Request

## Structure

`CreateAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | Your unique identifier for the prospective account holder.<br>The length must be between three (3) and fifty (50) characters long. Only letters, digits, and hyphens (-) are allowed. |
| `account_holder_details` | [`AccountHolderDetails1`](../../doc/models/account-holder-details-1.md) | Required | The details of the prospective account holder. |
| `create_default_account` | `bool` | Optional | If set to **true**, an account with the default options is automatically created for the account holder.<br>By default, this field is set to **true**. |
| `description` | `str` | Optional | A description of the prospective account holder, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores `_`. |
| `legal_entity` | [`LegalEntityEnum`](../../doc/models/legal-entity-enum.md) | Required | The legal entity type of the account holder. This determines the information that should be provided in the request.<br><br>Possible values: **Business**, **Individual**, or **NonProfit**.<br><br>* If set to **Business** or **NonProfit**, then `accountHolderDetails.businessDetails` must be provided, with at least one entry in the `accountHolderDetails.businessDetails.shareholders` list.<br><br>* If set to **Individual**, then `accountHolderDetails.individualDetails` must be provided. |
| `primary_currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals. |
| `processing_tier` | `int` | Optional | The starting [processing tier](https://docs.adyen.com/classic-platforms/onboarding-and-verification/precheck-kyc-information) for the prospective account holder. |
| `verification_profile` | `str` | Optional | The identifier of the profile that applies to this entity. |

## Example

```python
from adyen.models.account_holder_details_1 import AccountHolderDetails1
from adyen.models.bank_account_detail import BankAccountDetail
from adyen.models.business_details_3 import BusinessDetails3
from adyen.models.create_account_holder_request import CreateAccountHolderRequest
from adyen.models.gender_enum import GenderEnum
from adyen.models.legal_entity_enum import LegalEntityEnum
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details_2 import UltimateParentCompanyBusinessDetails2
from adyen.models.vias_address_1 import ViasAddress1
from adyen.models.vias_address_2 import ViasAddress2
from adyen.models.vias_address_9 import ViasAddress9
from adyen.models.vias_name_1 import ViasName1

create_account_holder_request = CreateAccountHolderRequest(
    account_holder_code='accountHolderCode0',
    account_holder_details=AccountHolderDetails1(
        address=ViasAddress9(
            country='country0',
            city='city6',
            house_number_or_name='houseNumberOrName4',
            postal_code='postalCode8',
            state_or_province='stateOrProvince4',
            street='street6'
        ),
        bank_account_details=[
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0'
            ),
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0'
            ),
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0'
            )
        ],
        bank_aggregator_data_reference='bankAggregatorDataReference6',
        business_details=BusinessDetails3(
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
        email='email2',
        full_phone_number='fullPhoneNumber8'
    ),
    legal_entity=LegalEntityEnum.NONPROFIT,
    create_default_account=False,
    description='description6',
    primary_currency='primaryCurrency6',
    processing_tier=202,
    verification_profile='verificationProfile4'
)
```

