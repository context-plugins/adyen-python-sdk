
# Token Mandate

## Structure

`TokenMandate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id_type` | `str` | Optional | The type of account identifier for the masked account number. |
| `amount` | `str` | Required | The billing amount (in minor units) of the recurring transactions. |
| `amount_rule` | [`AmountRuleEnum`](../../doc/models/amount-rule-enum.md) | Optional | The limitation rule of the billing amount.<br><br>Possible values:<br><br>* **max**: The transaction amount can not exceed the `amount`.<br><br>* **exact**: The transaction amount should be the same as the `amount`. |
| `billing_attempts_rule` | [`BillingAttemptsRuleEnum`](../../doc/models/billing-attempts-rule-enum.md) | Optional | The rule to specify the period, within which the recurring debit can happen, relative to the mandate recurring date.<br><br>Possible values:<br><br>* **on**: On a specific date.<br><br>* **before**:  Before and on a specific date.<br><br>* **after**: On and after a specific date. |
| `billing_day` | `str` | Optional | The number of the day, on which the recurring debit can happen. Should be within the same calendar month as the mandate recurring date.<br><br>Possible values: 1-31 based on the `frequency`. |
| `count` | `str` | Optional | The number of transactions that can be performed within the given frequency. |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `ends_at` | `str` | Required | End date of the billing plan, in YYYY-MM-DD format. |
| `frequency` | [`FrequencyEnum`](../../doc/models/frequency-enum.md) | Required | The frequency with which a shopper should be charged.<br><br>Possible values: **adhoc**, **daily**, **weekly**, **biWeekly**, **monthly**, **quarterly**, **halfYearly**, **yearly**. |
| `mandate_id` | `str` | Required | The unique identifier of the mandate. |
| `masked_account_id` | `str` | Optional | The masked account number associated with the mandate. |
| `min_amount` | `str` | Optional | For a billing plan where the payment amounts are variable, the minimum amount to charge the shopper for each recurring payment. When a shopper approves the billing plan, they can also specify a maximum amount in their banking app. |
| `provider_id` | `str` | Required | The provider-specific identifier for this mandate. |
| `recurring_amount` | `str` | Optional | For a billing plan where the payment amount is fixed, the amount the shopper will be charged for each recurring payment. |
| `recurring_statement` | `str` | Optional | The text that will be shown on the shopper's bank statement for the recurring payments. We recommend to add a descriptive text about the subscription to let your shoppers recognize your recurring payments.<br>Maximum length: 35 characters.<br><br>**Constraints**: *Maximum Length*: `35` |
| `remarks` | `str` | Optional | Additional remarks or notes about the mandate. |
| `retry_policy` | [`RetryPolicyEnum`](../../doc/models/retry-policy-enum.md) | Optional | When set to true, you can retry for failed recurring payments. The default value is true. |
| `starts_at` | `str` | Optional | Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date. |
| `status` | `str` | Required | The status of the mandate. Examples : active, revoked, completed, expired |
| `tx_variant` | `str` | Required | The transaction variant used for this mandate. |

## Example

```python
from adyen.models.amount_rule_enum import AmountRuleEnum
from adyen.models.billing_attempts_rule_enum import BillingAttemptsRuleEnum
from adyen.models.frequency_enum import FrequencyEnum
from adyen.models.token_mandate import TokenMandate

token_mandate = TokenMandate(
    amount='amount6',
    currency='currency4',
    ends_at='endsAt4',
    frequency=FrequencyEnum.MONTHLY,
    mandate_id='mandateId4',
    provider_id='providerId8',
    status='status4',
    tx_variant='txVariant2',
    account_id_type='accountIdType6',
    amount_rule=AmountRuleEnum.MAX,
    billing_attempts_rule=BillingAttemptsRuleEnum.AFTER,
    billing_day='billingDay6',
    count='count0'
)
```

