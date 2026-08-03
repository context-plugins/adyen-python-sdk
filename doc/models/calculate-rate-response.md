
# Calculate Rate Response

The response returned when you calculate an amount in a different currency.

*This model accepts additional fields of type Any.*

## Structure

`CalculateRateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exchange_calculations` | [`List[CalculateRateResponseItem]`](../../doc/models/calculate-rate-response-item.md) | Optional | An array of objects, where each object returns a currency and value for which you performed an exchange calculation. You can use the calculated amounts in your payment requests. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.calculate_rate_response import CalculateRateResponse
from adyen.models.calculate_rate_response_item import CalculateRateResponseItem
from adyen.models.source_amount import SourceAmount
from adyen.models.target_amount import TargetAmount

calculate_rate_response = CalculateRateResponse(
    exchange_calculations=[
        CalculateRateResponseItem(
            applied_exchange_rate=140.08,
            exchange_side='exchangeSide0',
            source_amount=SourceAmount(
                currency='currency8',
                value=232,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            target_amount=TargetAmount(
                currency='currency8',
                value=168,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            mtype='type2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CalculateRateResponseItem(
            applied_exchange_rate=140.08,
            exchange_side='exchangeSide0',
            source_amount=SourceAmount(
                currency='currency8',
                value=232,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            target_amount=TargetAmount(
                currency='currency8',
                value=168,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            mtype='type2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CalculateRateResponseItem(
            applied_exchange_rate=140.08,
            exchange_side='exchangeSide0',
            source_amount=SourceAmount(
                currency='currency8',
                value=232,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            target_amount=TargetAmount(
                currency='currency8',
                value=168,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            mtype='type2',
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

