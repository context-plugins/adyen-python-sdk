
# Account Holder Details

*This model accepts additional fields of type Any.*

## Structure

`AccountHolderDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`ViasAddress`](../../doc/models/vias-address.md) | Required | - |
| `bank_account_details` | [`List[BankAccountDetail]`](../../doc/models/bank-account-detail.md) | Optional | Array of bank accounts associated with the account holder. For details about the required `bankAccountDetail` fields, see [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information). |
| `bank_aggregator_data_reference` | `str` | Optional | The opaque reference value returned by the Adyen API during bank account login. |
| `business_details` | [`BusinessDetails`](../../doc/models/business-details.md) | Optional | - |
| `email` | `str` | Optional | The email address of the account holder. |
| `full_phone_number` | `str` | Optional | The phone number of the account holder provided as a single string. It will be handled as a landline phone.<br>**Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344" |
| `individual_details` | [`IndividualDetails`](../../doc/models/individual-details.md) | Optional | - |
| `last_review_date` | `str` | Optional | Date when you last reviewed the account holder's information, in ISO-8601 YYYY-MM-DD format. For example, **2020-01-31**. |
| `legal_arrangements` | [`List[LegalArrangementDetail]`](../../doc/models/legal-arrangement-detail.md) | Optional | An array containing information about the account holder's [legal arrangements](https://docs.adyen.com/classic-platforms/verification-process/legal-arrangements). |
| `merchant_category_code` | `str` | Optional | The Merchant Category Code of the account holder.<br><br>> If not specified in the request, this will be derived from the platform account (which is configured by Adyen). |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs for general use by the account holder or merchant.<br>The keys do not have specific names and may be used for storing miscellaneous data as desired.<br><br>> The values being stored have a maximum length of eighty (80) characters and will be truncated if necessary.<br>> Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| `payout_methods` | [`List[PayoutMethod]`](../../doc/models/payout-method.md) | Optional | Array of tokenized card details associated with the account holder. For details about how you can use the tokens to pay out, refer to [Pay out to cards](https://docs.adyen.com/classic-platforms/payout-to-cards). |
| `phone_number` | [`PhoneNumber3`](../../doc/models/phone-number-3.md) | Optional | - |
| `principal_business_address` | [`ViasAddress`](../../doc/models/vias-address.md) | Optional | - |
| `store_details` | [`List[StoreDetail]`](../../doc/models/store-detail.md) | Optional | Array of stores associated with the account holder. Required when onboarding account holders that have an Adyen [point of sale](https://docs.adyen.com/classic-platforms/platforms-for-pos). |
| `web_address` | `str` | Optional | The URL of the website of the account holder. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_holder_details import AccountHolderDetails
from adyen.models.bank_account_detail import BankAccountDetail
from adyen.models.business_details import BusinessDetails
from adyen.models.gender import Gender
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details import UltimateParentCompanyBusinessDetails
from adyen.models.vias_address import ViasAddress
from adyen.models.vias_name import ViasName

account_holder_details = AccountHolderDetails(
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
)
```

