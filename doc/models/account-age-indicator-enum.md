
# Account Age Indicator Enum

Indicator for the length of time since this shopper account was created in the merchant's environment.
Allowed values:

* notApplicable
* thisTransaction
* lessThan30Days
* from30To60Days
* moreThan60Days, Indicator when the shopper has changed their password.
  Allowed values:
* notApplicable
* thisTransaction
* lessThan30Days
* from30To60Days
* moreThan60Days, Indicator for the length of time since this payment method was added to this shopper's account.
  Allowed values:
* notApplicable
* thisTransaction
* lessThan30Days
* from30To60Days
* moreThan60Days

## Enumeration

`AccountAgeIndicatorEnum`

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
from adyen.models.account_age_indicator_enum import AccountAgeIndicatorEnum

account_age_indicator = AccountAgeIndicatorEnum.NOTAPPLICABLE
```

