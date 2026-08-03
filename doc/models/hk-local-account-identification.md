
# Hk Local Account Identification

*This model accepts additional fields of type Any.*

## Structure

`HkLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 9- to 17-digit bank account number, without separators or whitespace. Starts with the 3-digit branch code.<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `17` |
| `clearing_code` | `str` | Required | The 3-digit clearing code, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `mtype` | [`Type1810`](../../doc/models/type-1810.md) | Required | **hkLocal** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.hk_local_account_identification import HkLocalAccountIdentification
from adyen.models.type_1810 import Type1810

hk_local_account_identification = HkLocalAccountIdentification(
    account_number='accountNumber4',
    clearing_code='clearingCode0',
    mtype=Type1810.HKLOCAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

