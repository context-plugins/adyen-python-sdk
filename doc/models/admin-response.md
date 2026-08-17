
# Admin Response

It conveys the result of the Custom Admin.
Content of the Custom Admin Response message.

## Structure

`AdminResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |

## Example

```python
from adyen.models.admin_response import AdminResponse
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

admin_response = AdminResponse(
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    )
)
```

