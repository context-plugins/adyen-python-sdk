
# Network Token Activation Data Response

## Structure

`NetworkTokenActivationDataResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_input` | `str` | Optional | A block of data that contains the activation data for a network token. This `sdkInput` is required to initialize Adyen's SDK for network token provisioning.<br><br>For more information, see the repositories for Adyen's SDKs for network token provisioning:<br><br>* [Adyen Apple Pay Provisioning SDK](https://github.com/Adyen/adyen-apple-pay-provisioning-ios).<br>* [Adyen Google Wallet Provisioning SDK](https://github.com/Adyen/adyen-issuing-android) |

## Example

```python
from adyen.models.network_token_activation_data_response import NetworkTokenActivationDataResponse

network_token_activation_data_response = NetworkTokenActivationDataResponse(
    sdk_input='sdkInput4'
)
```

