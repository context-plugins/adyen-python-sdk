
# Calculate Rate Request Item

The request parameters required to calculate an amount in a different currency.

*This model accepts additional fields of type Any.*

## Structure

`CalculateRateRequestItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exchange_side` | [`ExchangeSide2`](../../doc/models/exchange-side-2.md) | Required | - |
| `source_amount` | [`SourceAmount`](../../doc/models/source-amount.md) | Required | - |
| `target_currency` | `str` | Required | The currency to which you want to convert the source amount. |
| `mtype` | [`RateType2`](../../doc/models/rate-type-2.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.calculate_rate_request_item import CalculateRateRequestItem
from adyen.models.exchange_side_2 import ExchangeSide2
from adyen.models.rate_type_2 import RateType2
from adyen.models.source_amount import SourceAmount

calculate_rate_request_item = CalculateRateRequestItem(
    exchange_side=ExchangeSide2.BUY,
    source_amount=SourceAmount(
        currency='currency8',
        value=232,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    target_currency='targetCurrency4',
    mtype=RateType2.TRANSFER,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

