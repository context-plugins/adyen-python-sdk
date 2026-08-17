
# Account Verification Report Response

## Structure

`AccountVerificationReportResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | [`List[VerifiedAccount]`](../../doc/models/verified-account.md) | Required | A list of bank accounts with their respective information. |
| `country` | [`AccountVerificationCountry1Enum`](../../doc/models/account-verification-country-1-enum.md) | Required | The location where the third-party individual's bank account is registered. |
| `id` | `str` | Required | The unique identifier for the specific report. |

## Example

```python
from adyen.models.account_identifiers_1 import AccountIdentifiers1
from adyen.models.account_party import AccountParty
from adyen.models.account_type_11_enum import AccountType11Enum
from adyen.models.account_verification_country_1_enum import AccountVerificationCountry1Enum
from adyen.models.account_verification_report_response import AccountVerificationReportResponse
from adyen.models.ach_account_identifier_1 import ACHAccountIdentifier1
from adyen.models.bacs_account_identifier_2 import BACSAccountIdentifier2
from adyen.models.bsb_account_identifier_2 import BSBAccountIdentifier2
from adyen.models.eft_account_identifier_2 import EFTAccountIdentifier2
from adyen.models.iban_account_identifier_2 import IBANAccountIdentifier2
from adyen.models.identity_2 import Identity2
from adyen.models.party_role_2_enum import PartyRole2Enum
from adyen.models.verified_account import VerifiedAccount

account_verification_report_response = AccountVerificationReportResponse(
    accounts=[
        VerifiedAccount(
            account_id='accountId0',
            account_name='accountName4',
            account_number='accountNumber8',
            account_type=AccountType11Enum.CURRENT,
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
    ],
    country=AccountVerificationCountry1Enum.FR,
    id='id6'
)
```

