
# Counterparty Types Restriction 1

Contains a list of counterparty types and how they must be evaluated.

Supported operations: **anyMatch**, **noneMatch**.

Supported value inputs:

- **balanceAccount**
- **bankAccount**
- **card**
- **transferInstrument**

## Structure

`CounterpartyTypesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[ValueEnum]`](../../doc/models/value-enum.md) | Optional | The list of counterparty types to be evaluated. |

## Example

```python
from adyen.models.counterparty_types_restriction_1 import CounterpartyTypesRestriction1
from adyen.models.value_enum import ValueEnum

counterparty_types_restriction_1 = CounterpartyTypesRestriction1(
    operation='operation8',
    value=[
        ValueEnum.BALANCEACCOUNT,
        ValueEnum.BANKACCOUNT
    ]
)
```

