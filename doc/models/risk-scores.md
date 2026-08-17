
# Risk Scores

## Structure

`RiskScores`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mastercard` | `int` | Optional | Transaction risk score provided by Mastercard. Values provided by Mastercard range between 0 (lowest risk) to 998 (highest risk). |
| `visa` | `int` | Optional | Transaction risk score provided by Visa. Values provided by Visa range between 01 (lowest risk) to 99 (highest risk). |

## Example

```python
from adyen.models.risk_scores import RiskScores

risk_scores = RiskScores(
    mastercard=164,
    visa=86
)
```

