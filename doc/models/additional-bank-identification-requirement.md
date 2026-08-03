
# Additional Bank Identification Requirement

*This model accepts additional fields of type Any.*

## Structure

`AdditionalBankIdentificationRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_bank_identification_type` | [`AdditionalBankIdentificationType`](../../doc/models/additional-bank-identification-type.md) | Optional | - |
| `description` | `str` | Optional | The description of the additional bank identification requirement. |
| `mtype` | [`Type610`](../../doc/models/type-610.md) | Required | **additionalBankIdentificationRequirement** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_bank_identification_requirement import AdditionalBankIdentificationRequirement
from adyen.models.additional_bank_identification_type import AdditionalBankIdentificationType
from adyen.models.type_610 import Type610

additional_bank_identification_requirement = AdditionalBankIdentificationRequirement(
    mtype=Type610.ADDITIONALBANKIDENTIFICATIONREQUIREMENT,
    additional_bank_identification_type=AdditionalBankIdentificationType.AUBSBCODE,
    description='description2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

