
# Checkout Order Response 1

Contains updated information regarding the order in case order information was provided in the request.

## Structure

`CheckoutOrderResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount12`](../../doc/models/amount-12.md) | Optional | The initial amount of the order. |
| `expires_at` | `str` | Optional | The expiry date for the order. |
| `order_data` | `str` | Optional | The encrypted order data. |
| `psp_reference` | `str` | Required | The `pspReference` that belongs to the order. |
| `reference` | `str` | Optional | The merchant reference for the order. |
| `remaining_amount` | [`Amount13`](../../doc/models/amount-13.md) | Optional | The updated remaining amount. |

## Example

```python
from adyen.models.amount_12 import Amount12
from adyen.models.amount_13 import Amount13
from adyen.models.checkout_order_response_1 import CheckoutOrderResponse1

checkout_order_response_1 = CheckoutOrderResponse1(
    psp_reference='pspReference4',
    amount=Amount12(
        currency='currency2',
        value=110
    ),
    expires_at='expiresAt0',
    order_data='orderData4',
    reference='reference0',
    remaining_amount=Amount13(
        currency='currency6',
        value=156
    )
)
```

