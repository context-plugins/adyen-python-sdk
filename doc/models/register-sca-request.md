
# Register SCA Request

## Structure

`RegisterSCARequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the SCA device that you are registering. You can use it to help your users identify the device.<br><br>If you do not specify a `name`, Adyen automatically generates one. |
| `payment_instrument_id` | `str` | Required | The unique identifier of the payment instrument for which you are registering the SCA device. |
| `strong_customer_authentication` | [`DelegatedAuthenticationData1`](../../doc/models/delegated-authentication-data-1.md) | Required | Contains information required to register the SCA device. |

## Example

```python
from adyen.models.delegated_authentication_data_1 import DelegatedAuthenticationData1
from adyen.models.register_sca_request import RegisterSCARequest

register_sca_request = RegisterSCARequest(
    payment_instrument_id='paymentInstrumentId4',
    strong_customer_authentication=DelegatedAuthenticationData1(
        sdk_output='sdkOutput4'
    ),
    name='name2'
)
```

