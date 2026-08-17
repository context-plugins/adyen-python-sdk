
# US International Ach Address Requirement

## Structure

`USInternationalAchAddressRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies that you must provide a complete street address for International ACH (IAT) transactions. |
| `mtype` | `str` | Required, Constant | **usInternationalAchAddressRequirement**<br><br>**Value**: `"usInternationalAchAddressRequirement"` |

## Example

```python
from adyen.models.us_international_ach_address_requirement import USInternationalAchAddressRequirement

us_international_ach_address_requirement = USInternationalAchAddressRequirement(
    description='description2'
)
```

