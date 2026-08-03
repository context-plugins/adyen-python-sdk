
# Individual

*This model accepts additional fields of type Any.*

## Structure

`Individual`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `birth_data` | [`BirthData`](../../doc/models/birth-data.md) | Optional | - |
| `email` | `str` | Optional | The email address of the legal entity. |
| `identification_data` | [`IdentificationData`](../../doc/models/identification-data.md) | Optional | - |
| `name` | [`Name1`](../../doc/models/name-1.md) | Required | - |
| `nationality` | `str` | Optional | The individual's nationality. |
| `phone` | [`PhoneNumber`](../../doc/models/phone-number.md) | Optional | - |
| `residential_address` | [`Address1`](../../doc/models/address-1.md) | Required | - |
| `support` | [`Support`](../../doc/models/support.md) | Optional | - |
| `tax_information` | [`List[TaxInformation]`](../../doc/models/tax-information.md) | Optional | The tax information of the individual. |
| `web_data` | [`WebData`](../../doc/models/web-data.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_1 import Address1
from adyen.models.birth_data import BirthData
from adyen.models.identification_data import IdentificationData
from adyen.models.individual import Individual
from adyen.models.name_1 import Name1
from adyen.models.phone_number import PhoneNumber
from adyen.models.type_132 import Type132

individual = Individual(
    name=Name1(
        first_name='firstName4',
        last_name='lastName4',
        infix='infix4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    residential_address=Address1(
        country='country6',
        city='city2',
        postal_code='postalCode4',
        state_or_province='stateOrProvince0',
        street='street2',
        street_2='street28',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    birth_data=BirthData(
        date_of_birth='dateOfBirth8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    email='email0',
    identification_data=IdentificationData(
        mtype=Type132.NATIONALIDNUMBER,
        card_number='cardNumber6',
        expiry_date='expiryDate8',
        issuer_country='issuerCountry6',
        issuer_state='issuerState6',
        national_id_exempt=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    nationality='nationality4',
    phone=PhoneNumber(
        number='number8',
        phone_country_code='phoneCountryCode8',
        mtype='type0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

