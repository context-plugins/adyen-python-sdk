
# Additional Data Wallets

*This model accepts additional fields of type Any.*

## Structure

`AdditionalDataWallets`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `androidpay_token` | `str` | Optional | The Android Pay token retrieved from the SDK. |
| `masterpass_transaction_id` | `str` | Optional | The Mastercard Masterpass Transaction ID retrieved from the SDK. |
| `payment_token` | `str` | Optional | The Apple Pay token retrieved from the SDK. |
| `paywithgoogle_token` | `str` | Optional | The Google Pay token retrieved from the SDK. |
| `samsungpay_token` | `str` | Optional | The Samsung Pay token retrieved from the SDK. |
| `visacheckout_call_id` | `str` | Optional | The Visa Checkout Call ID retrieved from the SDK. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_data_wallets import AdditionalDataWallets

additional_data_wallets = AdditionalDataWallets(
    androidpay_token='androidpay.token0',
    masterpass_transaction_id='masterpass.transactionId6',
    payment_token='payment.token2',
    paywithgoogle_token='paywithgoogle.token8',
    samsungpay_token='samsungpay.token8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

