
# Counterparty Bank Restriction

*This model accepts additional fields of type Any.*

## Structure

`CounterpartyBankRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[BankIdentification]`](../../doc/models/bank-identification.md) | Optional | The list of counterparty bank institutions to be evaluated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_identification import BankIdentification
from adyen.models.counterparty_bank_restriction import CounterpartyBankRestriction
from adyen.models.identification_type import IdentificationType

counterparty_bank_restriction = CounterpartyBankRestriction(
    operation='operation0',
    value=[
        BankIdentification(
            country='country6',
            identification='identification0',
            identification_type=IdentificationType.BIC,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        BankIdentification(
            country='country6',
            identification='identification0',
            identification_type=IdentificationType.BIC,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        BankIdentification(
            country='country6',
            identification='identification0',
            identification_type=IdentificationType.BIC,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

