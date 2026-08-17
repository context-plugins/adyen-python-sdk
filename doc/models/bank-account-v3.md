
# Bank Account V3

## Structure

`BankAccountV3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`PartyIdentification3`](../../doc/models/party-identification-3.md) | Required | Information about the owner of the bank account. |
| `account_identification` | [AULocalAccountIdentification](../../doc/models/au-local-account-identification.md) \| [BRLocalAccountIdentification](../../doc/models/br-local-account-identification.md) \| [CALocalAccountIdentification](../../doc/models/ca-local-account-identification.md) \| [CZLocalAccountIdentification](../../doc/models/cz-local-account-identification.md) \| [DKLocalAccountIdentification](../../doc/models/dk-local-account-identification.md) \| [HKLocalAccountIdentification](../../doc/models/hk-local-account-identification.md) \| [HULocalAccountIdentification](../../doc/models/hu-local-account-identification.md) \| [IbanAccountIdentification](../../doc/models/iban-account-identification.md) \| [NOLocalAccountIdentification](../../doc/models/no-local-account-identification.md) \| [NZLocalAccountIdentification](../../doc/models/nz-local-account-identification.md) \| [NumberAndBicAccountIdentification](../../doc/models/number-and-bic-account-identification.md) \| [PLLocalAccountIdentification](../../doc/models/pl-local-account-identification.md) \| [SELocalAccountIdentification](../../doc/models/se-local-account-identification.md) \| [SGLocalAccountIdentification](../../doc/models/sg-local-account-identification.md) \| [UKLocalAccountIdentification](../../doc/models/uk-local-account-identification.md) \| [USLocalAccountIdentification](../../doc/models/us-local-account-identification.md) | Required | This is a container for one-of cases. |
| `stored_payment_method_id` | `str` | Optional | The unique token that identifies the stored bank account details of the counterparty for a payout. |

## Example

```python
import dateutil.parser

from adyen.models.address_12 import Address12
from adyen.models.au_local_account_identification import AULocalAccountIdentification
from adyen.models.bank_account_v_3 import BankAccountV3
from adyen.models.party_identification_3 import PartyIdentification3
from adyen.models.type_112_enum import Type112Enum

bank_account_v_3 = BankAccountV3(
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
        full_name='fullName0',
        mtype=Type112Enum.UNKNOWN
    ),
    account_identification=AULocalAccountIdentification(
        account_number='accountNumber4',
        bsb_code='bsbCode8'
    ),
    stored_payment_method_id='storedPaymentMethodId6'
)
```

