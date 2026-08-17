
# Balance Check Response

## Structure

`BalanceCheckResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**. |
| `balance` | [`Amount8`](../../doc/models/amount-8.md) | Required | The balance for the payment method. |
| `fraud_result` | [`FraudResult1`](../../doc/models/fraud-result-1.md) | Optional | The fraud result properties of the payment. |
| `psp_reference` | `str` | Optional | Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `refusal_reason` | `str` | Optional | If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes `resultCode` and `refusalReason` values.<br><br>For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `result_code` | [`ResultCodeEnum`](../../doc/models/result-code-enum.md) | Required | The result of the cancellation request.<br><br>Possible values:<br><br>* **Success** – Indicates that the balance check was successful.<br>* **NotEnoughBalance** – Commonly indicates that the card did not have enough balance to pay the amount in the request, or that the currency of the balance on the card did not match the currency of the requested amount.<br>* **Failed** – Indicates that the balance check failed. |
| `transaction_limit` | [`Amount9`](../../doc/models/amount-9.md) | Optional | The maximum spendable balance for a single transaction. Applicable to some gift cards. |

## Example

```python
from adyen.models.amount_8 import Amount8
from adyen.models.amount_9 import Amount9
from adyen.models.balance_check_response import BalanceCheckResponse
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_result_1 import FraudResult1
from adyen.models.result_code_enum import ResultCodeEnum

balance_check_response = BalanceCheckResponse(
    balance=Amount8(
        currency='currency4',
        value=128
    ),
    result_code=ResultCodeEnum.SUCCESS,
    additional_data={
        'key0': 'additionalData8'
    },
    fraud_result=FraudResult1(
        account_score=232,
        results=[
            FraudCheckResult(
                account_score=102,
                check_id=246,
                name='name6'
            ),
            FraudCheckResult(
                account_score=102,
                check_id=246,
                name='name6'
            )
        ]
    ),
    psp_reference='pspReference0',
    refusal_reason='refusalReason2',
    transaction_limit=Amount9(
        currency='currency4',
        value=238
    )
)
```

