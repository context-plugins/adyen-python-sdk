
# Tax Total 2

Total tax amount from the order.

*This model accepts additional fields of type Any.*

## Structure

`TaxTotal2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount2`](../../doc/models/amount-2.md) | Optional | The transaction amount used as a base for the cost estimation. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_2 import Amount2
from adyen.models.tax_total_2 import TaxTotal2

tax_total_2 = TaxTotal2(
    amount=Amount2(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

