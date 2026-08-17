
# Counterparty Types Restriction

## Structure

`CounterpartyTypesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[ValueEnum]`](../../doc/models/value-enum.md) | Optional | The list of counterparty types to be evaluated. |

## Example

```python
from adyen.models.counterparty_types_restriction import CounterpartyTypesRestriction
from adyen.models.value_enum import ValueEnum

counterparty_types_restriction = CounterpartyTypesRestriction(
    operation='operation8',
    value=[
        ValueEnum.BALANCEACCOUNT
    ]
)
```

