
# Nz Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`NzLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 15-16 digit bank account number. The first 2 digits are the bank number, the next 4 digits are the branch number, the next 7 digits are the account number, and the final 2-3 digits are the suffix.<br><br>**Constraints**: *Minimum Length*: `15`, *Maximum Length*: `16` |
| `mtype` | [`Type233`](../../doc/models/type-233.md) | Required | **nzLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.nz_local_account_identification import NzLocalAccountIdentification
from adyen.models.type_233 import Type233

nz_local_account_identification = NzLocalAccountIdentification(
    account_number='accountNumber0',
    mtype=Type233.NZLOCAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

