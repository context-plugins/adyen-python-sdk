
# Cancel Order Request

## Structure

`CancelOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier that orderData belongs to. |
| `order` | [`EncryptedOrderData4`](../../doc/models/encrypted-order-data-4.md) | Required | The order request object that contains a pspReference that represents the order and the matching encrypted order data. |

## Example

```python
from adyen.models.cancel_order_request import CancelOrderRequest
from adyen.models.encrypted_order_data_4 import EncryptedOrderData4

cancel_order_request = CancelOrderRequest(
    merchant_account='merchantAccount8',
    order=EncryptedOrderData4(
        order_data='orderData8',
        psp_reference='pspReference8'
    )
)
```

