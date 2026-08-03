
# Network Token Activation Data Response

*This model accepts additional fields of type Any.*

## Structure

`NetworkTokenActivationDataResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_input` | `str` | Optional | A block of data that contains the activation data for a network token. This `sdkInput` is required to initialize Adyen's SDK for network token provisioning.<br><br>For more information, see the repositories for Adyen's SDKs for network token provisioning:<br><br>* [Adyen Apple Pay Provisioning SDK](https://github.com/Adyen/adyen-apple-pay-provisioning-ios).<br>* [Adyen Google Wallet Provisioning SDK](https://github.com/Adyen/adyen-issuing-android) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.network_token_activation_data_response import NetworkTokenActivationDataResponse

network_token_activation_data_response = NetworkTokenActivationDataResponse(
    sdk_input='sdkInput4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

