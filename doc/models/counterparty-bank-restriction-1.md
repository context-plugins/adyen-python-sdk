
# Counterparty Bank Restriction 1

Contains a list of counterparty financial institutions and how they must be evaluated.

Supported operations: **anyMatch**, **noneMatch**.

## Structure

`CounterpartyBankRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[BankIdentification]`](../../doc/models/bank-identification.md) | Optional | The list of counterparty bank institutions to be evaluated. |

## Example

```python
from adyen.models.bank_identification import BankIdentification
from adyen.models.counterparty_bank_restriction_1 import CounterpartyBankRestriction1
from adyen.models.identification_type_enum import IdentificationTypeEnum

counterparty_bank_restriction_1 = CounterpartyBankRestriction1(
    operation='operation6',
    value=[
        BankIdentification(
            country='country6',
            identification='identification0',
            identification_type=IdentificationTypeEnum.BIC
        )
    ]
)
```

