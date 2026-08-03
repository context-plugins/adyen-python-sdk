
# Password Change Indicator

Indicator when the shopper has changed their password.
Allowed values:

* notApplicable
* thisTransaction
* lessThan30Days
* from30To60Days
* moreThan60Days

## Enumeration

`PasswordChangeIndicator`

## Fields

| Name |
|  --- |
| `NOTAPPLICABLE` |
| `THISTRANSACTION` |
| `LESSTHAN30DAYS` |
| `FROM30TO60DAYS` |
| `MORETHAN60DAYS` |

## Example

```python
from adyen.models.password_change_indicator import PasswordChangeIndicator

password_change_indicator = PasswordChangeIndicator.LESSTHAN30DAYS
```

