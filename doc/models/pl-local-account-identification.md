
# Pl Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`PlLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 26-digit bank account number ([Numer rachunku](https://pl.wikipedia.org/wiki/Numer_Rachunku_Bankowego)), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `26`, *Maximum Length*: `26` |
| `mtype` | [`Type256`](../../doc/models/type-256.md) | Required | **plLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pl_local_account_identification import PlLocalAccountIdentification
from adyen.models.type_256 import Type256

pl_local_account_identification = PlLocalAccountIdentification(
    account_number='accountNumber0',
    mtype=Type256.PLLOCAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

