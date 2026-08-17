
# Condition Type Enum

Define when you want to get notified about a balance change. Possible values:

* **greaterThan**: the balance in the account(s) exceeds the specified `value`.

* **greaterThanOrEqual**: the balance in the account(s) reaches or exceeds the specified `value`.

* **lessThan**: the balance in the account(s) drops below the specified `value`.

* **lessThanOrEqual**: the balance in the account(s) reaches to drops below the specified `value`.

## Enumeration

`ConditionTypeEnum`

## Fields

| Name |
|  --- |
| `GREATERTHAN` |
| `GREATERTHANOREQUAL` |
| `LESSTHAN` |
| `LESSTHANOREQUAL` |

## Example

```python
from adyen.models.condition_type_enum import ConditionTypeEnum

condition_type = ConditionTypeEnum.GREATERTHAN
```

