
# Register Sca Response

*This model accepts additional fields of type Any.*

## Structure

`RegisterScaResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the SCA device you are registering. |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument for which you are registering the SCA device. |
| `sdk_input` | `str` | Optional | A string that you must pass to the authentication SDK to continue with the registration process.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `success` | `bool` | Optional | Specifies if the registration was initiated successfully. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.register_sca_response import RegisterScaResponse

register_sca_response = RegisterScaResponse(
    id='id2',
    payment_instrument_id='paymentInstrumentId4',
    sdk_input='sdkInput4',
    success=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

