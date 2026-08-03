
# Paypal Update Order Response

*This model accepts additional fields of type Any.*

## Structure

`PaypalUpdateOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_data` | `str` | Required | The updated paymentData. |
| `status` | [`Status42`](../../doc/models/status-42.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.paypal_update_order_response import PaypalUpdateOrderResponse
from adyen.models.status_42 import Status42

paypal_update_order_response = PaypalUpdateOrderResponse(
    payment_data='paymentData2',
    status=Status42.ERROR,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

