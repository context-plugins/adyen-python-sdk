
# Mandate Bank Account

*This model accepts additional fields of type Any.*

## Structure

`MandateBankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`MandatePartyIdentification`](../../doc/models/mandate-party-identification.md) | Required | - |
| `account_identification` | [`MandateAccountIdentification2`](../../doc/models/mandate-account-identification-2.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mandate_account_identification_2 import MandateAccountIdentification2
from adyen.models.mandate_bank_account import MandateBankAccount
from adyen.models.mandate_party_identification import MandatePartyIdentification

mandate_bank_account = MandateBankAccount(
    account_holder=MandatePartyIdentification(
        full_name='fullName0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    account_identification=MandateAccountIdentification2(
        mtype='MandateAccountIdentification2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

