
# Calculate Rate Response Item

The response parameters returned when you calculate an amount in a different currency.

*This model accepts additional fields of type Any.*

## Structure

`CalculateRateResponseItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `applied_exchange_rate` | `float` | Optional | The exchange rate to convert the source currency to the target currency. This includes Adyen's markup. |
| `exchange_side` | `str` | Optional | The operation performed on the source amount. Possible values:<br><br>* **buy**<br>* **sell** |
| `source_amount` | [`SourceAmount`](../../doc/models/source-amount.md) | Optional | - |
| `target_amount` | [`TargetAmount`](../../doc/models/target-amount.md) | Optional | - |
| `mtype` | `str` | Optional | The type of transaction. Possible values:<br><br>* **splitPayment**: for payments<br>* **splitRefund**: for refunds |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.calculate_rate_response_item import CalculateRateResponseItem
from adyen.models.source_amount import SourceAmount
from adyen.models.target_amount import TargetAmount

calculate_rate_response_item = CalculateRateResponseItem(
    applied_exchange_rate=7.04,
    exchange_side='exchangeSide6',
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
    mtype='type8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

