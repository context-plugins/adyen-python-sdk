
# Address Requirement

*This model accepts additional fields of type Any.*

## Structure

`AddressRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies the required address related fields for a particular route. |
| `required_address_fields` | [`List[RequiredAddressField]`](../../doc/models/required-address-field.md) | Optional | List of address fields. |
| `mtype` | [`Type710`](../../doc/models/type-710.md) | Required | **addressRequirement** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_requirement import AddressRequirement
from adyen.models.required_address_field import RequiredAddressField
from adyen.models.type_710 import Type710

address_requirement = AddressRequirement(
    mtype=Type710.ADDRESSREQUIREMENT,
    description='description2',
    required_address_fields=[
        RequiredAddressField.COUNTRY,
        RequiredAddressField.CITY,
        RequiredAddressField.STATEORPROVINCE
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

