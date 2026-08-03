
# Bank Account 11

The details of the bank account, from which the payment should be made.

> Either `bankAccount` or `card` field must be provided in a payment request.

*This model accepts additional fields of type Any.*

## Structure

`BankAccount11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_number` | `str` | Optional | The bank account number (without separators). |
| `bank_city` | `str` | Optional | The bank city. |
| `bank_location_id` | `str` | Optional | The location id of the bank. The field value is `nil` in most cases. |
| `bank_name` | `str` | Optional | The name of the bank. |
| `bic` | `str` | Optional | The [Business Identifier Code](https://en.wikipedia.org/wiki/ISO_9362) (BIC) is the SWIFT address assigned to a bank. The field value is `nil` in most cases. |
| `country_code` | `str` | Optional | Country code where the bank is located.<br><br>A valid value is an ISO two-character country code (e.g. 'NL'). |
| `iban` | `str` | Optional | The [International Bank Account Number](https://en.wikipedia.org/wiki/International_Bank_Account_Number) (IBAN). |
| `owner_name` | `str` | Optional | The name of the bank account holder.<br>If you submit a name with non-Latin characters, we automatically replace some of them with corresponding Latin characters to meet the FATF recommendations. For example:<br><br>* χ12 is converted to ch12.<br>* üA is converted to euA.<br>* Peter Møller is converted to Peter Mller, because banks don't accept 'ø'.<br>  After replacement, the ownerName must have at least three alphanumeric characters (A-Z, a-z, 0-9), and at least one of them must be a valid Latin character (A-Z, a-z). For example:<br>* John17 - allowed.<br>* J17 - allowed.<br>* 171 - not allowed.<br>* John-7 - allowed.<br><br>> If provided details don't match the required format, the response returns the error message: 203 'Invalid bank account holder name'. |
| `tax_id` | `str` | Optional | The bank account holder's tax ID. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_account_11 import BankAccount11

bank_account_11 = BankAccount11(
    bank_account_number='bankAccountNumber2',
    bank_city='bankCity6',
    bank_location_id='bankLocationId6',
    bank_name='bankName2',
    bic='bic4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

