
# Cancel Order Request

*This model accepts additional fields of type Any.*

## Structure

`CancelOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier that orderData belongs to. |
| `order` | [`EncryptedOrderData`](../../doc/models/encrypted-order-data.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.cancel_order_request import CancelOrderRequest
from adyen.models.encrypted_order_data import EncryptedOrderData

cancel_order_request = CancelOrderRequest(
    merchant_account='merchantAccount8',
    order=EncryptedOrderData(
        order_data='orderData8',
        psp_reference='pspReference8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

