
# Risk Scores Restriction 1

Risk scores provided by specific sources. The same operation applies to all scores.

Current sources available: **visa**, **mastercard**

Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.

## Structure

`RiskScoresRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`RiskScores`](../../doc/models/risk-scores.md) | Optional | - |

## Example

```python
from adyen.models.risk_scores import RiskScores
from adyen.models.risk_scores_restriction_1 import RiskScoresRestriction1

risk_scores_restriction_1 = RiskScoresRestriction1(
    operation='operation2',
    value=RiskScores(
        mastercard=84,
        visa=6
    )
)
```

