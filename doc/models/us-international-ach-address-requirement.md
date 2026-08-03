
# Us International Ach Address Requirement

*This model accepts additional fields of type Any.*

## Structure

`UsInternationalAchAddressRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies that you must provide a complete street address for International ACH (IAT) transactions. |
| `mtype` | [`Type383`](../../doc/models/type-383.md) | Required | **usInternationalAchAddressRequirement** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_383 import Type383
from adyen.models.us_international_ach_address_requirement import UsInternationalAchAddressRequirement

us_international_ach_address_requirement = UsInternationalAchAddressRequirement(
    mtype=Type383.USINTERNATIONALACHADDRESSREQUIREMENT,
    description='description2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

