
# Tax Information

*This model accepts additional fields of type Any.*

## Structure

`TaxInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country` | `str` | Optional | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `number` | `str` | Optional | The tax ID number (TIN) of the organization or individual. |
| `number_absent` | `bool` | Optional | Set this to **true** if the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia. |
| `mtype` | `str` | Optional | The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provide **SSN**, **EIN**, or **ITIN** for the US. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.tax_information import TaxInformation

tax_information = TaxInformation(
    country='country0',
    number='number6',
    number_absent=False,
    mtype='type4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

