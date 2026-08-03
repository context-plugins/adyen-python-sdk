
# Register Sca Request

*This model accepts additional fields of type Any.*

## Structure

`RegisterScaRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the SCA device that you are registering. You can use it to help your users identify the device.<br><br>If you do not specify a `name`, Adyen automatically generates one. |
| `payment_instrument_id` | `str` | Required | The unique identifier of the payment instrument for which you are registering the SCA device. |
| `strong_customer_authentication` | [`DelegatedAuthenticationData`](../../doc/models/delegated-authentication-data.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.delegated_authentication_data import DelegatedAuthenticationData
from adyen.models.register_sca_request import RegisterScaRequest

register_sca_request = RegisterScaRequest(
    payment_instrument_id='paymentInstrumentId4',
    strong_customer_authentication=DelegatedAuthenticationData(
        sdk_output='sdkOutput4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    name='name2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

