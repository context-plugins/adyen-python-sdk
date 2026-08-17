
# Additional Data Wallets

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

## Example

```python
from adyen.models.additional_data_wallets import AdditionalDataWallets

additional_data_wallets = AdditionalDataWallets(
    androidpay_token='androidpay.token0',
    masterpass_transaction_id='masterpass.transactionId6',
    payment_token='payment.token2',
    paywithgoogle_token='paywithgoogle.token8',
    samsungpay_token='samsungpay.token8'
)
```

