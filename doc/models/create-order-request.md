
# Create Order Request

*This model accepts additional fields of type Any.*

## Structure

`CreateOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `expires_at` | `str` | Optional | The date when the order should expire. If not provided, the default expiry duration is 1 day.<br><br>[ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the order. |
| `reference` | `str` | Required | A custom reference identifying the order. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.create_order_request import CreateOrderRequest

create_order_request = CreateOrderRequest(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_account='merchantAccount4',
    reference='reference8',
    expires_at='expiresAt8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

