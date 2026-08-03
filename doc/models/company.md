
# Company

*This model accepts additional fields of type Any.*

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
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.company import Company

company = Company(
    homepage='homepage6',
    name='name0',
    registration_number='registrationNumber2',
    registry_location='registryLocation2',
    tax_id='taxId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

