
# Us International Ach Priority Requirement

*This model accepts additional fields of type Any.*

## Structure

`UsInternationalAchPriorityRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies that transactions deemed to be International ACH (IAT) per OFAC/NACHA rules cannot have fast priority. |
| `mtype` | [`Type393`](../../doc/models/type-393.md) | Required | **usInternationalAchPriorityRequirement** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_393 import Type393
from adyen.models.us_international_ach_priority_requirement import UsInternationalAchPriorityRequirement

us_international_ach_priority_requirement = UsInternationalAchPriorityRequirement(
    mtype=Type393.USINTERNATIONALACHPRIORITYREQUIREMENT,
    description='description6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

