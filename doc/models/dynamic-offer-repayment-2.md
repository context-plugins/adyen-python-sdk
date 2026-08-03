
# Dynamic Offer Repayment 2

Contains information about the repayment configuration of the grant.

*This model accepts additional fields of type Any.*

## Structure

`DynamicOfferRepayment2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `term` | [`Term`](../../doc/models/term.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.dynamic_offer_repayment_2 import DynamicOfferRepayment2
from adyen.models.term import Term

dynamic_offer_repayment_2 = DynamicOfferRepayment2(
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

