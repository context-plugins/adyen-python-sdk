
# Enable Service Response

It conveys the result of the Enable Service processing.
Content of the Enable Service Response message.

## Structure

`EnableServiceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |

## Example

```python
from adyen.models.enable_service_response import EnableServiceResponse
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

enable_service_response = EnableServiceResponse(
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    )
)
```

