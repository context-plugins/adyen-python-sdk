
# Error Condition 1 Enum

Condition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:

* **Aborted**
* **Busy**
* **Cancel**
* **DeviceOut**
* **InProgress**
* **InsertedCard**
* **InvalidCard**
* **LoggedOut**
* **MessageFormat**
* **NotAllowed**
* **NotFound**
* **PaymentRestriction**
* **Refusal**
* **UnavailableDevice**
* **UnavailableService**
* **UnreachableHost**
* **WrongPIN**

## Enumeration

`ErrorCondition1Enum`

## Fields

| Name |
|  --- |
| `ABORTED` |
| `BUSY` |
| `CANCEL` |
| `DEVICEOUT` |
| `INSERTEDCARD` |
| `INPROGRESS` |
| `LOGGEDOUT` |
| `MESSAGEFORMAT` |
| `NOTALLOWED` |
| `NOTFOUND` |
| `PAYMENTRESTRICTION` |
| `REFUSAL` |
| `UNAVAILABLEDEVICE` |
| `UNAVAILABLESERVICE` |
| `INVALIDCARD` |
| `UNREACHABLEHOST` |
| `WRONGPIN` |

## Example

```python
from adyen.models.error_condition_1_enum import ErrorCondition1Enum

error_condition_1 = ErrorCondition1Enum.INSERTEDCARD
```

