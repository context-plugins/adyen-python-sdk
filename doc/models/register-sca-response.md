
# Register SCA Response

## Structure

`RegisterSCAResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the SCA device you are registering. |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument for which you are registering the SCA device. |
| `sdk_input` | `str` | Optional | A string that you must pass to the authentication SDK to continue with the registration process.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `success` | `bool` | Optional | Specifies if the registration was initiated successfully. |

## Example

```python
from adyen.models.register_sca_response import RegisterSCAResponse

register_sca_response = RegisterSCAResponse(
    id='id2',
    payment_instrument_id='paymentInstrumentId4',
    sdk_input='sdkInput4',
    success=False
)
```

