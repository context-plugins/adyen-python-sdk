
# Verified Account

*This model accepts additional fields of type Any.*

## Structure

`VerifiedAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Required | The unique identifier for the bank account. |
| `account_name` | `str` | Required | The name of the bank account. This name is assigned by the banking institution, and it describes the type of bank account. |
| `account_number` | `str` | Required | The account number of the bank account. |
| `account_type` | [`AccountType12`](../../doc/models/account-type-12.md) | Required | - |
| `bank_name` | `str` | Optional | The name of the banking institution where the bank account is held. |
| `currency` | `str` | Required | The currency of the funds in the bank account. |
| `identifiers` | [`AccountIdentifiers`](../../doc/models/account-identifiers.md) | Required | - |
| `parties` | [`List[AccountParty]`](../../doc/models/account-party.md) | Required | Contains details of all parties associated with the report. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_identifiers import AccountIdentifiers
from adyen.models.account_party import AccountParty
from adyen.models.account_type_12 import AccountType12
from adyen.models.ach_account_identifier import AchAccountIdentifier
from adyen.models.bacs_account_identifier import BacsAccountIdentifier
from adyen.models.bsb_account_identifier import BsbAccountIdentifier
from adyen.models.eft_account_identifier import EftAccountIdentifier
from adyen.models.iban_account_identifier import IbanAccountIdentifier
from adyen.models.identity import Identity
from adyen.models.party_role_2 import PartyRole2
from adyen.models.verified_account import VerifiedAccount

verified_account = VerifiedAccount(
    account_id='accountId0',
    account_name='accountName4',
    account_number='accountNumber8',
    account_type=AccountType12.BUSINESS,
    currency='currency0',
    identifiers=AccountIdentifiers(
        ach=AchAccountIdentifier(
            account_number='accountNumber4',
            routing_number='routingNumber8',
            account_last_digits='accountLastDigits2',
            is_tokenized=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        bacs=BacsAccountIdentifier(
            account_number='accountNumber2',
            sort_code='sortCode8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        bsb=BsbAccountIdentifier(
            account_number='accountNumber2',
            bsb_code='bsbCode0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        eft=EftAccountIdentifier(
            account_number='accountNumber0',
            branch='branch8',
            institution='institution2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        iban=IbanAccountIdentifier(
            bban='bban8',
            bic='bic6',
            iban='iban8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    parties=[
        AccountParty(
            identity=Identity(
                full_legal_name='fullLegalName2',
                name='name4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            role=PartyRole2.HOLDER,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    bank_name='bankName6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

