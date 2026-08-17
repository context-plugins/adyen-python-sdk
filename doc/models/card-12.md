
# Card 12

Contains information about the counterparty card.

## Structure

`Card12`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_holder` | [`PartyIdentification1`](../../doc/models/party-identification-1.md) | Required | Contains information about the cardholder. |
| `card_identification` | [`CardIdentification3`](../../doc/models/card-identification-3.md) | Required | Contains the identification details of the card. |

## Example

```python
import dateutil.parser

from adyen.models.address_12 import Address12
from adyen.models.card_12 import Card12
from adyen.models.card_identification_3 import CardIdentification3
from adyen.models.party_identification_1 import PartyIdentification1
from adyen.models.type_112_enum import Type112Enum

card_12 = Card12(
    card_holder=PartyIdentification1(
        address=Address12(
            country='country0',
            city='city6',
            line_1='line18',
            line_2='line20',
            postal_code='postalCode8',
            state_or_province='stateOrProvince4'
        ),
        date_of_birth=dateutil.parser.parse('2016-03-13').date(),
        email='email0',
        first_name='firstName8',
        full_name='fullName6',
        mtype=Type112Enum.UNKNOWN
    ),
    card_identification=CardIdentification3(
        expiry_month='expiryMonth2',
        expiry_year='expiryYear2',
        issue_number='issueNumber0',
        number='number6',
        start_month='startMonth8'
    )
)
```

