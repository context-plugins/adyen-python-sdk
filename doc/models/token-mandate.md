
# Token Mandate

*This model accepts additional fields of type Any.*

## Structure

`TokenMandate`

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
from adyen.models.token_mandate import TokenMandate

token_mandate = TokenMandate(
    amount='amount6',
    currency='currency4',
    ends_at='endsAt4',
    frequency=Frequency1.MONTHLY,
    mandate_id='mandateId4',
    provider_id='providerId8',
    status='status4',
    tx_variant='txVariant2',
    account_id_type='accountIdType6',
    amount_rule=AmountRule.MAX,
    billing_attempts_rule=BillingAttemptsRule.AFTER,
    billing_day='billingDay6',
    count='count0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

