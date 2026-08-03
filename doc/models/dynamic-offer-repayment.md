
# Dynamic Offer Repayment

*This model accepts additional fields of type Any.*

## Structure

`DynamicOfferRepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `term` | [`Term`](../../doc/models/term.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.dynamic_offer_repayment import DynamicOfferRepayment
from adyen.models.term import Term

dynamic_offer_repayment = DynamicOfferRepayment(
    term=Term(
        estimated_days=248,
        maximum_days=24,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

