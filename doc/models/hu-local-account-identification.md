
# Hu Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`HuLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 24-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `24`, *Maximum Length*: `24` |
| `mtype` | [`Type193`](../../doc/models/type-193.md) | Required | **huLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.hu_local_account_identification import HuLocalAccountIdentification
from adyen.models.type_193 import Type193

hu_local_account_identification = HuLocalAccountIdentification(
    account_number='accountNumber4',
    mtype=Type193.HULOCAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

