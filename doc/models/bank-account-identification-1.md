
# Bank Account Identification 1

Contains the identification information of the account to which you can transfer funds related to repayments.

*This model accepts additional fields of type Any.*

## Structure

`BankAccountIdentification1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_account_identification_1 import BankAccountIdentification1

bank_account_identification_1 = BankAccountIdentification1(
    mtype='BankAccountIdentification1',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

