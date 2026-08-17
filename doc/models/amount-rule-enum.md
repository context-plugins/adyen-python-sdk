
# Amount Rule Enum

The limitation rule of the billing amount.

Possible values:

* **max**: The transaction amount can not exceed the `amount`.

* **exact**: The transaction amount should be the same as the `amount`.

## Enumeration

`AmountRuleEnum`

## Fields

| Name |
|  --- |
| `MAX` |
| `EXACT` |

## Example

```python
from adyen.models.amount_rule_enum import AmountRuleEnum

amount_rule = AmountRuleEnum.MAX
```

