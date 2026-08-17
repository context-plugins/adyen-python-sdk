
# Logout Response

It conveys the result of the Logout.
Content of the Logout Response message.

## Structure

`LogoutResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |

## Example

```python
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.logout_response import LogoutResponse
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

logout_response = LogoutResponse(
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    )
)
```

