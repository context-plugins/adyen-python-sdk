
# Counterparty Bank Restriction

## Structure

`CounterpartyBankRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[BankIdentification]`](../../doc/models/bank-identification.md) | Optional | The list of counterparty bank institutions to be evaluated. |

## Example

```python
from adyen.models.bank_identification import BankIdentification
from adyen.models.counterparty_bank_restriction import CounterpartyBankRestriction
from adyen.models.identification_type_enum import IdentificationTypeEnum

counterparty_bank_restriction = CounterpartyBankRestriction(
    operation='operation0',
    value=[
        BankIdentification(
            country='country6',
            identification='identification0',
            identification_type=IdentificationTypeEnum.BIC
        ),
        BankIdentification(
            country='country6',
            identification='identification0',
            identification_type=IdentificationTypeEnum.BIC
        ),
        BankIdentification(
            country='country6',
            identification='identification0',
            identification_type=IdentificationTypeEnum.BIC
        )
    ]
)
```

