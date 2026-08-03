
# Verification Status

The status of the verification checks for the supporting entity capability.

Possible values:

* **pending**: Adyen is running the verification.

* **invalid**: The verification failed. Check if the `errors` array contains more information.

* **valid**: The verification has been successfully completed.

* **rejected**: Adyen has verified the information, but found reasons to not allow the capability.

## Enumeration

`VerificationStatus`

## Fields

| Name |
|  --- |
| `INVALID` |
| `PENDING` |
| `REJECTED` |
| `VALID` |

## Example

```python
from adyen.models.verification_status import VerificationStatus

verification_status = VerificationStatus.INVALID
```

