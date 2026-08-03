
# Checkout Forward Response from Url 2

The details of the response Adyen received from the third party.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutForwardResponseFromUrl2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `str` | Optional | The body of the response Adyen received from the third party, in string format. |
| `headers` | `Dict[str, str]` | Optional | The HTTP headers of the response Adyen received from the third party. |
| `status` | `int` | Optional | The HTTP status of the response Adyen received from the third party. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_forward_response_from_url_2 import CheckoutForwardResponseFromUrl2

checkout_forward_response_from_url_2 = CheckoutForwardResponseFromUrl2(
    body='body8',
    headers={
        'key0': 'headers5'
    },
    status=44,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

