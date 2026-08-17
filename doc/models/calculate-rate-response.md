
# Calculate Rate Response

The response returned when you calculate an amount in a different currency.

## Structure

`CalculateRateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exchange_calculations` | [`List[CalculateRateResponseItem]`](../../doc/models/calculate-rate-response-item.md) | Optional | An array of objects, where each object returns a currency and value for which you performed an exchange calculation. You can use the calculated amounts in your payment requests. |

## Example

```python
from adyen.models.amount_22 import Amount22
from adyen.models.amount_34 import Amount34
from adyen.models.calculate_rate_response import CalculateRateResponse
from adyen.models.calculate_rate_response_item import CalculateRateResponseItem

calculate_rate_response = CalculateRateResponse(
    exchange_calculations=[
        CalculateRateResponseItem(
            applied_exchange_rate=140.08,
            exchange_side='exchangeSide0',
            source_amount=Amount22(
                currency='currency8',
                value=232
            ),
            target_amount=Amount34(
                currency='currency8',
                value=168
            ),
            mtype='type2'
        ),
        CalculateRateResponseItem(
            applied_exchange_rate=140.08,
            exchange_side='exchangeSide0',
            source_amount=Amount22(
                currency='currency8',
                value=232
            ),
            target_amount=Amount34(
                currency='currency8',
                value=168
            ),
            mtype='type2'
        ),
        CalculateRateResponseItem(
            applied_exchange_rate=140.08,
            exchange_side='exchangeSide0',
            source_amount=Amount22(
                currency='currency8',
                value=232
            ),
            target_amount=Amount34(
                currency='currency8',
                value=168
            ),
            mtype='type2'
        )
    ]
)
```

