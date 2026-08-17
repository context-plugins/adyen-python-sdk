
# Encrypted Order Data 4

The order request object that contains a pspReference that represents the order and the matching encrypted order data.

## Structure

`EncryptedOrderData4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_data` | `str` | Required | The encrypted order data.<br><br>**Constraints**: *Maximum Length*: `5000` |
| `psp_reference` | `str` | Required | The `pspReference` that belongs to the order. |

## Example

```python
from adyen.models.encrypted_order_data_4 import EncryptedOrderData4

encrypted_order_data_4 = EncryptedOrderData4(
    order_data='orderData4',
    psp_reference='pspReference6'
)
```

