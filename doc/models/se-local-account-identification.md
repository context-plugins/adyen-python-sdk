
# Se Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`SeLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 7- to 10-digit bank account number ([Bankkontonummer](https://sv.wikipedia.org/wiki/Bankkonto)), without the clearing number, separators, or whitespace.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `10` |
| `clearing_number` | `str` | Required | The 4- to 5-digit clearing number ([Clearingnummer](https://sv.wikipedia.org/wiki/Clearingnummer)), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `5` |
| `mtype` | [`Type264`](../../doc/models/type-264.md) | Required | **seLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.se_local_account_identification import SeLocalAccountIdentification
from adyen.models.type_264 import Type264

se_local_account_identification = SeLocalAccountIdentification(
    account_number='accountNumber2',
    clearing_number='clearingNumber0',
    mtype=Type264.SELOCAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

