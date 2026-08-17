
# Tax Reporting Classification 2

The tax reporting classification (FATCA/CRS self-certification) of the organization.

## Structure

`TaxReportingClassification2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `business_type` | [`BusinessTypeEnum`](../../doc/models/business-type-enum.md) | Optional | The organization's business type.<br><br>Possible values: **other**, **listedPublicCompany**, **subsidiaryOfListedPublicCompany**, **governmentalOrganization**, **internationalOrganization**, **financialInstitution**. |
| `financial_institution_number` | `str` | Optional | The Global Intermediary Identification Number (GIIN) required for FATCA. Only required if the organization is a US financial institution and the `businessType` is **financialInstitution**. |
| `main_source_of_income` | [`MainSourceOfIncomeEnum`](../../doc/models/main-source-of-income-enum.md) | Optional | The organization's main source of income. Only required if `businessType` is **other**.<br><br>Possible values: **businessOperation**, **realEstateSales**, **investmentInterestOrRoyalty**, **propertyRental**, **other**. |
| `mtype` | [`Type151Enum`](../../doc/models/type-151-enum.md) | Optional | The tax reporting classification type.<br><br>Possible values: **nonFinancialNonReportable**, **financialNonReportable**, **nonFinancialActive**, **nonFinancialPassive**. |

## Example

```python
from adyen.models.business_type_enum import BusinessTypeEnum
from adyen.models.main_source_of_income_enum import MainSourceOfIncomeEnum
from adyen.models.tax_reporting_classification_2 import TaxReportingClassification2
from adyen.models.type_151_enum import Type151Enum

tax_reporting_classification_2 = TaxReportingClassification2(
    business_type=BusinessTypeEnum.SUBSIDIARYOFLISTEDPUBLICCOMPANY,
    financial_institution_number='financialInstitutionNumber8',
    main_source_of_income=MainSourceOfIncomeEnum.PROPERTYRENTAL,
    mtype=Type151Enum.NONFINANCIALNONREPORTABLE
)
```

