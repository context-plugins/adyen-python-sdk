
# Fraud Check Result Wrapper

*This model accepts additional fields of type Any.*

## Structure

`FraudCheckResultWrapper`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fraud_check_result` | [`FraudCheckResult`](../../doc/models/fraud-check-result.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_check_result_wrapper import FraudCheckResultWrapper

fraud_check_result_wrapper = FraudCheckResultWrapper(
    fraud_check_result=FraudCheckResult(
        account_score=114,
        check_id=2,
        name='name0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

