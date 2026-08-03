
# Bank Account V31

Contains information about the counterparty bank account.

*This model accepts additional fields of type Any.*

## Structure

`BankAccountV31`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`PartyIdentification`](../../doc/models/party-identification.md) | Required | - |
| `account_identification` | [AULocalAccountIdentification](../../doc/models/au-local-account-identification.md) \| [BRLocalAccountIdentification](../../doc/models/br-local-account-identification.md) \| [CALocalAccountIdentification](../../doc/models/ca-local-account-identification.md) \| [CZLocalAccountIdentification](../../doc/models/cz-local-account-identification.md) \| [DKLocalAccountIdentification](../../doc/models/dk-local-account-identification.md) \| [HKLocalAccountIdentification](../../doc/models/hk-local-account-identification.md) \| [HULocalAccountIdentification](../../doc/models/hu-local-account-identification.md) \| [IbanAccountIdentification1](../../doc/models/iban-account-identification-1.md) \| [NOLocalAccountIdentification](../../doc/models/no-local-account-identification.md) \| [NZLocalAccountIdentification](../../doc/models/nz-local-account-identification.md) \| [NumberAndBicAccountIdentification](../../doc/models/number-and-bic-account-identification.md) \| [PLLocalAccountIdentification](../../doc/models/pl-local-account-identification.md) \| [SELocalAccountIdentification](../../doc/models/se-local-account-identification.md) \| [SGLocalAccountIdentification](../../doc/models/sg-local-account-identification.md) \| [UKLocalAccountIdentification](../../doc/models/uk-local-account-identification.md) \| [USLocalAccountIdentification](../../doc/models/us-local-account-identification.md) | Required | This is a container for one-of cases. |
| `stored_payment_method_id` | `str` | Optional | The unique token that identifies the stored bank account details of the counterparty for a payout. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.address_8 import Address8
from adyen.models.au_local_account_identification import AuLocalAccountIdentification
from adyen.models.bank_account_v_31 import BankAccountV31
from adyen.models.party_identification import PartyIdentification
from adyen.models.type_413 import Type413

bank_account_v_31 = BankAccountV31(
    account_holder=PartyIdentification(
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
        email='email6',
        first_name='firstName4',
        full_name='fullName0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    account_identification=AuLocalAccountIdentification(
        account_number='accountNumber4',
        bsb_code='bsbCode8',
        mtype=Type413.AULOCAL,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    stored_payment_method_id='storedPaymentMethodId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

