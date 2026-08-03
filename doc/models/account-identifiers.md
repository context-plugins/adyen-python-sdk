
# Account Identifiers

*This model accepts additional fields of type Any.*

## Structure

`AccountIdentifiers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ach` | [`AchAccountIdentifier`](../../doc/models/ach-account-identifier.md) | Optional | - |
| `bacs` | [`BacsAccountIdentifier`](../../doc/models/bacs-account-identifier.md) | Optional | - |
| `bsb` | [`BsbAccountIdentifier`](../../doc/models/bsb-account-identifier.md) | Optional | - |
| `eft` | [`EftAccountIdentifier`](../../doc/models/eft-account-identifier.md) | Optional | - |
| `iban` | [`IbanAccountIdentifier`](../../doc/models/iban-account-identifier.md) | Optional | - |
| `rix` | [`RixAccountIdentifier`](../../doc/models/rix-account-identifier.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_identifiers import AccountIdentifiers
from adyen.models.ach_account_identifier import AchAccountIdentifier
from adyen.models.bacs_account_identifier import BacsAccountIdentifier
from adyen.models.bsb_account_identifier import BsbAccountIdentifier
from adyen.models.eft_account_identifier import EftAccountIdentifier
from adyen.models.iban_account_identifier import IbanAccountIdentifier

account_identifiers = AccountIdentifiers(
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
)
```

