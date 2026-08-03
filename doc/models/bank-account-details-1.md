
# Bank Account Details 1

Contains the business account details. Returned when you create a payment instrument with `type` **bankAccount**.

*This model accepts additional fields of type Any.*

## Structure

`BankAccountDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | The bank account number, without separators or whitespace. |
| `account_type` | `str` | Optional | The bank account type.<br><br>Possible values: **checking** or **savings**. Defaults to **checking**.<br><br>**Default**: `"checking"` |
| `branch_number` | `str` | Optional | The bank account branch number, without separators or whitespace |
| `form_factor` | `str` | Optional | Business accounts with a `formFactor` value of **physical** are business accounts issued under the central bank of that country. The default value is **physical** for NL, US, and UK business accounts.<br><br>Adyen creates a local IBAN for business accounts when the `formFactor` value is set to **virtual**. The local IBANs that are supported are for DE and FR, which reference a physical NL account, with funds being routed through the central bank of NL.<br><br>**Default**: `"physical"` |
| `iban` | `str` | Optional | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. |
| `routing_number` | `str` | Optional | The [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace. |
| `sort_code` | `str` | Optional | The [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace. |
| `mtype` | `str` | Required | **iban** or **usLocal** or **ukLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_account_details_1 import BankAccountDetails1

bank_account_details_1 = BankAccountDetails1(
    mtype='type4',
    account_number='accountNumber6',
    account_type='checking',
    branch_number='branchNumber6',
    form_factor='physical',
    iban='iban0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

