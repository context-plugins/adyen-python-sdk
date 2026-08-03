
# Givex Response Info

*This model accepts additional fields of type Any.*

## Structure

`GivexResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Optional | The three-character ISO currency code |
| `password` | `str` | Optional | The password provided by the acquirer. |
| `payment_flow` | `str` | Optional | The sales channel used for the payment. |
| `username` | `str` | Optional | The username provided by the acquirer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.givex_response_info import GivexResponseInfo

givex_response_info = GivexResponseInfo(
    currency_code='currencyCode0',
    password='password4',
    payment_flow='paymentFlow8',
    username='username0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

