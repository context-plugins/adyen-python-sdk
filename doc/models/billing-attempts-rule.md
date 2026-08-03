
# Billing Attempts Rule

The rule to specify the period, within which the recurring debit can happen, relative to the mandate recurring date.

Possible values:

* **on**: On a specific date.

* **before**:  Before and on a specific date.

* **after**: On and after a specific date.

## Enumeration

`BillingAttemptsRule`

## Fields

| Name |
|  --- |
| `ON` |
| `BEFORE` |
| `AFTER` |

## Example

```python
from adyen.models.billing_attempts_rule import BillingAttemptsRule

billing_attempts_rule = BillingAttemptsRule.AFTER
```

