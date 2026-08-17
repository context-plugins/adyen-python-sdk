
# Password Change Indicator Enum

Indicator when the shopper has changed their password.
Allowed values:

* notApplicable
* thisTransaction
* lessThan30Days
* from30To60Days
* moreThan60Days

## Enumeration

`PasswordChangeIndicatorEnum`

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
from adyen.models.password_change_indicator_enum import PasswordChangeIndicatorEnum

password_change_indicator = PasswordChangeIndicatorEnum.LESSTHAN30DAYS
```

