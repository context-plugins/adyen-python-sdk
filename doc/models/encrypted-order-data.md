
# Encrypted Order Data

## Structure

`EncryptedOrderData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_data` | `str` | Required | The encrypted order data.<br><br>**Constraints**: *Maximum Length*: `5000` |
| `psp_reference` | `str` | Required | The `pspReference` that belongs to the order. |

## Example

```python
from adyen.models.encrypted_order_data import EncryptedOrderData

encrypted_order_data = EncryptedOrderData(
    order_data='orderData4',
    psp_reference='pspReference4'
)
```

