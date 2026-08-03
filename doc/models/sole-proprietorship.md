
# Sole Proprietorship

*This model accepts additional fields of type Any.*

## Structure

`SoleProprietorship`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_of_governing_law` | `str` | Required | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. |
| `date_of_incorporation` | `str` | Optional | The date when the legal arrangement was incorporated in YYYY-MM-DD format. |
| `doing_business_as` | `str` | Optional | The registered name, if different from the `name`. |
| `doing_business_as_absent` | `bool` | Optional | Set this to **true** if the legal arrangement does not have a `Doing business as` name. |
| `financial_reports` | [`List[FinancialReport]`](../../doc/models/financial-report.md) | Optional | The information from the financial report of the sole proprietorship. |
| `name` | `str` | Required | The legal name. |
| `principal_place_of_business` | [`Address1`](../../doc/models/address-1.md) | Optional | - |
| `registered_address` | [`Address1`](../../doc/models/address-1.md) | Required | - |
| `registration_number` | `str` | Optional | The registration number. |
| `tax_absent` | `bool` | Optional | The tax information is absent. |
| `tax_information` | [`List[TaxInformation]`](../../doc/models/tax-information.md) | Optional | The tax information of the entity. |
| `vat_absence_reason` | [`VatAbsenceReason1`](../../doc/models/vat-absence-reason-1.md) | Optional | - |
| `vat_number` | `str` | Optional | The VAT number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_1 import Address1
from adyen.models.financial_report import FinancialReport
from adyen.models.sole_proprietorship import SoleProprietorship

sole_proprietorship = SoleProprietorship(
    country_of_governing_law='countryOfGoverningLaw6',
    name='name8',
    registered_address=Address1(
        country='country4',
        city='city0',
        postal_code='postalCode8',
        state_or_province='stateOrProvince8',
        street='street0',
        street_2='street24',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    date_of_incorporation='dateOfIncorporation8',
    doing_business_as='doingBusinessAs6',
    doing_business_as_absent=False,
    financial_reports=[
        FinancialReport(
            annual_turnover='annualTurnover4',
            balance_sheet_total='balanceSheetTotal2',
            currency_of_financial_data='currencyOfFinancialData4',
            date_of_financial_data='dateOfFinancialData8',
            employee_count='employeeCount8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        FinancialReport(
            annual_turnover='annualTurnover4',
            balance_sheet_total='balanceSheetTotal2',
            currency_of_financial_data='currencyOfFinancialData4',
            date_of_financial_data='dateOfFinancialData8',
            employee_count='employeeCount8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        FinancialReport(
            annual_turnover='annualTurnover4',
            balance_sheet_total='balanceSheetTotal2',
            currency_of_financial_data='currencyOfFinancialData4',
            date_of_financial_data='dateOfFinancialData8',
            employee_count='employeeCount8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    principal_place_of_business=Address1(
        country='country6',
        city='city8',
        postal_code='postalCode6',
        state_or_province='stateOrProvince0',
        street='street2',
        street_2='street22',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

