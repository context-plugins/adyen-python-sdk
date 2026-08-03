
# Account Verification Report Response

*This model accepts additional fields of type Any.*

## Structure

`AccountVerificationReportResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | [`List[VerifiedAccount]`](../../doc/models/verified-account.md) | Required | A list of bank accounts with their respective information. |
| `country` | [`AccountVerificationCountry1`](../../doc/models/account-verification-country-1.md) | Required | - |
| `id` | `str` | Required | The unique identifier for the specific report. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_identifiers import AccountIdentifiers
from adyen.models.account_party import AccountParty
from adyen.models.account_type_12 import AccountType12
from adyen.models.account_verification_country_1 import AccountVerificationCountry1
from adyen.models.account_verification_report_response import AccountVerificationReportResponse
from adyen.models.ach_account_identifier import AchAccountIdentifier
from adyen.models.bacs_account_identifier import BacsAccountIdentifier
from adyen.models.bsb_account_identifier import BsbAccountIdentifier
from adyen.models.eft_account_identifier import EftAccountIdentifier
from adyen.models.iban_account_identifier import IbanAccountIdentifier
from adyen.models.identity import Identity
from adyen.models.party_role_2 import PartyRole2
from adyen.models.verified_account import VerifiedAccount

account_verification_report_response = AccountVerificationReportResponse(
    accounts=[
        VerifiedAccount(
            account_id='accountId0',
            account_name='accountName4',
            account_number='accountNumber8',
            account_type=AccountType12.CURRENT,
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
    ],
    country=AccountVerificationCountry1.FR,
    id='id6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

