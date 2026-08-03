
# Data Review Confirmation Response

*This model accepts additional fields of type Any.*

## Structure

`DataReviewConfirmationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data_reviewed_at` | `str` | Optional | Date when data review was confirmed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.data_review_confirmation_response import DataReviewConfirmationResponse

data_review_confirmation_response = DataReviewConfirmationResponse(
    data_reviewed_at='dataReviewedAt8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

