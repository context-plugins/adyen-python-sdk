
# Error Condition

Possible values:

* **Aborted**
* **Busy**
* **Cancel**
* **DeviceOut**
* **InsertedCard**
* **InProgress**
* **LoggedOut**
* **MessageFormat**
* **NotAllowed**
* **NotFound**
* **PaymentRestriction**
* **Refusal**
* **UnavailableDevice**
* **UnavailableService**
* **InvalidCard**
* **UnreachableHost**
* **WrongPIN**

## Enumeration

`ErrorCondition`

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
from adyen.models.error_condition import ErrorCondition

error_condition = ErrorCondition.REFUSAL
```

