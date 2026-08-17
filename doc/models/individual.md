
# Individual

## Structure

`Individual`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `birth_data` | [`BirthData1`](../../doc/models/birth-data-1.md) | Optional | The individual's birth information. |
| `email` | `str` | Optional | The email address of the legal entity. |
| `identification_data` | [`IdentificationData1`](../../doc/models/identification-data-1.md) | Optional | Information about the individual's identification document. |
| `name` | [`Name23`](../../doc/models/name-23.md) | Required | The individual's name. |
| `nationality` | `str` | Optional | The individual's nationality. |
| `phone` | [`PhoneNumber2`](../../doc/models/phone-number-2.md) | Optional | The phone number of the legal entity. |
| `residential_address` | [`Address13`](../../doc/models/address-13.md) | Required | The residential address of the individual. |
| `support` | [`Support1`](../../doc/models/support-1.md) | Optional | Support information for the legal entity. Required if you have a platform setup. |
| `tax_information` | [`List[TaxInformation]`](../../doc/models/tax-information.md) | Optional | The tax information of the individual. |
| `web_data` | [`WebData1`](../../doc/models/web-data-1.md) | Optional | The website and app URL of the legal entity. |

## Example

```python
from adyen.models.address_13 import Address13
from adyen.models.birth_data_1 import BirthData1
from adyen.models.identification_data_1 import IdentificationData1
from adyen.models.individual import Individual
from adyen.models.name_23 import Name23
from adyen.models.phone_number_2 import PhoneNumber2
from adyen.models.type_132_enum import Type132Enum

individual = Individual(
    name=Name23(
        first_name='firstName4',
        last_name='lastName4',
        infix='infix4'
    ),
    residential_address=Address13(
        country='country6',
        city='city2',
        postal_code='postalCode4',
        state_or_province='stateOrProvince0',
        street='street2',
        street_2='street28'
    ),
    birth_data=BirthData1(
        date_of_birth='dateOfBirth8'
    ),
    email='email0',
    identification_data=IdentificationData1(
        mtype=Type132Enum.NATIONALIDNUMBER,
        card_number='cardNumber6',
        expiry_date='expiryDate8',
        issuer_country='issuerCountry6',
        issuer_state='issuerState6',
        national_id_exempt=False
    ),
    nationality='nationality4',
    phone=PhoneNumber2(
        number='number8',
        mtype='type0'
    )
)
```

