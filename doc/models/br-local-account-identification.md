
# Br Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`BrLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `10` |
| `bank_code` | `str` | Required | The 3-digit bank code, with leading zeros.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `branch_number` | `str` | Required | The bank account branch number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `4` |
| `ispb` | `str` | Optional | The 8-digit ISPB, with leading zeros.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `8` |
| `mtype` | [`Type146`](../../doc/models/type-146.md) | Required | **brLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.br_local_account_identification import BrLocalAccountIdentification
from adyen.models.type_146 import Type146

br_local_account_identification = BrLocalAccountIdentification(
    account_number='accountNumber6',
    bank_code='bankCode6',
    branch_number='branchNumber6',
    mtype=Type146.BRLOCAL,
    ispb='ispb0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

