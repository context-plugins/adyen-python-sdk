
# Checkout Order Response

*This model accepts additional fields of type Any.*

## Structure

`CheckoutOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `expires_at` | `str` | Optional | The expiry date for the order. |
| `order_data` | `str` | Optional | The encrypted order data. |
| `psp_reference` | `str` | Required | The `pspReference` that belongs to the order. |
| `reference` | `str` | Optional | The merchant reference for the order. |
| `remaining_amount` | [`RemainingAmount`](../../doc/models/remaining-amount.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.checkout_order_response import CheckoutOrderResponse
from adyen.models.remaining_amount import RemainingAmount

checkout_order_response = CheckoutOrderResponse(
    psp_reference='pspReference8',
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    expires_at='expiresAt6',
    order_data='orderData8',
    reference='reference4',
    remaining_amount=RemainingAmount(
        currency='currency6',
        value=156,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

