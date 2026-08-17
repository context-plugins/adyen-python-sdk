
# Subject Erasure Response

## Structure

`SubjectErasureResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `result` | [`Result2Enum`](../../doc/models/result-2-enum.md) | Optional | The result of this operation. |

## Example

```python
from adyen.models.result_2_enum import Result2Enum
from adyen.models.subject_erasure_response import SubjectErasureResponse

subject_erasure_response = SubjectErasureResponse(
    result=Result2Enum.PAYMENT_NOT_FOUND
)
```

