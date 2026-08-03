
# Token Mandate 2

Mandate details for the stored payment method.

*This model accepts additional fields of type Any.*

## Structure

`TokenMandate2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id_type` | `str` | Optional | The type of account identifier for the masked account number. |
| `amount` | `str` | Required | The billing amount (in minor units) of the recurring transactions. |
| `amount_rule` | [`AmountRule`](../../doc/models/amount-rule.md) | Optional | - |
| `billing_attempts_rule` | [`BillingAttemptsRule`](../../doc/models/billing-attempts-rule.md) | Optional | - |
| `billing_day` | `str` | Optional | The number of the day, on which the recurring debit can happen. Should be within the same calendar month as the mandate recurring date.<br><br>Possible values: 1-31 based on the `frequency`. |
| `count` | `str` | Optional | The number of transactions that can be performed within the given frequency. |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `ends_at` | `str` | Required | End date of the billing plan, in YYYY-MM-DD format. |
| `frequency` | [`Frequency1`](../../doc/models/frequency-1.md) | Required | - |
| `mandate_id` | `str` | Required | The unique identifier of the mandate. |
| `masked_account_id` | `str` | Optional | The masked account number associated with the mandate. |
| `min_amount` | `str` | Optional | For a billing plan where the payment amounts are variable, the minimum amount to charge the shopper for each recurring payment. When a shopper approves the billing plan, they can also specify a maximum amount in their banking app. |
| `provider_id` | `str` | Required | The provider-specific identifier for this mandate. |
| `recurring_amount` | `str` | Optional | For a billing plan where the payment amount is fixed, the amount the shopper will be charged for each recurring payment. |
| `recurring_statement` | `str` | Optional | The text that will be shown on the shopper's bank statement for the recurring payments. We recommend to add a descriptive text about the subscription to let your shoppers recognize your recurring payments.<br>Maximum length: 35 characters.<br><br>**Constraints**: *Maximum Length*: `35` |
| `remarks` | `str` | Optional | Additional remarks or notes about the mandate. |
| `retry_policy` | [`RetryPolicy`](../../doc/models/retry-policy.md) | Optional | - |
| `starts_at` | `str` | Optional | Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date. |
| `status` | `str` | Required | The status of the mandate. Examples : active, revoked, completed, expired |
| `tx_variant` | `str` | Required | The transaction variant used for this mandate. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_rule import AmountRule
from adyen.models.billing_attempts_rule import BillingAttemptsRule
from adyen.models.frequency_1 import Frequency1
from adyen.models.token_mandate_2 import TokenMandate2

token_mandate_2 = TokenMandate2(
    amount='amount2',
    currency='currency0',
    ends_at='endsAt0',
    frequency=Frequency1.WEEKLY,
    mandate_id='mandateId8',
    provider_id='providerId4',
    status='status2',
    tx_variant='txVariant8',
    account_id_type='accountIdType0',
    amount_rule=AmountRule.MAX,
    billing_attempts_rule=BillingAttemptsRule.AFTER,
    billing_day='billingDay2',
    count='count4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

