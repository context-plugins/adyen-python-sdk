
# Organization 1

Information about the organization. Required if `type` is **organization**.

*This model accepts additional fields of type Any.*

## Structure

`Organization1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_of_governing_law` | `str` | Optional | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. |
| `date_of_incorporation` | `str` | Optional | The date when the organization was incorporated in YYYY-MM-DD format. |
| `date_of_initiation_of_legal_proceeding` | `str` | Optional | Required if the value of `statusOfLegalProceeding` is one of the following:<br><br>**underJudicialAdministration**, **bankruptcyInsolvency**, **otherLegalMeasures**<br><br>The date at which a legal proceeding was initiated, in **YYYY-MM-DD** format. Example: **2000-02-12** |
| `description` | `str` | Optional | Your description for the organization. |
| `doing_business_as` | `str` | Optional | The organization's trading name, if different from the registered legal name. |
| `doing_business_as_absent` | `bool` | Optional | Set this to **true** if the organization or legal arrangement does not have a `Doing business as` name. |
| `economic_sector` | `str` | Optional | The sector of the economy the legal entity operates within, represented by a 2-4 digit code that may include a ".". Example: 45.11<br><br>You can locate economic sector codes for your area by referencing codes defined by the NACE (Nomenclature of Economic Activities) used in the European Union. |
| `email` | `str` | Optional | The email address of the legal entity. |
| `financial_reports` | [`List[FinancialReport]`](../../doc/models/financial-report.md) | Optional | The financial report information of the organization. |
| `global_legal_entity_identifier` | `str` | Optional | The global legal entity identifier for the organization.<br><br>This field is not required if the `registrationNumber` for the organization has been provided. |
| `head_office_indicator` | `bool` | Optional | Indicates that the registered business address is also the company's headquarters. |
| `institutional_sector` | [`InstitutionalSector`](../../doc/models/institutional-sector.md) | Optional | - |
| `legal_form` | `str` | Optional | The type of business entity as defined in the national legal system. Use a legal form listed within the accepted legal forms compiled by the Central Bank of Europe. |
| `legal_name` | `str` | Required | The organization's legal name. |
| `phone` | [`PhoneNumber`](../../doc/models/phone-number.md) | Optional | - |
| `principal_place_of_business` | [`Address1`](../../doc/models/address-1.md) | Optional | - |
| `registered_address` | [`Address1`](../../doc/models/address-1.md) | Required | - |
| `registration_number` | `str` | Optional | The organization's registration number. |
| `registration_number_absent` | `bool` | Optional | Set this to **true** if the organization does not have a registration number available. Only applicable for organizations in New Zealand, and incorporated partnerships and government organizations in Australia. |
| `status_of_legal_proceeding` | [`StatusOfLegalProceeding`](../../doc/models/status-of-legal-proceeding.md) | Optional | - |
| `stock_data` | [`StockData`](../../doc/models/stock-data.md) | Optional | - |
| `support` | [`Support`](../../doc/models/support.md) | Optional | - |
| `tax_information` | [`List[TaxInformation]`](../../doc/models/tax-information.md) | Optional | The tax information of the organization. |
| `tax_reporting_classification` | [`TaxReportingClassification`](../../doc/models/tax-reporting-classification.md) | Optional | - |
| `mtype` | [`Type161`](../../doc/models/type-161.md) | Optional | - |
| `vat_absence_reason` | [`VatAbsenceReason`](../../doc/models/vat-absence-reason.md) | Optional | - |
| `vat_number` | `str` | Optional | The organization's VAT number. |
| `web_data` | [`WebData`](../../doc/models/web-data.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_1 import Address1
from adyen.models.organization_1 import Organization1

organization_1 = Organization1(
    legal_name='legalName8',
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
    country_of_governing_law='countryOfGoverningLaw8',
    date_of_incorporation='dateOfIncorporation6',
    date_of_initiation_of_legal_proceeding='dateOfInitiationOfLegalProceeding6',
    description='description6',
    doing_business_as='doingBusinessAs4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

