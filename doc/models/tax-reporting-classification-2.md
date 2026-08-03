
# Tax Reporting Classification 2

The tax reporting classification (FATCA/CRS self-certification) of the organization.

*This model accepts additional fields of type Any.*

## Structure

`TaxReportingClassification2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `business_type` | [`BusinessType`](../../doc/models/business-type.md) | Optional | - |
| `financial_institution_number` | `str` | Optional | The Global Intermediary Identification Number (GIIN) required for FATCA. Only required if the organization is a US financial institution and the `businessType` is **financialInstitution**. |
| `main_source_of_income` | [`MainSourceOfIncome`](../../doc/models/main-source-of-income.md) | Optional | - |
| `mtype` | [`Type151`](../../doc/models/type-151.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.business_type import BusinessType
from adyen.models.main_source_of_income import MainSourceOfIncome
from adyen.models.tax_reporting_classification_2 import TaxReportingClassification2
from adyen.models.type_151 import Type151

tax_reporting_classification_2 = TaxReportingClassification2(
    business_type=BusinessType.SUBSIDIARYOFLISTEDPUBLICCOMPANY,
    financial_institution_number='financialInstitutionNumber8',
    main_source_of_income=MainSourceOfIncome.PROPERTYRENTAL,
    mtype=Type151.NONFINANCIALNONREPORTABLE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

