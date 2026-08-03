
# Perform Verification Request

*This model accepts additional fields of type Any.*

## Structure

`PerformVerificationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder to verify. |
| `account_state_type` | [`AccountStateType`](../../doc/models/account-state-type.md) | Required | - |
| `tier` | `int` | Required | The tier required for the account holder. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_state_type import AccountStateType
from adyen.models.perform_verification_request import PerformVerificationRequest

perform_verification_request = PerformVerificationRequest(
    account_holder_code='accountHolderCode6',
    account_state_type=AccountStateType.PAYOUT,
    tier=12,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

