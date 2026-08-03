
# Repayment 1

*This model accepts additional fields of type Any.*

## Structure

`Repayment1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `basis_points` | `int` | Required | The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp). |
| `term` | [`Term`](../../doc/models/term.md) | Optional | - |
| `threshold` | [`ThresholdRepayment`](../../doc/models/threshold-repayment.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.repayment_1 import Repayment1
from adyen.models.term import Term
from adyen.models.threshold_repayment import ThresholdRepayment

repayment_1 = Repayment1(
    basis_points=2,
    term=Term(
        estimated_days=248,
        maximum_days=24,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    threshold=ThresholdRepayment(
        amount=Amount5(
            currency='currency2',
            value=110,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

