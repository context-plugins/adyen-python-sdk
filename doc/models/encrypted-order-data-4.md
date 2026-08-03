
# Encrypted Order Data 4

The order request object that contains a pspReference that represents the order and the matching encrypted order data.

*This model accepts additional fields of type Any.*

## Structure

`EncryptedOrderData4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_data` | `str` | Required | The encrypted order data.<br><br>**Constraints**: *Maximum Length*: `5000` |
| `psp_reference` | `str` | Required | The `pspReference` that belongs to the order. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.encrypted_order_data_4 import EncryptedOrderData4

encrypted_order_data_4 = EncryptedOrderData4(
    order_data='orderData4',
    psp_reference='pspReference6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

