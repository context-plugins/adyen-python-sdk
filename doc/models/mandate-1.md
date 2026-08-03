
# Mandate 1

*This model accepts additional fields of type Any.*

## Structure

`Mandate1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Required | The billing amount (in minor units) of the recurring transactions. |
| `amount_rule` | [`AmountRule`](../../doc/models/amount-rule.md) | Optional | - |
| `billing_attempts_rule` | [`BillingAttemptsRule`](../../doc/models/billing-attempts-rule.md) | Optional | - |
| `billing_day` | `str` | Optional | The number of the day, on which the recurring debit can happen. Should be within the same calendar month as the mandate recurring date.<br><br>Possible values: 1-31 based on the `frequency`. |
| `count` | `str` | Optional | The number of transactions that can be performed within the given frequency. |
| `ends_at` | `str` | Required | End date of the billing plan, in YYYY-MM-DD format. |
| `frequency` | [`Frequency1`](../../doc/models/frequency-1.md) | Required | - |
| `remarks` | `str` | Optional | The message shown by UPI to the shopper on the approval screen. |
| `starts_at` | `str` | Optional | Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_rule import AmountRule
from adyen.models.billing_attempts_rule import BillingAttemptsRule
from adyen.models.frequency_1 import Frequency1
from adyen.models.mandate_1 import Mandate1

mandate_1 = Mandate1(
    amount='amount6',
    ends_at='endsAt4',
    frequency=Frequency1.MONTHLY,
    amount_rule=AmountRule.MAX,
    billing_attempts_rule=BillingAttemptsRule.ON,
    billing_day='billingDay6',
    count='count0',
    remarks='remarks0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

