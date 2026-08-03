
# Payment Response

*This model accepts additional fields of type Any.*

## Structure

`PaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [CheckoutAwaitAction](../../doc/models/checkout-await-action.md) \| [CheckoutBankTransferAction](../../doc/models/checkout-bank-transfer-action.md) \| [CheckoutDelegatedAuthenticationAction](../../doc/models/checkout-delegated-authentication-action.md) \| [CheckoutNativeRedirectAction](../../doc/models/checkout-native-redirect-action.md) \| [CheckoutQrCodeAction](../../doc/models/checkout-qr-code-action.md) \| [CheckoutRedirectAction](../../doc/models/checkout-redirect-action.md) \| [CheckoutSDKAction](../../doc/models/checkout-sdk-action.md) \| [CheckoutThreeDS2Action](../../doc/models/checkout-three-ds-2-action.md) \| [CheckoutVoucherAction](../../doc/models/checkout-voucher-action.md) \| None | Optional | This is a container for one-of cases. |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**. |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `donation_token` | `str` | Optional | Donation Token containing payment details for Adyen Giving. |
| `fraud_result` | [`FraudResult`](../../doc/models/fraud-result.md) | Optional | - |
| `merchant_reference` | `str` | Optional | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement.<br>If you need to provide multiple references for a transaction, separate them with hyphens ("-").<br>Maximum length: 80 characters. |
| `order` | [`CheckoutOrderResponse`](../../doc/models/checkout-order-response.md) | Optional | - |
| `payment_method` | [`PaymentResponse8`](../../doc/models/payment-response-8.md) | Optional | - |
| `payment_validations` | [`PaymentResponse7`](../../doc/models/payment-response-7.md) | Optional | - |
| `psp_reference` | `str` | Optional | Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.<br><br>> For payment methods that require a redirect or additional action, you will get this value in the `/payments/details` response. |
| `refusal_reason` | `str` | Optional | If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes `resultCode` and `refusalReason` values.<br><br>For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `refusal_reason_code` | `str` | Optional | Code that specifies the refusal reason. For more information, see [Authorisation refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `result_code` | [`ResultCode1`](../../doc/models/result-code-1.md) | Optional | - |
| `three_ds_2_response_data` | [`ThreeDs2ResponseData`](../../doc/models/three-ds-2-response-data.md) | Optional | - |
| `three_ds_2_result` | [`ThreeDs2Result2`](../../doc/models/three-ds-2-result-2.md) | Optional | - |
| `three_ds_payment_data` | `str` | Optional | When non-empty, contains a value that you must submit to the `/payments/details` endpoint as `paymentData`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.checkout_await_action import CheckoutAwaitAction
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_result import FraudResult
from adyen.models.payment_response import PaymentResponse
from adyen.models.type_493 import Type493

payment_response = PaymentResponse(
    action=CheckoutAwaitAction(
        mtype=Type493.AWAIT,
        payment_data='paymentData8',
        payment_method_type='paymentMethodType8',
        url='url0',
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

