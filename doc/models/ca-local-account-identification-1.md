
# Ca Local Account Identification 1

*This model accepts additional fields of type Any.*

## Structure

`CaLocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 5- to 12-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `12` |
| `account_type` | [`AccountType`](../../doc/models/account-type.md) | Optional | - |
| `institution_number` | `str` | Required | The 3-digit institution number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `transit_number` | `str` | Required | The 5-digit transit number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `5` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_type import AccountType
from adyen.models.bank_account_identification import CaLocalAccountIdentification1

ca_local_account_identification_1 = CaLocalAccountIdentification1(
    account_number='accountNumber8',
    institution_number='institutionNumber2',
    transit_number='transitNumber8',
    account_type=AccountType.CHECKING,
    mtype='caLocal',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

