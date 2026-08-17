
# Account Holder Details 4

The details to which the Account Holder should be updated.

Required if a processingTier is not provided.

## Structure

`AccountHolderDetails4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`ViasAddress9`](../../doc/models/vias-address-9.md) | Required | The address of the account holder. |
| `bank_account_details` | [`List[BankAccountDetail]`](../../doc/models/bank-account-detail.md) | Optional | Array of bank accounts associated with the account holder. For details about the required `bankAccountDetail` fields, see [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information). |
| `bank_aggregator_data_reference` | `str` | Optional | The opaque reference value returned by the Adyen API during bank account login. |
| `business_details` | [`BusinessDetails3`](../../doc/models/business-details-3.md) | Optional | Details about the business or nonprofit account holder.<br>Required when creating an account holder with `legalEntity` **Business** or **NonProfit**. |
| `email` | `str` | Optional | The email address of the account holder. |
| `full_phone_number` | `str` | Optional | The phone number of the account holder provided as a single string. It will be handled as a landline phone.<br>**Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344" |
| `individual_details` | [`IndividualDetails3`](../../doc/models/individual-details-3.md) | Optional | Details about the individual account holder.<br>Required when creating an account holder with `legalEntity` **Individual**. |
| `last_review_date` | `str` | Optional | Date when you last reviewed the account holder's information, in ISO-8601 YYYY-MM-DD format. For example, **2020-01-31**. |
| `legal_arrangements` | [`List[LegalArrangementDetail]`](../../doc/models/legal-arrangement-detail.md) | Optional | An array containing information about the account holder's [legal arrangements](https://docs.adyen.com/classic-platforms/verification-process/legal-arrangements). |
| `merchant_category_code` | `str` | Optional | The Merchant Category Code of the account holder.<br><br>> If not specified in the request, this will be derived from the platform account (which is configured by Adyen). |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs for general use by the account holder or merchant.<br>The keys do not have specific names and may be used for storing miscellaneous data as desired.<br><br>> The values being stored have a maximum length of eighty (80) characters and will be truncated if necessary.<br>> Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| `payout_methods` | [`List[PayoutMethod]`](../../doc/models/payout-method.md) | Optional | Array of tokenized card details associated with the account holder. For details about how you can use the tokens to pay out, refer to [Pay out to cards](https://docs.adyen.com/classic-platforms/payout-to-cards). |
| `phone_number` | [`ViasPhoneNumber3`](../../doc/models/vias-phone-number-3.md) | Optional | The phone number of the account holder.<br><br>> Required if a `fullPhoneNumber` is not provided. |
| `principal_business_address` | [`ViasAddress6`](../../doc/models/vias-address-6.md) | Optional | The principal business address of the account holder. |
| `store_details` | [`List[StoreDetail]`](../../doc/models/store-detail.md) | Optional | Array of stores associated with the account holder. Required when onboarding account holders that have an Adyen [point of sale](https://docs.adyen.com/classic-platforms/platforms-for-pos). |
| `web_address` | `str` | Optional | The URL of the website of the account holder. |

## Example

```python
from adyen.models.account_holder_details_4 import AccountHolderDetails4
from adyen.models.bank_account_detail import BankAccountDetail
from adyen.models.business_details_3 import BusinessDetails3
from adyen.models.gender_enum import GenderEnum
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details_2 import UltimateParentCompanyBusinessDetails2
from adyen.models.vias_address_1 import ViasAddress1
from adyen.models.vias_address_2 import ViasAddress2
from adyen.models.vias_address_9 import ViasAddress9
from adyen.models.vias_name_1 import ViasName1

account_holder_details_4 = AccountHolderDetails4(
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
        )
    ],
    bank_aggregator_data_reference='bankAggregatorDataReference4',
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
    email='email4',
    full_phone_number='fullPhoneNumber6'
)
```

