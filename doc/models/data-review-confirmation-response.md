
# Data Review Confirmation Response

## Structure

`DataReviewConfirmationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data_reviewed_at` | `str` | Optional | Date when data review was confirmed. |

## Example

```python
from adyen.models.data_review_confirmation_response import DataReviewConfirmationResponse

data_review_confirmation_response = DataReviewConfirmationResponse(
    data_reviewed_at='dataReviewedAt8'
)
```

