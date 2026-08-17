
# Organization

## Structure

`Organization`

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
| `institutional_sector` | [`InstitutionalSectorEnum`](../../doc/models/institutional-sector-enum.md) | Optional | The institutional sector the organization operates within. |
| `legal_form` | `str` | Optional | The type of business entity as defined in the national legal system. Use a legal form listed within the accepted legal forms compiled by the Central Bank of Europe. |
| `legal_name` | `str` | Required | The organization's legal name. |
| `phone` | [`PhoneNumber2`](../../doc/models/phone-number-2.md) | Optional | The phone number of the legal entity. |
| `principal_place_of_business` | [`Address22`](../../doc/models/address-22.md) | Optional | The address where the organization operates from. Provide this if the principal place of business is different from the `registeredAddress`. |
| `registered_address` | [`Address31`](../../doc/models/address-31.md) | Required | The address of the organization registered at their registrar (such as the Chamber of Commerce). |
| `registration_number` | `str` | Optional | The organization's registration number. |
| `registration_number_absent` | `bool` | Optional | Set this to **true** if the organization does not have a registration number available. Only applicable for organizations in New Zealand, and incorporated partnerships and government organizations in Australia. |
| `status_of_legal_proceeding` | [`StatusOfLegalProceedingEnum`](../../doc/models/status-of-legal-proceeding-enum.md) | Optional | The status of any current or past legal action taken against the legal entity.<br><br>Possible values: **noLegalActionsTaken**, **underJudicialAdministration**, **bankruptcyInsolvency**, **otherLegalMeasures**<br><br>If the value of this field is **noLegalActionsTaken**, then `dateOfInitiationOfLegalProceeding` is not required. Otherwise, it is required. |
| `stock_data` | [`StockData2`](../../doc/models/stock-data-2.md) | Optional | Information about the organization's publicly traded stock. Provide this object only if `type` is **listedPublicCompany**. |
| `support` | [`Support1`](../../doc/models/support-1.md) | Optional | Support information for the legal entity. Required if you have a platform setup. |
| `tax_information` | [`List[TaxInformation]`](../../doc/models/tax-information.md) | Optional | The tax information of the organization. |
| `tax_reporting_classification` | [`TaxReportingClassification2`](../../doc/models/tax-reporting-classification-2.md) | Optional | The tax reporting classification (FATCA/CRS self-certification) of the organization. |
| `mtype` | [`Type161Enum`](../../doc/models/type-161-enum.md) | Optional | Type of organization.<br><br>Possible values: **associationIncorporated**, **governmentalOrganization**, **listedPublicCompany**, **nonProfit**, **partnershipIncorporated**, **privateCompany**. |
| `vat_absence_reason` | [`VatAbsenceReasonEnum`](../../doc/models/vat-absence-reason-enum.md) | Optional | The reason the organization has not provided a VAT number.<br><br>Possible values: **industryExemption**, **belowTaxThreshold**. |
| `vat_number` | `str` | Optional | The organization's VAT number. |
| `web_data` | [`WebData1`](../../doc/models/web-data-1.md) | Optional | The website and app URL of the legal entity. |

## Example

```python
from adyen.models.address_31 import Address31
from adyen.models.organization import Organization

organization = Organization(
    legal_name='legalName2',
    registered_address=Address31(
        country='country4',
        city='city0',
        postal_code='postalCode8',
        state_or_province='stateOrProvince8',
        street='street0',
        street_2='street24'
    ),
    country_of_governing_law='countryOfGoverningLaw8',
    date_of_incorporation='dateOfIncorporation4',
    date_of_initiation_of_legal_proceeding='dateOfInitiationOfLegalProceeding6',
    description='description6',
    doing_business_as='doingBusinessAs4'
)
```

