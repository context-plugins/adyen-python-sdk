
# Calculate Rate Response Item

The response parameters returned when you calculate an amount in a different currency.

## Structure

`CalculateRateResponseItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `applied_exchange_rate` | `float` | Optional | The exchange rate to convert the source currency to the target currency. This includes Adyen's markup. |
| `exchange_side` | `str` | Optional | The operation performed on the source amount. Possible values:<br><br>* **buy**<br>* **sell** |
| `source_amount` | [`Amount22`](../../doc/models/amount-22.md) | Optional | The currency of the amount you converted (the source amount). |
| `target_amount` | [`Amount34`](../../doc/models/amount-34.md) | Optional | An object specifying the currency and value to which you want to convert the source amount (the target amount). |
| `mtype` | `str` | Optional | The type of transaction. Possible values:<br><br>* **splitPayment**: for payments<br>* **splitRefund**: for refunds |

## Example

```python
from adyen.models.amount_22 import Amount22
from adyen.models.amount_34 import Amount34
from adyen.models.calculate_rate_response_item import CalculateRateResponseItem

calculate_rate_response_item = CalculateRateResponseItem(
    applied_exchange_rate=7.04,
    exchange_side='exchangeSide6',
    source_amount=Amount22(
        currency='currency8',
        value=232
    ),
    target_amount=Amount34(
        currency='currency8',
        value=168
    ),
    mtype='type8'
)
```

