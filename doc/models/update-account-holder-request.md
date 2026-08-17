
# Update Account Holder Request

## Structure

`UpdateAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder to be updated. |
| `account_holder_details` | [`AccountHolderDetails4`](../../doc/models/account-holder-details-4.md) | Optional | The details to which the Account Holder should be updated.<br><br>Required if a processingTier is not provided. |
| `description` | `str` | Optional | A description of the account holder, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores `_`. |
| `legal_entity` | [`LegalEntityEnum`](../../doc/models/legal-entity-enum.md) | Optional | The legal entity type of the account holder. This determines the information that should be provided in the request.<br><br>Possible values: **Business**, **Individual**, or **NonProfit**.<br><br>* If set to **Business** or **NonProfit**, then `accountHolderDetails.businessDetails` must be provided, with at least one entry in the `accountHolderDetails.businessDetails.shareholders` list.<br><br>* If set to **Individual**, then `accountHolderDetails.individualDetails` must be provided. |
| `primary_currency` | `str` | Optional | The primary three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), to which the account holder should be updated. |
| `processing_tier` | `int` | Optional | The processing tier to which the Account Holder should be updated.<br><br>> The processing tier can not be lowered through this request.<br><br>> Required if accountHolderDetails are not provided. |
| `verification_profile` | `str` | Optional | The identifier of the profile that applies to this entity. |

## Example

```python
from adyen.models.account_holder_details_4 import AccountHolderDetails4
from adyen.models.bank_account_detail import BankAccountDetail
from adyen.models.business_details_3 import BusinessDetails3
from adyen.models.gender_enum import GenderEnum
from adyen.models.legal_entity_enum import LegalEntityEnum
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details_2 import UltimateParentCompanyBusinessDetails2
from adyen.models.update_account_holder_request import UpdateAccountHolderRequest
from adyen.models.vias_address_1 import ViasAddress1
from adyen.models.vias_address_2 import ViasAddress2
from adyen.models.vias_address_9 import ViasAddress9
from adyen.models.vias_name_1 import ViasName1

update_account_holder_request = UpdateAccountHolderRequest(
    account_holder_code='accountHolderCode2',
    account_holder_details=AccountHolderDetails4(
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
    description='description8',
    legal_entity=LegalEntityEnum.BUSINESS,
    primary_currency='primaryCurrency4',
    processing_tier=70
)
```

