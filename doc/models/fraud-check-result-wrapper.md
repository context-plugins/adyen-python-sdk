
# Fraud Check Result Wrapper

## Structure

`FraudCheckResultWrapper`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fraud_check_result` | [`FraudCheckResult`](../../doc/models/fraud-check-result.md) | Optional | - |

## Example

```python
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_check_result_wrapper import FraudCheckResultWrapper

fraud_check_result_wrapper = FraudCheckResultWrapper(
    fraud_check_result=FraudCheckResult(
        account_score=114,
        check_id=2,
        name='name0'
    )
)
```

