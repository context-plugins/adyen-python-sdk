
# Ach Direct Debit

*This model accepts additional fields of type Any.*

## Structure

`AchDirectDebit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_type` | [`AccountHolderType`](../../doc/models/account-holder-type.md) | Optional | - |
| `bank_account_number` | `str` | Optional | The bank account number (without separators). |
| `bank_account_type` | [`BankAccountType`](../../doc/models/bank-account-type.md) | Optional | - |
| `bank_location_id` | `str` | Optional | The bank routing number of the account. The field value is `nil` in most cases. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `encrypted_bank_account_number` | `str` | Optional | Encrypted bank account number. The bank account number (without separators). |
| `encrypted_bank_location_id` | `str` | Optional | Encrypted location id. The bank routing number of the account. The field value is `nil` in most cases. |
| `owner_name` | `str` | Optional | The name of the bank account holder.<br>If you submit a name with non-Latin characters, we automatically replace some of them with corresponding Latin characters to meet the FATF recommendations. For example:<br><br>* χ12 is converted to ch12.<br>* üA is converted to euA.<br>* Peter Møller is converted to Peter Mller, because banks don't accept 'ø'.<br>  After replacement, the ownerName must have at least three alphanumeric characters (A-Z, a-z, 0-9), and at least one of them must be a valid Latin character (A-Z, a-z). For example:<br>* John17 - allowed.<br>* J17 - allowed.<br>* 171 - not allowed.<br>* John-7 - allowed.<br><br>> If provided details don't match the required format, the response returns the error message: 203 'Invalid bank account holder name'. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of your user's verified transfer instrument, which you can use to top up their balance accounts. |
| `mtype` | [`Type9`](../../doc/models/type-9.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_holder_type import AccountHolderType
from adyen.models.ach_direct_debit import AchDirectDebit
from adyen.models.bank_account_type import BankAccountType

ach_direct_debit = AchDirectDebit(
    account_holder_type=AccountHolderType.BUSINESS,
    bank_account_number='bankAccountNumber2',
    bank_account_type=BankAccountType.CHECKING,
    bank_location_id='bankLocationId6',
    checkout_attempt_id='checkoutAttemptId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

