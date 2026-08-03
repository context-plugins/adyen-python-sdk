
# Card 11

Contains information about the counterparty card.

*This model accepts additional fields of type Any.*

## Structure

`Card11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_holder` | [`PartyIdentification`](../../doc/models/party-identification.md) | Required | - |
| `card_identification` | [`CardIdentification`](../../doc/models/card-identification.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.address_8 import Address8
from adyen.models.card_11 import Card11
from adyen.models.card_identification import CardIdentification
from adyen.models.party_identification import PartyIdentification

card_11 = Card11(
    card_holder=PartyIdentification(
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
    ),
    card_identification=CardIdentification(
        expiry_month='expiryMonth2',
        expiry_year='expiryYear2',
        issue_number='issueNumber0',
        number='number6',
        start_month='startMonth8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

