
# Account Change Indicator

Indicator for the length of time since the shopper's account was last updated.
Allowed values:

* thisTransaction
* lessThan30Days
* from30To60Days
* moreThan60Days

## Enumeration

`AccountChangeIndicator`

## Fields

| Name |
|  --- |
| `THISTRANSACTION` |
| `LESSTHAN30DAYS` |
| `FROM30TO60DAYS` |
| `MORETHAN60DAYS` |

## Example

```python
from adyen.models.account_change_indicator import AccountChangeIndicator

account_change_indicator = AccountChangeIndicator.THISTRANSACTION
```

