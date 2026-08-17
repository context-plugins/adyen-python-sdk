
# Company

## Structure

`Company`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `homepage` | `str` | Optional | The company website's home page. |
| `name` | `str` | Optional | The company name. |
| `registration_number` | `str` | Optional | Registration number of the company. |
| `registry_location` | `str` | Optional | Registry location of the company. |
| `tax_id` | `str` | Optional | Tax ID of the company. |
| `mtype` | `str` | Optional | The company type. |

## Example

```python
from adyen.models.company import Company

company = Company(
    homepage='homepage6',
    name='name0',
    registration_number='registrationNumber2',
    registry_location='registryLocation2',
    tax_id='taxId6'
)
```

