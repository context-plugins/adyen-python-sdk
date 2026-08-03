
# Iban Account Identification Requirement

*This model accepts additional fields of type Any.*

## Structure

`IbanAccountIdentificationRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies the allowed prefixes for the international bank account number as defined in the ISO-13616 standard. |
| `iban_prefixes` | `List[str]` | Optional | Contains the list of allowed prefixes for international bank accounts. For example: NL, US, UK. |
| `mtype` | [`Type303`](../../doc/models/type-303.md) | Required | **ibanAccountIdentificationRequirement** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.iban_account_identification_requirement import IbanAccountIdentificationRequirement
from adyen.models.type_303 import Type303

iban_account_identification_requirement = IbanAccountIdentificationRequirement(
    mtype=Type303.IBANACCOUNTIDENTIFICATIONREQUIREMENT,
    description='description4',
    iban_prefixes=[
        'ibanPrefixes8'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

