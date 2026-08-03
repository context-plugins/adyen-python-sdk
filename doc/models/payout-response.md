
# Payout Response

*This model accepts additional fields of type Any.*

## Structure

`PayoutResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**. |
| `auth_code` | `str` | Optional | Authorisation code:<br><br>* When the payment is authorised successfully, this field holds the authorisation code for the payment.<br>* When the payment is not authorised, this field is empty. |
| `dcc_amount` | [`DccAmount`](../../doc/models/dcc-amount.md) | Optional | - |
| `dcc_signature` | `str` | Optional | Cryptographic signature used to verify `dccQuote`.<br><br>> This value only applies if you have implemented Dynamic Currency Conversion. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new). |
| `fraud_result` | [`FraudResult6`](../../doc/models/fraud-result-6.md) | Optional | - |
| `issuer_url` | `str` | Optional | The URL to direct the shopper to.<br><br>> In case of SecurePlus, do not redirect a shopper to this URL. |
| `md` | `str` | Optional | The payment session.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `pa_request` | `str` | Optional | The 3D request data for the issuer.<br><br>If the value is **CUPSecurePlus-CollectSMSVerificationCode**, collect an SMS code from the shopper and pass it in the `/authorise3D` request. For more information, see [3D Secure](https://docs.adyen.com/classic-integration/3d-secure). |
| `psp_reference` | `str` | Optional | Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `refusal_reason` | `str` | Optional | If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes `resultCode` and `refusalReason` values.<br><br>For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `result_code` | [`ResultCode1`](../../doc/models/result-code-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.dcc_amount import DccAmount
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_check_result_wrapper import FraudCheckResultWrapper
from adyen.models.fraud_result_6 import FraudResult6
from adyen.models.payout_response import PayoutResponse

payout_response = PayoutResponse(
    additional_data={
        'key0': 'additionalData6'
    },
    auth_code='authCode0',
    dcc_amount=DccAmount(
        currency='currency4',
        value=56,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    dcc_signature='dccSignature8',
    fraud_result=FraudResult6(
        account_score=232,
        results=[
            FraudCheckResultWrapper(
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
            ),
            FraudCheckResultWrapper(
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

