
# Additional Data Retry

## Structure

`AdditionalDataRetry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `retry_chain_attempt_number` | `str` | Optional | The number of times the transaction (not order) has been retried between different payment service providers. For instance, the `chainAttemptNumber` set to 2 means that this transaction has been recently tried on another provider before being sent to Adyen.<br><br>> If you submit `retry.chainAttemptNumber`, `retry.orderAttemptNumber`, and `retry.skipRetry` values, we also recommend you provide the `merchantOrderReference` to facilitate linking payment attempts together. |
| `retry_order_attempt_number` | `str` | Optional | The index of the attempt to bill a particular order, which is identified by the `merchantOrderReference` field. For example, if a recurring transaction fails and is retried one day later, then the order number for these attempts would be 1 and 2, respectively.<br><br>> If you submit `retry.chainAttemptNumber`, `retry.orderAttemptNumber`, and `retry.skipRetry` values, we also recommend you provide the `merchantOrderReference` to facilitate linking payment attempts together. |
| `retry_skip_retry` | `str` | Optional | The Boolean value indicating whether Adyen should skip or retry this transaction, if possible.<br><br>> If you submit `retry.chainAttemptNumber`, `retry.orderAttemptNumber`, and `retry.skipRetry` values, we also recommend you provide the `merchantOrderReference` to facilitate linking payment attempts together. |

## Example

```python
from adyen.models.additional_data_retry import AdditionalDataRetry

additional_data_retry = AdditionalDataRetry(
    retry_chain_attempt_number='retry.chainAttemptNumber6',
    retry_order_attempt_number='retry.orderAttemptNumber2',
    retry_skip_retry='retry.skipRetry8'
)
```

