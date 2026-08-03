
# Dk Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`DkLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 4-10 digits bank account number (Kontonummer) (without separators or whitespace).<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `10` |
| `bank_code` | `str` | Required | The 4-digit bank code (Registreringsnummer) (without separators or whitespace).<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |
| `mtype` | [`Type173`](../../doc/models/type-173.md) | Required | **dkLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.dk_local_account_identification import DkLocalAccountIdentification
from adyen.models.type_173 import Type173

dk_local_account_identification = DkLocalAccountIdentification(
    account_number='accountNumber0',
    bank_code='bankCode2',
    mtype=Type173.DKLOCAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

