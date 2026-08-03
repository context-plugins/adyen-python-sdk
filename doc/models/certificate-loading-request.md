
# Certificate Loading Request

*This model accepts additional fields of type Any.*

## Structure

`CertificateLoadingRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The unique identifier of your merchant account. |
| `setup_token` | `str` | Required | The setup token provided by the SDK in a Mobile solution for in-person payments.<br><br>- When using the Android SDK, obtain the token through the `MerchantAuthenticationService.authenticate(setupToken)` callback of `AuthenticationService`.<br>- When using the iOS SDK, obtain the token through the `PaymentServiceDelegate.register(with:)` callback of `PaymentServiceDelegate`. |
| `store` | `str` | Optional | The reference of the store that you want to process transactions for. Do not include this parameter if your account structure uses merchant accounts as stores, or if you are a registered payment facilitator. |
| `sub_merchant_data` | [`SubMerchantData2`](../../doc/models/sub-merchant-data-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.certificate_loading_request import CertificateLoadingRequest
from adyen.models.sub_merchant_data_2 import SubMerchantData2

certificate_loading_request = CertificateLoadingRequest(
    merchant_account='merchantAccount6',
    setup_token='setupToken0',
    store='store4',
    sub_merchant_data=SubMerchantData2(
        display_name='displayName4',
        id='id8',
        mcc='mcc8',
        name='name8',
        city='city2',
        country='country2',
        email='email8',
        phone_number='phoneNumber2',
        postal_code='postalCode0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

