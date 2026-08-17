
# Create Order Request

## Structure

`CreateOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount21`](../../doc/models/amount-21.md) | Required | The total amount of the order. |
| `expires_at` | `str` | Optional | The date when the order should expire. If not provided, the default expiry duration is 1 day.<br><br>[ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the order. |
| `reference` | `str` | Required | A custom reference identifying the order. |

## Example

```python
from adyen.models.amount_21 import Amount21
from adyen.models.create_order_request import CreateOrderRequest

create_order_request = CreateOrderRequest(
    amount=Amount21(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount4',
    reference='reference8',
    expires_at='expiresAt8'
)
```

