
# Store and Forward 1

Settings for store-and-forward offline payments. The `maxAmount`, `maxPayments`, and `supportedCardTypes` parameters must be configured, either in the request or inherited from a higher level in your account structure.

*This model accepts additional fields of type Any.*

## Structure

`StoreAndForward1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_amount` | [`List[MinorUnitsMonetaryValue]`](../../doc/models/minor-units-monetary-value.md) | Optional | The maximum amount that the terminal accepts for a single store-and-forward payment. |
| `max_payments` | `int` | Optional | The maximum number of store-and-forward transactions per terminal that you can process while offline. |
| `supported_card_types` | [`SupportedCardTypes`](../../doc/models/supported-card-types.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.minor_units_monetary_value import MinorUnitsMonetaryValue
from adyen.models.store_and_forward_1 import StoreAndForward1
from adyen.models.supported_card_types import SupportedCardTypes

store_and_forward_1 = StoreAndForward1(
    max_amount=[
        MinorUnitsMonetaryValue(
            amount=50,
            currency_code='currencyCode4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        MinorUnitsMonetaryValue(
            amount=50,
            currency_code='currencyCode4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    max_payments=64,
    supported_card_types=SupportedCardTypes(
        credit=False,
        debit=False,
        deferred_debit=False,
        prepaid=False,
        unknown=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

