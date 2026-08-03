
# Ultimate Party Identification 1

The ultimate sender of the funds of the transfer (ultimate debtor).

*This model accepts additional fields of type Any.*

## Structure

`UltimatePartyIdentification1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address8`](../../doc/models/address-8.md) | Optional | - |
| `date_of_birth` | `date` | Optional | The date of birth of the individual in [ISO-8601](https://www.w3.org/TR/NOTE-datetime) format. For example, **YYYY-MM-DD**.<br><br>Allowed only when `type` is **individual**. |
| `email` | `str` | Optional | The email address of the organization or individual. Maximum length: 254 characters.<br><br>**Constraints**: *Maximum Length*: `254` |
| `first_name` | `str` | Optional | The first name of the individual.<br><br>Supported characters: [a-z] [A-Z] - . / — and space.<br><br>This parameter is:<br><br>- Allowed only when `type` is **individual**.<br>- Required when `category` is **card**. |
| `full_name` | `str` | Optional | The full name of the entity that owns the bank account or card.<br><br>Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space.<br><br>Required when `category` is **bank**. |
| `funding_instrument` | [`FundingInstrument`](../../doc/models/funding-instrument.md) | Optional | - |
| `last_name` | `str` | Optional | The last name of the individual.<br><br>Supported characters: [a-z] [A-Z] - . / — and space.<br><br>This parameter is:<br><br>- Allowed only when `type` is **individual**.<br>- Required when `category` is **card**. |
| `reference` | `str` | Optional | A unique reference to identify the party or counterparty involved in the transfer. For example, your client's unique wallet or payee ID.<br><br>Required when you include `cardIdentification.storedPaymentMethodId`.<br><br>**Constraints**: *Maximum Length*: `150` |
| `mtype` | [`Type110`](../../doc/models/type-110.md) | Optional | - |
| `url` | `str` | Optional | The URL of the organization or individual. Maximum length: 255 characters.<br><br>**Constraints**: *Maximum Length*: `255` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.address_8 import Address8
from adyen.models.ultimate_party_identification_1 import UltimatePartyIdentification1

ultimate_party_identification_1 = UltimatePartyIdentification1(
    address=Address8(
        country='country0',
        city='city6',
        line_1='line18',
        line_2='line20',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    date_of_birth=dateutil.parser.parse('2016-03-13').date(),
    email='email0',
    first_name='firstName8',
    full_name='fullName6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

