
# Confidence Score

*This model accepts additional fields of type Any.*

## Structure

`ConfidenceScore`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | `List[str]` | Optional | - |
| `score` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.confidence_score import ConfidenceScore

confidence_score = ConfidenceScore(
    errors=[
        'errors7'
    ],
    score=148.32,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

