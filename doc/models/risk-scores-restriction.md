
# Risk Scores Restriction

*This model accepts additional fields of type Any.*

## Structure

`RiskScoresRestriction`

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
from adyen.models.risk_scores_restriction import RiskScoresRestriction

risk_scores_restriction = RiskScoresRestriction(
    operation='operation0',
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

