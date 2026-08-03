
# Balance Check Response

*This model accepts additional fields of type Any.*

## Structure

`BalanceCheckResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**. |
| `balance` | [`Balance1`](../../doc/models/balance-1.md) | Required | - |
| `fraud_result` | [`FraudResult`](../../doc/models/fraud-result.md) | Optional | - |
| `psp_reference` | `str` | Optional | Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `refusal_reason` | `str` | Optional | If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes `resultCode` and `refusalReason` values.<br><br>For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `result_code` | [`ResultCode`](../../doc/models/result-code.md) | Required | - |
| `transaction_limit` | [`TransactionLimit`](../../doc/models/transaction-limit.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.balance_1 import Balance1
from adyen.models.balance_check_response import BalanceCheckResponse
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_result import FraudResult
from adyen.models.result_code import ResultCode
from adyen.models.transaction_limit import TransactionLimit

balance_check_response = BalanceCheckResponse(
    balance=Balance1(
        currency='currency4',
        value=128,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    result_code=ResultCode.SUCCESS,
    additional_data={
        'key0': 'additionalData8'
    },
    fraud_result=FraudResult(
        account_score=232,
        results=[
            FraudCheckResult(
                account_score=102,
                check_id=246,
                name='name6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            FraudCheckResult(
                account_score=102,
                check_id=246,
                name='name6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    psp_reference='pspReference0',
    refusal_reason='refusalReason2',
    transaction_limit=TransactionLimit(
        currency='currency4',
        value=238,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

