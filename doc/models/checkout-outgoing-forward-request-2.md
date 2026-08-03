
# Checkout Outgoing Forward Request 2

The [details of the request](https://docs.adyen.com/online-payments/tokenization/forward-payment-details#request-to-adyen-card) that you want to forward to the third-party.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutOutgoingForwardRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `str` | Required | The request body that you want Adyen to forward to the third party on your behalf, in string format.<br><br>Include key value pairs to specify the payment details, and use [placeholders](https://docs.adyen.com/online-payments/tokenization/forward-payment-details#placeholders) for the values. Adyen replaces the placeholders with the payment details when making the request to the third party.<br><br>When forwarding a network token, include a [condition](https://docs.adyen.com/online-payments/tokenization/forward-payment-details#conditional-placeholders) that checks if the network token exists, and informs Adyen of which fields to send depending on the outcome.<br><br>**Constraints**: *Maximum Length*: `20000` |
| `credentials` | `str` | Optional | Your credentials that are needed to authenticate with the third party. |
| `headers` | `Dict[str, str]` | Optional | The request headers that will be included in the request Adyen makes to the third party on your behalf. Supports the `{{credentials}}` [placeholder](https://docs.adyen.com/online-payments/tokenization/forward-payment-details#placeholders). |
| `http_method` | [`HttpMethod`](../../doc/models/http-method.md) | Required | - |
| `url_suffix` | `str` | Optional | The suffix that Adyen needs to append to the `baseUrl` to construct the destination URL that belongs to the third party. This is usually the endpoint name for the request, for example, **/payments**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_outgoing_forward_request_2 import CheckoutOutgoingForwardRequest2
from adyen.models.http_method import HttpMethod

checkout_outgoing_forward_request_2 = CheckoutOutgoingForwardRequest2(
    body='body0',
    http_method=HttpMethod.POST,
    credentials='credentials8',
    headers={
        'key0': 'headers7'
    },
    url_suffix='urlSuffix0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

