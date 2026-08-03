
# Repayment 8

*This model accepts additional fields of type Any.*

## Structure

`Repayment8`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `basis_points` | `int` | Required | The repayment that is deducted daily from incoming net volume, in [basis points](https://www.investopedia.com/terms/b/basispoint.asp). |
| `term` | [`Term`](../../doc/models/term.md) | Optional | - |
| `threshold` | [`ThresholdRepayment`](../../doc/models/threshold-repayment.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.repayment_8 import Repayment8
from adyen.models.term import Term
from adyen.models.threshold_repayment import ThresholdRepayment

repayment_8 = Repayment8(
    basis_points=68,
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

