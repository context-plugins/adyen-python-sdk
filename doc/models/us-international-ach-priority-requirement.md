
# US International Ach Priority Requirement

## Structure

`USInternationalAchPriorityRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies that transactions deemed to be International ACH (IAT) per OFAC/NACHA rules cannot have fast priority. |
| `mtype` | `str` | Required, Constant | **usInternationalAchPriorityRequirement**<br><br>**Value**: `"usInternationalAchPriorityRequirement"` |

## Example

```python
from adyen.models.us_international_ach_priority_requirement import USInternationalAchPriorityRequirement

us_international_ach_priority_requirement = USInternationalAchPriorityRequirement(
    description='description6'
)
```

