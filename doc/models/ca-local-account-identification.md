
# Ca Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`CaLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 5- to 12-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `12` |
| `account_type` | [`AccountType`](../../doc/models/account-type.md) | Optional | - |
| `institution_number` | `str` | Required | The 3-digit institution number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `transit_number` | `str` | Required | The 5-digit transit number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `5` |
| `mtype` | [`Type153`](../../doc/models/type-153.md) | Required | **caLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_type import AccountType
from adyen.models.ca_local_account_identification import CaLocalAccountIdentification
from adyen.models.type_153 import Type153

ca_local_account_identification = CaLocalAccountIdentification(
    account_number='accountNumber2',
    institution_number='institutionNumber4',
    transit_number='transitNumber2',
    mtype=Type153.CALOCAL,
    account_type=AccountType.CHECKING,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

