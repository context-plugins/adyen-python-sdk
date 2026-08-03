
# Additional Bank Identification 1

Additional identification codes of the bank. Some banks may require these identifiers for cross-border transfers.

*This model accepts additional fields of type Any.*

## Structure

`AdditionalBankIdentification1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The value of the additional bank identification. |
| `mtype` | [`AdditionalBankIdentificationType`](../../doc/models/additional-bank-identification-type.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_bank_identification_1 import AdditionalBankIdentification1
from adyen.models.additional_bank_identification_type import AdditionalBankIdentificationType

additional_bank_identification_1 = AdditionalBankIdentification1(
    code='code4',
    mtype=AdditionalBankIdentificationType.GBSORTCODE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

