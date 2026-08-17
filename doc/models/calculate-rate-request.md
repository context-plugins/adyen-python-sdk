
# Calculate Rate Request

The request to calculate an amount in a different currency.

## Structure

`CalculateRateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exchange_calculations` | [`List[CalculateRateRequestItem]`](../../doc/models/calculate-rate-request-item.md) | Required | An array of objects, where each object defines a currency and value for which you want to perform an exchange calculation.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `1000` |

## Example

```python
from adyen.models.amount_19 import Amount19
from adyen.models.calculate_rate_request import CalculateRateRequest
from adyen.models.calculate_rate_request_item import CalculateRateRequestItem
from adyen.models.exchange_side_2_enum import ExchangeSide2Enum
from adyen.models.rate_type_2_enum import RateType2Enum

calculate_rate_request = CalculateRateRequest(
    exchange_calculations=[
        CalculateRateRequestItem(
            exchange_side=ExchangeSide2Enum.BUY,
            source_amount=Amount19(
                currency='currency8',
                value=232
            ),
            target_currency='targetCurrency8',
            mtype=RateType2Enum.TRANSFER
        )
    ]
)
```

