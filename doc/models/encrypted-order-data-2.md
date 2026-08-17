
# Encrypted Order Data 2

The order information required for partial payments.

## Structure

`EncryptedOrderData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_data` | `str` | Required | The encrypted order data.<br><br>**Constraints**: *Maximum Length*: `5000` |
| `psp_reference` | `str` | Required | The `pspReference` that belongs to the order. |

## Example

```python
from adyen.models.encrypted_order_data_2 import EncryptedOrderData2

encrypted_order_data_2 = EncryptedOrderData2(
    order_data='orderData0',
    psp_reference='pspReference0'
)
```

