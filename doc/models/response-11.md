
# Response 11

Result of a message request processing.

## Structure

`Response11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `result` | [`Result11Enum`](../../doc/models/result-11-enum.md) | Required | Result of the processing of the message.<br>Possible values:<br><br>* **Failure**<br>* **Partial**<br>* **Success** |
| `error_condition` | [`ErrorCondition1Enum`](../../doc/models/error-condition-1-enum.md) | Optional | Condition that has produced an error on the processing of a message request.<br>Returned if Result is not Success.<br>Possible values:<br><br>* **Aborted**<br>* **Busy**<br>* **Cancel**<br>* **DeviceOut**<br>* **InProgress**<br>* **InsertedCard**<br>* **InvalidCard**<br>* **LoggedOut**<br>* **MessageFormat**<br>* **NotAllowed**<br>* **NotFound**<br>* **PaymentRestriction**<br>* **Refusal**<br>* **UnavailableDevice**<br>* **UnavailableService**<br>* **UnreachableHost**<br>* **WrongPIN** |
| `additional_response` | `str` | Optional | Additional information related to processing status of a message request.<br>If present, the POI logs it for further examination.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum

response_11 = Response11(
    result=Result11Enum.FAILURE,
    error_condition=ErrorCondition1Enum.DEVICEOUT,
    additional_response='AdditionalResponse6'
)
```

