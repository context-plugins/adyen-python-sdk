
# Create Order Response

*This model accepts additional fields of type Any.*

## Structure

`CreateOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**. |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `expires_at` | `str` | Required | The date that the order will expire. |
| `fraud_result` | [`FraudResult`](../../doc/models/fraud-result.md) | Optional | - |
| `order_data` | `str` | Required | The encrypted data that will be used by merchant for adding payments to the order. |
| `psp_reference` | `str` | Optional | Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `reference` | `str` | Optional | The reference provided by merchant for creating the order. |
| `refusal_reason` | `str` | Optional | If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes `resultCode` and `refusalReason` values.<br><br>For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `remaining_amount` | [`RemainingAmount`](../../doc/models/remaining-amount.md) | Required | - |
| `result_code` | [`ResultCode23`](../../doc/models/result-code-23.md) | Required | The result of the order creation request.<br>The value is always **Success**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.create_order_response import CreateOrderResponse
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_result import FraudResult
from adyen.models.remaining_amount import RemainingAmount
from adyen.models.result_code_23 import ResultCode23

create_order_response = CreateOrderResponse(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    expires_at='expiresAt6',
    order_data='orderData8',
    remaining_amount=RemainingAmount(
        currency='currency6',
        value=156,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    result_code=ResultCode23.SUCCESS,
    additional_data={
        'key0': 'additionalData0',
        'key1': 'additionalData1',
        'key2': 'additionalData2'
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
    psp_reference='pspReference8',
    reference='reference4',
    refusal_reason='refusalReason0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

