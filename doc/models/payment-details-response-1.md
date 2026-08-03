
# Payment Details Response 1

*This model accepts additional fields of type Any.*

## Structure

`PaymentDetailsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`CheckoutThreeDs2Action`](../../doc/models/checkout-three-ds-2-action.md) | Optional | Action to be taken for completing the payment. When returned, only the 3D Secure action is needed in most cases. |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**. |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `donation_token` | `str` | Optional | Donation Token containing payment details for Adyen Giving. |
| `fraud_result` | [`FraudResult`](../../doc/models/fraud-result.md) | Optional | - |
| `merchant_reference` | `str` | Optional | The reference used during the /payments request. |
| `order` | [`CheckoutOrderResponse`](../../doc/models/checkout-order-response.md) | Optional | - |
| `payment_method` | [`PaymentResponse8`](../../doc/models/payment-response-8.md) | Optional | - |
| `payment_validations` | [`PaymentResponse7`](../../doc/models/payment-response-7.md) | Optional | - |
| `psp_reference` | `str` | Optional | Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `refusal_reason` | `str` | Optional | If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes `resultCode` and `refusalReason` values.<br><br>For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `refusal_reason_code` | `str` | Optional | Code that specifies the refusal reason. For more information, see [Authorisation refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `result_code` | [`ResultCode1`](../../doc/models/result-code-1.md) | Optional | - |
| `shopper_locale` | `str` | Optional | The shopperLocale. |
| `three_ds_2_response_data` | [`ThreeDs2ResponseData`](../../doc/models/three-ds-2-response-data.md) | Optional | - |
| `three_ds_2_result` | [`ThreeDs2Result2`](../../doc/models/three-ds-2-result-2.md) | Optional | - |
| `three_ds_payment_data` | `str` | Optional | When non-empty, contains a value that you must submit to the `/payments/details` endpoint as `paymentData`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.checkout_three_ds_2_action import CheckoutThreeDs2Action
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_result import FraudResult
from adyen.models.payment_details_response_1 import PaymentDetailsResponse1
from adyen.models.type_583 import Type583

payment_details_response_1 = PaymentDetailsResponse1(
    action=CheckoutThreeDs2Action(
        mtype=Type583.THREEDS2,
        authorisation_token='authorisationToken6',
        payment_data='paymentData4',
        payment_method_type='paymentMethodType4',
        subtype='subtype4',
        token='token6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_data={
        'key0': 'additionalData8',
        'key1': 'additionalData9'
    },
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    donation_token='donationToken0',
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

