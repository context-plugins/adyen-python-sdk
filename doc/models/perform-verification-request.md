
# Perform Verification Request

## Structure

`PerformVerificationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder to verify. |
| `account_state_type` | [`AccountStateTypeEnum`](../../doc/models/account-state-type-enum.md) | Required | The state required for the account holder.<br><br>> Permitted values: `Processing`, `Payout`. |
| `tier` | `int` | Required | The tier required for the account holder. |

## Example

```python
from adyen.models.account_state_type_enum import AccountStateTypeEnum
from adyen.models.perform_verification_request import PerformVerificationRequest

perform_verification_request = PerformVerificationRequest(
    account_holder_code='accountHolderCode6',
    account_state_type=AccountStateTypeEnum.PAYOUT,
    tier=12
)
```

