
# Calculate Rate Request Item

The request parameters required to calculate an amount in a different currency.

## Structure

`CalculateRateRequestItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exchange_side` | [`ExchangeSide2Enum`](../../doc/models/exchange-side-2-enum.md) | Required | The operation performed on the source amount. Possible values:<br><br>* **buy**<br>* **sell** |
| `source_amount` | [`Amount19`](../../doc/models/amount-19.md) | Required | An object specifying the currency and value for which you want to perform an exchange calculation. |
| `target_currency` | `str` | Required | The currency to which you want to convert the source amount. |
| `mtype` | [`RateType2Enum`](../../doc/models/rate-type-2-enum.md) | Required | The type of transaction. Possible values:<br><br>* **splitPayment**: for payments<br>* **splitRefund**: for refunds |

## Example

```python
from adyen.models.amount_19 import Amount19
from adyen.models.calculate_rate_request_item import CalculateRateRequestItem
from adyen.models.exchange_side_2_enum import ExchangeSide2Enum
from adyen.models.rate_type_2_enum import RateType2Enum

calculate_rate_request_item = CalculateRateRequestItem(
    exchange_side=ExchangeSide2Enum.BUY,
    source_amount=Amount19(
        currency='currency8',
        value=232
    ),
    target_currency='targetCurrency4',
    mtype=RateType2Enum.TRANSFER
)
```

