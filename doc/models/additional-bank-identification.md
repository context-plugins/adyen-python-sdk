
# Additional Bank Identification

*This model accepts additional fields of type Any.*

## Structure

`AdditionalBankIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The value of the additional bank identification. |
| `mtype` | [`AdditionalBankIdentificationType`](../../doc/models/additional-bank-identification-type.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_bank_identification import AdditionalBankIdentification
from adyen.models.additional_bank_identification_type import AdditionalBankIdentificationType

additional_bank_identification = AdditionalBankIdentification(
    code='code4',
    mtype=AdditionalBankIdentificationType.AUBSBCODE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

