
# Account Identifiers

## Structure

`AccountIdentifiers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ach` | [`ACHAccountIdentifier1`](../../doc/models/ach-account-identifier-1.md) | Optional | Identifiers relevant for Automated Clearing House (ACH) payments, primarily used in the United States. |
| `bacs` | [`BACSAccountIdentifier2`](../../doc/models/bacs-account-identifier-2.md) | Optional | Identifiers relevant for Bankers' Automated Clearing Services (BACS) payments, primarily used in the United Kingdom. |
| `bsb` | [`BSBAccountIdentifier2`](../../doc/models/bsb-account-identifier-2.md) | Optional | Identifiers relevant for Australian banking, specifically for BSB (Bank-State-Branch) numbers. |
| `eft` | [`EFTAccountIdentifier2`](../../doc/models/eft-account-identifier-2.md) | Optional | Identifiers relevant for Electronic Funds Transfer (EFT) payments, commonly used in Canada. |
| `iban` | [`IBANAccountIdentifier2`](../../doc/models/iban-account-identifier-2.md) | Optional | The international bank account number as defined in the ISO-13616 standard. |
| `rix` | [`RIXAccountIdentifier2`](../../doc/models/rix-account-identifier-2.md) | Optional | Identifiers relevant for the Rix (Russian Interbank eXchange) system, used for interbank payments within Russia. |

## Example

```python
from adyen.models.account_identifiers import AccountIdentifiers
from adyen.models.ach_account_identifier_1 import ACHAccountIdentifier1
from adyen.models.bacs_account_identifier_2 import BACSAccountIdentifier2
from adyen.models.bsb_account_identifier_2 import BSBAccountIdentifier2
from adyen.models.eft_account_identifier_2 import EFTAccountIdentifier2
from adyen.models.iban_account_identifier_2 import IBANAccountIdentifier2

account_identifiers = AccountIdentifiers(
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
)
```

