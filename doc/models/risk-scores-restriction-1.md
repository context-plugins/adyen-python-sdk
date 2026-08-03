
# Risk Scores Restriction 1

Risk scores provided by specific sources. The same operation applies to all scores.

Current sources available: **visa**, **mastercard**

Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.

*This model accepts additional fields of type Any.*

## Structure

`RiskScoresRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`RiskScores`](../../doc/models/risk-scores.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.risk_scores import RiskScores
from adyen.models.risk_scores_restriction_1 import RiskScoresRestriction1

risk_scores_restriction_1 = RiskScoresRestriction1(
    operation='operation2',
    value=RiskScores(
        mastercard=84,
        visa=6,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

