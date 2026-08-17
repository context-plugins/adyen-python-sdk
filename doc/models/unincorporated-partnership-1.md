
# Unincorporated Partnership 1

Information about the unincorporated partnership. Required if `type` is **unincorporatedPartnership**.

## Structure

`UnincorporatedPartnership1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_of_governing_law` | `str` | Required | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. |
| `date_of_incorporation` | `str` | Optional | The date when the legal arrangement was incorporated in YYYY-MM-DD format. |
| `description` | `str` | Optional | Short description about the Legal Arrangement. |
| `doing_business_as` | `str` | Optional | The registered name, if different from the `name`. |
| `doing_business_as_absent` | `bool` | Optional | Set this to **true** if the legal arrangement does not have a `Doing business as` name. |
| `name` | `str` | Required | The legal name. |
| `principal_place_of_business` | [`Address41`](../../doc/models/address-41.md) | Optional | The business address. Required if the principal place of business is different from the `registeredAddress`. |
| `registered_address` | [`Address51`](../../doc/models/address-51.md) | Required | The address registered at the registrar, such as the Chamber of Commerce. |
| `registration_number` | `str` | Optional | The registration number. |
| `tax_information` | [`List[TaxInformation]`](../../doc/models/tax-information.md) | Optional | The tax information of the entity. |
| `mtype` | [`Type191Enum`](../../doc/models/type-191-enum.md) | Optional, Read-only | Type of Partnership.<br><br>Possible values:<br><br>* **limitedPartnership**<br>* **generalPartnership**<br>* **familyPartnership**<br>* **commercialPartnership**<br>* **publicPartnership**<br>* **otherPartnership**<br>* **gbr**<br>* **gmbh**<br>* **kgaa**<br>* **cv**<br>* **vof**<br>* **maatschap**<br>* **privateFundLimitedPartnership**<br>* **businessTrustEntity**<br>* **businessPartnership**<br>* **limitedLiabilityPartnership**<br>* **eg**<br>* **cooperative**<br>* **vos**<br>* **comunidadDeBienes**<br>* **herenciaYacente**<br>* **comunidadDePropietarios**<br>* **sep**<br>* **sca**<br>* **bt**<br>* **kkt**<br>* **scs**<br>* **snc** |
| `vat_absence_reason` | [`VatAbsenceReason1Enum`](../../doc/models/vat-absence-reason-1-enum.md) | Optional | The reason for not providing a VAT number.<br><br>Possible values: **industryExemption**, **belowTaxThreshold**. |
| `vat_number` | `str` | Optional | The VAT number. |

## Example

```python
from adyen.models.address_41 import Address41
from adyen.models.address_51 import Address51
from adyen.models.unincorporated_partnership_1 import UnincorporatedPartnership1

unincorporated_partnership_1 = UnincorporatedPartnership1(
    country_of_governing_law='countryOfGoverningLaw2',
    name='name2',
    registered_address=Address51(
        country='country4',
        city='city0',
        postal_code='postalCode8',
        state_or_province='stateOrProvince8',
        street='street0',
        street_2='street24'
    ),
    date_of_incorporation='dateOfIncorporation2',
    description='description2',
    doing_business_as='doingBusinessAs0',
    doing_business_as_absent=False,
    principal_place_of_business=Address41(
        country='country6',
        city='city8',
        postal_code='postalCode6',
        state_or_province='stateOrProvince0',
        street='street2',
        street_2='street22'
    )
)
```

