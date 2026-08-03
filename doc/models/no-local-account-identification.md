
# No Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`NoLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 11-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `11`, *Maximum Length*: `11` |
| `mtype` | [`Type223`](../../doc/models/type-223.md) | Required | **noLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.no_local_account_identification import NoLocalAccountIdentification
from adyen.models.type_223 import Type223

no_local_account_identification = NoLocalAccountIdentification(
    account_number='accountNumber6',
    mtype=Type223.NOLOCAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

