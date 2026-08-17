
# Create Order Response

## Structure

`CreateOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**. |
| `amount` | [`Amount12`](../../doc/models/amount-12.md) | Required | The initial amount of the order. |
| `expires_at` | `str` | Required | The date that the order will expire. |
| `fraud_result` | [`FraudResult1`](../../doc/models/fraud-result-1.md) | Optional | The fraud result properties of the payment. |
| `order_data` | `str` | Required | The encrypted data that will be used by merchant for adding payments to the order. |
| `psp_reference` | `str` | Optional | Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `reference` | `str` | Optional | The reference provided by merchant for creating the order. |
| `refusal_reason` | `str` | Optional | If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes `resultCode` and `refusalReason` values.<br><br>For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `remaining_amount` | [`Amount23`](../../doc/models/amount-23.md) | Required | The remaining amount in the order. |
| `result_code` | `str` | Required, Constant | The result of the order creation request.<br>The value is always **Success**.<br><br>**Value**: `"Success"` |

## Example

```python
from adyen.models.amount_12 import Amount12
from adyen.models.amount_23 import Amount23
from adyen.models.create_order_response import CreateOrderResponse
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_result_1 import FraudResult1

create_order_response = CreateOrderResponse(
    amount=Amount12(
        currency='currency2',
        value=110
    ),
    expires_at='expiresAt6',
    order_data='orderData8',
    remaining_amount=Amount23(
        currency='currency6',
        value=156
    ),
    additional_data={
        'key0': 'additionalData0',
        'key1': 'additionalData1',
        'key2': 'additionalData2'
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
    psp_reference='pspReference8',
    reference='reference4',
    refusal_reason='refusalReason0'
)
```

