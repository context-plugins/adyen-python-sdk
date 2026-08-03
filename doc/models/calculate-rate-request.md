
# Calculate Rate Request

The request to calculate an amount in a different currency.

*This model accepts additional fields of type Any.*

## Structure

`CalculateRateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exchange_calculations` | [`List[CalculateRateRequestItem]`](../../doc/models/calculate-rate-request-item.md) | Required | An array of objects, where each object defines a currency and value for which you want to perform an exchange calculation.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `1000` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.calculate_rate_request import CalculateRateRequest
from adyen.models.calculate_rate_request_item import CalculateRateRequestItem
from adyen.models.exchange_side_2 import ExchangeSide2
from adyen.models.rate_type_2 import RateType2
from adyen.models.source_amount import SourceAmount

calculate_rate_request = CalculateRateRequest(
    exchange_calculations=[
        CalculateRateRequestItem(
            exchange_side=ExchangeSide2.BUY,
            source_amount=SourceAmount(
                currency='currency8',
                value=232,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            target_currency='targetCurrency8',
            mtype=RateType2.TRANSFER,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

