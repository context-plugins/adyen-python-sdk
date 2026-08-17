
# Verified Account

## Structure

`VerifiedAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Required | The unique identifier for the bank account. |
| `account_name` | `str` | Required | The name of the bank account. This name is assigned by the banking institution, and it describes the type of bank account. |
| `account_number` | `str` | Required | The account number of the bank account. |
| `account_type` | [`AccountType11Enum`](../../doc/models/account-type-11-enum.md) | Required | The type of the bank account. Possible values are **CURRENT**, **SAVINGS**, **BUSINESS**, **CREDIT_CARD**, **LOAN**, **UNKNOWN**. |
| `bank_name` | `str` | Optional | The name of the banking institution where the bank account is held. |
| `currency` | `str` | Required | The currency of the funds in the bank account. |
| `identifiers` | [`AccountIdentifiers1`](../../doc/models/account-identifiers-1.md) | Required | Contains various codes and details used to uniquely identify the bank account across different regions. |
| `parties` | [`List[AccountParty]`](../../doc/models/account-party.md) | Required | Contains details of all parties associated with the report. |

## Example

```python
from adyen.models.account_identifiers_1 import AccountIdentifiers1
from adyen.models.account_party import AccountParty
from adyen.models.account_type_11_enum import AccountType11Enum
from adyen.models.ach_account_identifier_1 import ACHAccountIdentifier1
from adyen.models.bacs_account_identifier_2 import BACSAccountIdentifier2
from adyen.models.bsb_account_identifier_2 import BSBAccountIdentifier2
from adyen.models.eft_account_identifier_2 import EFTAccountIdentifier2
from adyen.models.iban_account_identifier_2 import IBANAccountIdentifier2
from adyen.models.identity_2 import Identity2
from adyen.models.party_role_2_enum import PartyRole2Enum
from adyen.models.verified_account import VerifiedAccount

verified_account = VerifiedAccount(
    account_id='accountId0',
    account_name='accountName4',
    account_number='accountNumber8',
    account_type=AccountType11Enum.BUSINESS,
    currency='currency0',
    identifiers=AccountIdentifiers1(
        ach=ACHAccountIdentifier1(
            account_number='accountNumber4',
            routing_number='routingNumber8',
            account_last_digits='accountLastDigits2',
            is_tokenized=False
        ),
        bacs=BACSAccountIdentifier2(
            account_number='accountNumber2',
            sort_code='sortCode8'
        ),
        bsb=BSBAccountIdentifier2(
            account_number='accountNumber2',
            bsb_code='bsbCode0'
        ),
        eft=EFTAccountIdentifier2(
            account_number='accountNumber0',
            branch='branch8',
            institution='institution2'
        ),
        iban=IBANAccountIdentifier2(
            bban='bban8',
            bic='bic6',
            iban='iban8'
        )
    ),
    parties=[
        AccountParty(
            identity=Identity2(
                full_legal_name='fullLegalName2',
                name='name4'
            ),
            role=PartyRole2Enum.HOLDER
        )
    ],
    bank_name='bankName6'
)
```

