
# Company 1

Information regarding the company.

## Structure

`Company1`

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
from adyen.models.company_1 import Company1

company_1 = Company1(
    homepage='homepage2',
    name='name6',
    registration_number='registrationNumber6',
    registry_location='registryLocation8',
    tax_id='taxId8'
)
```

