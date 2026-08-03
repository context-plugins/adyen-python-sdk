
# Bank Identification

*This model accepts additional fields of type Any.*

## Structure

`BankIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country` | `str` | Optional | Two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
| `identification` | `str` | Optional | The bank identification code. |
| `identification_type` | [`IdentificationType`](../../doc/models/identification-type.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_identification import BankIdentification
from adyen.models.identification_type import IdentificationType

bank_identification = BankIdentification(
    country='country6',
    identification='identification0',
    identification_type=IdentificationType.BIC,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

