
# Payment Account Indicator Enum

Indicator for the length of time since this payment method was added to this shopper's account.
Allowed values:

* notApplicable
* thisTransaction
* lessThan30Days
* from30To60Days
* moreThan60Days

## Enumeration

`PaymentAccountIndicatorEnum`

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
from adyen.models.payment_account_indicator_enum import PaymentAccountIndicatorEnum

payment_account_indicator = PaymentAccountIndicatorEnum.MORETHAN60DAYS
```

