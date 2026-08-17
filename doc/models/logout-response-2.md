
# Logout Response 2

Content of the Logout Response message.

## Structure

`LogoutResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |

## Example

```python
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.logout_response_2 import LogoutResponse2
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

logout_response_2 = LogoutResponse2(
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    )
)
```

