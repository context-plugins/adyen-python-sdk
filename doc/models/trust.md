
# Trust

## Structure

`Trust`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_of_governing_law` | `str` | Required | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. |
| `date_of_incorporation` | `str` | Optional | The date when the legal arrangement was incorporated in YYYY-MM-DD format. |
| `description` | `str` | Optional | A short description about the trust. Only applicable for charitable trusts in New Zealand. |
| `doing_business_as` | `str` | Optional | The registered name, if different from the `name`. |
| `doing_business_as_absent` | `bool` | Optional | Set this to **true** if the legal arrangement does not have a `Doing business as` name. |
| `name` | `str` | Required | The legal name. |
| `principal_place_of_business` | [`Address41`](../../doc/models/address-41.md) | Optional | The business address. Required if the principal place of business is different from the `registeredAddress`. |
| `registered_address` | [`Address51`](../../doc/models/address-51.md) | Required | The address registered at the registrar, such as the Chamber of Commerce. |
| `registration_number` | `str` | Optional | The registration number. |
| `tax_information` | [`List[TaxInformation]`](../../doc/models/tax-information.md) | Optional | The tax information of the entity. |
| `mtype` | [`Type171Enum`](../../doc/models/type-171-enum.md) | Required | Type of trust.<br><br>See possible values for trusts in [Australia](https://docs.adyen.com/platforms/verification-requirements/?tab=trust_3_4#trust-types-in-australia) and [New Zealand](https://docs.adyen.com/platforms/verification-requirements/?tab=trust_3_4#trust-types-in-new-zealand). |
| `undefined_beneficiary_info` | [`List[UndefinedBeneficiary]`](../../doc/models/undefined-beneficiary.md) | Optional | The undefined beneficiary information of the entity. |
| `vat_absence_reason` | [`VatAbsenceReason1Enum`](../../doc/models/vat-absence-reason-1-enum.md) | Optional | The reason for not providing a VAT number.<br><br>Possible values: **industryExemption**, **belowTaxThreshold**. |
| `vat_number` | `str` | Optional | The VAT number. |

## Example

```python
from adyen.models.address_41 import Address41
from adyen.models.address_51 import Address51
from adyen.models.trust import Trust
from adyen.models.type_171_enum import Type171Enum

trust = Trust(
    country_of_governing_law='countryOfGoverningLaw0',
    name='name4',
    registered_address=Address51(
        country='country4',
        city='city0',
        postal_code='postalCode8',
        state_or_province='stateOrProvince8',
        street='street0',
        street_2='street24'
    ),
    mtype=Type171Enum.FIXEDTRUST,
    date_of_incorporation='dateOfIncorporation6',
    description='description6',
    doing_business_as='doingBusinessAs2',
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

