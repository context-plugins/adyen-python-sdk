
# Amount Rule

The limitation rule of the billing amount.

Possible values:

* **max**: The transaction amount can not exceed the `amount`.

* **exact**: The transaction amount should be the same as the `amount`.

## Enumeration

`AmountRule`

## Fields

| Name |
|  --- |
| `MAX` |
| `EXACT` |

## Example

```python
from adyen.models.amount_rule import AmountRule

amount_rule = AmountRule.MAX
```

