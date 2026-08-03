
# Cz Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`CzLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 2- to 16-digit bank account number (Číslo účtu) in the following format:<br><br>- The optional prefix (předčíslí).<br><br>- The required second part (základní část) which must be at least two non-zero digits.<br><br>Examples:<br><br>- **19-123457** (with prefix)<br><br>- **123457** (without prefix)<br><br>- **000019-0000123457** (with prefix, normalized)<br><br>- **000000-0000123457** (without prefix, normalized)<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `17` |
| `bank_code` | `str` | Required | The 4-digit bank code (Kód banky), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |
| `mtype` | [`Type163`](../../doc/models/type-163.md) | Required | **czLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.cz_local_account_identification import CzLocalAccountIdentification
from adyen.models.type_163 import Type163

cz_local_account_identification = CzLocalAccountIdentification(
    account_number='accountNumber8',
    bank_code='bankCode0',
    mtype=Type163.CZLOCAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

