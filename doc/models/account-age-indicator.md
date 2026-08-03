
# Account Age Indicator

Indicator for the length of time since this shopper account was created in the merchant's environment.
Allowed values:

* notApplicable
* thisTransaction
* lessThan30Days
* from30To60Days
* moreThan60Days

## Enumeration

`AccountAgeIndicator`

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
from adyen.models.account_age_indicator import AccountAgeIndicator

account_age_indicator = AccountAgeIndicator.NOTAPPLICABLE
```

