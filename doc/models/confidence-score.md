
# Confidence Score

## Structure

`ConfidenceScore`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | `List[str]` | Optional | - |
| `score` | `float` | Optional | - |

## Example

```python
from adyen.models.confidence_score import ConfidenceScore

confidence_score = ConfidenceScore(
    errors=[
        'errors7'
    ],
    score=148.32
)
```

