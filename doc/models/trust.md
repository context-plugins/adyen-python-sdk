
# Trust

*This model accepts additional fields of type Any.*

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
| `principal_place_of_business` | [`Address1`](../../doc/models/address-1.md) | Optional | - |
| `registered_address` | [`Address1`](../../doc/models/address-1.md) | Required | - |
| `registration_number` | `str` | Optional | The registration number. |
| `tax_information` | [`List[TaxInformation]`](../../doc/models/tax-information.md) | Optional | The tax information of the entity. |
| `mtype` | [`Type171`](../../doc/models/type-171.md) | Required | - |
| `undefined_beneficiary_info` | [`List[UndefinedBeneficiary]`](../../doc/models/undefined-beneficiary.md) | Optional | The undefined beneficiary information of the entity. |
| `vat_absence_reason` | [`VatAbsenceReason1`](../../doc/models/vat-absence-reason-1.md) | Optional | - |
| `vat_number` | `str` | Optional | The VAT number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_1 import Address1
from adyen.models.trust import Trust
from adyen.models.type_171 import Type171

trust = Trust(
    country_of_governing_law='countryOfGoverningLaw0',
    name='name4',
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
    mtype=Type171.FIXEDTRUST,
    date_of_incorporation='dateOfIncorporation6',
    description='description6',
    doing_business_as='doingBusinessAs2',
    doing_business_as_absent=False,
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

