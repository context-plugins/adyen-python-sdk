
# Mandate

The mandate details to initiate recurring transaction.

## Structure

`Mandate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Required | The billing amount (in minor units) of the recurring transactions. |
| `amount_rule` | [`AmountRuleEnum`](../../doc/models/amount-rule-enum.md) | Optional | The limitation rule of the billing amount.<br><br>Possible values:<br><br>* **max**: The transaction amount can not exceed the `amount`.<br><br>* **exact**: The transaction amount should be the same as the `amount`. |
| `billing_attempts_rule` | [`BillingAttemptsRuleEnum`](../../doc/models/billing-attempts-rule-enum.md) | Optional | The rule to specify the period, within which the recurring debit can happen, relative to the mandate recurring date.<br><br>Possible values:<br><br>* **on**: On a specific date.<br><br>* **before**:  Before and on a specific date.<br><br>* **after**: On and after a specific date. |
| `billing_day` | `str` | Optional | The number of the day, on which the recurring debit can happen. Should be within the same calendar month as the mandate recurring date.<br><br>Possible values: 1-31 based on the `frequency`. |
| `count` | `str` | Optional | The number of transactions that can be performed within the given frequency. |
| `ends_at` | `str` | Required | End date of the billing plan, in YYYY-MM-DD format. |
| `frequency` | [`FrequencyEnum`](../../doc/models/frequency-enum.md) | Required | The frequency with which a shopper should be charged.<br><br>Possible values: **adhoc**, **daily**, **weekly**, **biWeekly**, **monthly**, **quarterly**, **halfYearly**, **yearly**. |
| `remarks` | `str` | Optional | The message shown by UPI to the shopper on the approval screen. |
| `starts_at` | `str` | Optional | Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date. |

## Example

```python
from adyen.models.amount_rule_enum import AmountRuleEnum
from adyen.models.billing_attempts_rule_enum import BillingAttemptsRuleEnum
from adyen.models.frequency_enum import FrequencyEnum
from adyen.models.mandate import Mandate

mandate = Mandate(
    amount='amount8',
    ends_at='endsAt6',
    frequency=FrequencyEnum.MONTHLY,
    amount_rule=AmountRuleEnum.MAX,
    billing_attempts_rule=BillingAttemptsRuleEnum.ON,
    billing_day='billingDay8',
    count='count8',
    remarks='remarks8'
)
```

