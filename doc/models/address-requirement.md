
# Address Requirement

## Structure

`AddressRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies the required address related fields for a particular route. |
| `required_address_fields` | [`List[RequiredAddressFieldEnum]`](../../doc/models/required-address-field-enum.md) | Optional | List of address fields. |
| `mtype` | `str` | Required, Constant | **addressRequirement**<br><br>**Value**: `"addressRequirement"` |

## Example

```python
from adyen.models.address_requirement import AddressRequirement
from adyen.models.required_address_field_enum import RequiredAddressFieldEnum

address_requirement = AddressRequirement(
    description='description2',
    required_address_fields=[
        RequiredAddressFieldEnum.COUNTRY,
        RequiredAddressFieldEnum.CITY,
        RequiredAddressFieldEnum.STATEORPROVINCE
    ]
)
```

