
# Party Identification

## Structure

`PartyIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address12`](../../doc/models/address-12.md) | Optional | The address of the bank account or card owner. |
| `date_of_birth` | `date` | Optional | The date of birth of the individual in [ISO-8601](https://www.w3.org/TR/NOTE-datetime) format. For example, **YYYY-MM-DD**.<br><br>Allowed only when `type` is **individual**. |
| `email` | `str` | Optional | The email address of the organization or individual. Maximum length: 254 characters.<br><br>**Constraints**: *Maximum Length*: `254` |
| `first_name` | `str` | Optional | The first name of the individual.<br><br>Supported characters: [a-z] [A-Z] - . / — and space.<br><br>This parameter is:<br><br>- Allowed only when `type` is **individual**.<br>- Required when `category` is **card**. |
| `full_name` | `str` | Optional | The full name of the entity that owns the bank account or card.<br><br>Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space.<br><br>Required when `category` is **bank**. |
| `last_name` | `str` | Optional | The last name of the individual.<br><br>Supported characters: [a-z] [A-Z] - . / — and space.<br><br>This parameter is:<br><br>- Allowed only when `type` is **individual**.<br>- Required when `category` is **card**. |
| `reference` | `str` | Optional | A unique reference to identify the party or counterparty involved in the transfer. For example, your client's unique wallet or payee ID.<br><br>Required when you include `cardIdentification.storedPaymentMethodId`.<br><br>**Constraints**: *Maximum Length*: `150` |
| `mtype` | [`Type112Enum`](../../doc/models/type-112-enum.md) | Optional | The type of entity that owns the bank account or card.<br><br>Possible values: **individual**, **organization**, or **unknown**.<br><br>Required when `category` is **card**. In this case, the value must be **individual**.<br><br>**Default**: `"unknown"` |
| `url` | `str` | Optional | The URL of the organization or individual. Maximum length: 255 characters.<br><br>**Constraints**: *Maximum Length*: `255` |

## Example

```python
import dateutil.parser

from adyen.models.address_12 import Address12
from adyen.models.party_identification import PartyIdentification
from adyen.models.type_112_enum import Type112Enum

party_identification = PartyIdentification(
    address=Address12(
        country='country0',
        city='city6',
        line_1='line18',
        line_2='line20',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4'
    ),
    date_of_birth=dateutil.parser.parse('2016-03-13').date(),
    email='email2',
    first_name='firstName0',
    full_name='fullName4',
    mtype=Type112Enum.UNKNOWN
)
```

