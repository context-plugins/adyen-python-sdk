
# Bank Account Detail 1

*This model accepts additional fields of type Any.*

## Structure

`BankAccountDetail1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | The bank account number (without separators).<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `account_type` | `str` | Optional | The type of bank account.<br>Only applicable to bank accounts held in the USA.<br>The permitted values are: `checking`, `savings`.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `bank_account_name` | `str` | Optional | The name of the bank account. |
| `bank_account_reference` | `str` | Optional | Merchant reference to the bank account. |
| `bank_account_uuid` | `str` | Optional | The unique identifier (UUID) of the Bank Account.<br><br>> If, during an account holder create or update request, this field is left blank (but other fields provided), a new Bank Account will be created with a procedurally-generated UUID.<br><br>> If, during an account holder create request, a UUID is provided, the creation of the Bank Account will fail while the creation of the account holder will continue.<br><br>> If, during an account holder update request, a UUID that is not correlated with an existing Bank Account is provided, the update of the account holder will fail.<br><br>> If, during an account holder update request, a UUID that is correlated with an existing Bank Account is provided, the existing Bank Account will be updated. |
| `bank_bic_swift` | `str` | Optional | The bank identifier code.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `bank_city` | `str` | Optional | The city in which the bank branch is located.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `bank_code` | `str` | Optional | The bank code of the banking institution with which the bank account is registered.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `bank_name` | `str` | Optional | The name of the banking institution with which the bank account is held.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `branch_code` | `str` | Optional | The branch code of the branch under which the bank account is registered. The value to be specified in this parameter depends on the country of the bank account:<br><br>* United States - Routing number<br>* United Kingdom - Sort code<br>* Germany - Bankleitzahl<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `check_code` | `str` | Optional | The check code of the bank account.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `country_code` | `str` | Optional | The two-letter country code in which the bank account is registered.<br><br>> The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `currency_code` | `str` | Optional | The currency in which the bank account deals.<br><br>> The permitted currency codes are defined in ISO-4217 (e.g. 'EUR'). |
| `iban` | `str` | Optional | The international bank account number.<br><br>> The IBAN standard is defined in ISO-13616.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `owner_city` | `str` | Optional | The city of residence of the bank account owner.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `owner_country_code` | `str` | Optional | The country code of the country of residence of the bank account owner.<br><br>> The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `owner_date_of_birth` | `str` | Optional | The date of birth of the bank account owner.<br>The date should be in ISO-8601 format yyyy-mm-dd (e.g. 2000-01-31). |
| `owner_house_number_or_name` | `str` | Optional | The house name or number of the residence of the bank account owner.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `owner_name` | `str` | Optional | The name of the bank account owner.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `owner_nationality` | `str` | Optional | The country code of the country of nationality of the bank account owner.<br><br>> The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `owner_postal_code` | `str` | Optional | The postal code of the residence of the bank account owner.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `owner_state` | `str` | Optional | The state of residence of the bank account owner.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `owner_street` | `str` | Optional | The street name of the residence of the bank account owner.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `primary_account` | `bool` | Optional | If set to true, the bank account is a primary account. |
| `tax_id` | `str` | Optional | The tax ID number.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `url_for_verification` | `str` | Optional | The URL to be used for bank account verification.<br>This may be generated on bank account creation.<br><br>> Refer to [Required information](https://docs.adyen.com/classic-platforms/verification-process/required-information) for details on field requirements. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_account_detail_1 import BankAccountDetail1

bank_account_detail_1 = BankAccountDetail1(
    account_number='accountNumber6',
    account_type='accountType8',
    bank_account_name='bankAccountName0',
    bank_account_reference='bankAccountReference0',
    bank_account_uuid='bankAccountUUID4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

