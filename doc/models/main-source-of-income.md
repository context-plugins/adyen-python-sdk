
# Main Source of Income

The organization's main source of income. Only required if `businessType` is **other**.

Possible values: **businessOperation**, **realEstateSales**, **investmentInterestOrRoyalty**, **propertyRental**, **other**.

## Enumeration

`MainSourceOfIncome`

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
from adyen.models.main_source_of_income import MainSourceOfIncome

main_source_of_income = MainSourceOfIncome.BUSINESSOPERATION
```

