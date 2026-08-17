
# Counterparty Info V3

## Structure

`CounterpartyInfoV3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The unique identifier of the counterparty [balance account](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id). |
| `bank_account` | [`BankAccountV31`](../../doc/models/bank-account-v31.md) | Optional | Contains information about the counterparty bank account. |
| `card` | [`Card12`](../../doc/models/card-12.md) | Optional | Contains information about the counterparty card. |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the counterparty [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id). |

## Example

```python
import dateutil.parser

from adyen.models.address_12 import Address12
from adyen.models.au_local_account_identification import AULocalAccountIdentification
from adyen.models.bank_account_v_31 import BankAccountV31
from adyen.models.card_12 import Card12
from adyen.models.card_identification_3 import CardIdentification3
from adyen.models.counterparty_info_v_3 import CounterpartyInfoV3
from adyen.models.party_identification_1 import PartyIdentification1
from adyen.models.party_identification_3 import PartyIdentification3

counterparty_info_v_3 = CounterpartyInfoV3(
    balance_account_id='balanceAccountId0',
    bank_account=BankAccountV31(
        account_holder=PartyIdentification3(
            address=Address12(
                country='country0',
                city='city6',
                line_1='line18',
                line_2='line20',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4'
            ),
            date_of_birth=dateutil.parser.parse('2016-03-13').date(),
            email='email6',
            first_name='firstName4',
            full_name='fullName0'
        ),
        account_identification=AULocalAccountIdentification(
            account_number='accountNumber4',
            bsb_code='bsbCode8'
        ),
        stored_payment_method_id='storedPaymentMethodId2'
    ),
    card=Card12(
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
            full_name='fullName6'
        ),
        card_identification=CardIdentification3(
            expiry_month='expiryMonth2',
            expiry_year='expiryYear2',
            issue_number='issueNumber0',
            number='number6',
            start_month='startMonth8'
        )
    ),
    transfer_instrument_id='transferInstrumentId4'
)
```

