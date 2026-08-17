
# Risk Scores Restriction

## Structure

`RiskScoresRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`RiskScores`](../../doc/models/risk-scores.md) | Optional | - |

## Example

```python
from adyen.models.risk_scores import RiskScores
from adyen.models.risk_scores_restriction import RiskScoresRestriction

risk_scores_restriction = RiskScoresRestriction(
    operation='operation0',
    value=RiskScores(
        mastercard=84,
        visa=6
    )
)
```

