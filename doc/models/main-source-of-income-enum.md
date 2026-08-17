
# Main Source of Income Enum

The organization's main source of income. Only required if `businessType` is **other**.

Possible values: **businessOperation**, **realEstateSales**, **investmentInterestOrRoyalty**, **propertyRental**, **other**.

## Enumeration

`MainSourceOfIncomeEnum`

## Fields

| Name |
|  --- |
| `BUSINESSOPERATION` |
| `REALESTATESALES` |
| `INVESTMENTINTERESTORROYALTY` |
| `PROPERTYRENTAL` |
| `OTHER` |

## Example

```python
from adyen.models.main_source_of_income_enum import MainSourceOfIncomeEnum

main_source_of_income = MainSourceOfIncomeEnum.BUSINESSOPERATION
```

